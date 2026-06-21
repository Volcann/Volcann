import os
import re
import unittest
import xml.etree.ElementTree as ET


class TestRepositoryAssets(unittest.TestCase):

    def setUp(self):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.readme_path = os.path.join(self.root_dir, "README.md")
        self.profile_3d_dir = os.path.join(self.root_dir, "profile-3d-contrib")

    def test_readme_exists(self):
        self.assertTrue(os.path.isfile(self.readme_path))

    def test_svg_xml_wellformedness(self):
        svg_files = []
        for root, _, files in os.walk(self.root_dir):
            if ".git" in root or ".venv" in root or "venv" in root:
                continue
            for file in files:
                if file.endswith(".svg"):
                    svg_files.append(os.path.join(root, file))

        self.assertTrue(len(svg_files) > 0)

        for svg_path in svg_files:
            rel_path = os.path.relpath(svg_path, self.root_dir)
            with self.subTest(svg=rel_path):
                self.assertTrue(os.path.getsize(svg_path) > 0)
                try:
                    tree = ET.parse(svg_path)
                    root_elem = tree.getroot()
                    tag = root_elem.tag
                    local_tag = tag.split('}')[-1] if '}' in tag else tag
                    self.assertEqual(local_tag.lower(), "svg")
                except ET.ParseError as e:
                    self.fail()

    def test_readme_local_links_and_images(self):
        if not os.path.isfile(self.readme_path):
            self.skipTest()

        with open(self.readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        md_links = re.findall(r'\[.*?\]\((?!https?://|mailto:)(.*?)\)', content)
        md_images = re.findall(r'!\[.*?\]\((?!https?://)(.*?)\)', content)
        html_srcs = re.findall(r'src=["\'](?!https?://)(.*?)["\']', content)
        html_hrefs = re.findall(r'href=["\'](?!https?://|mailto:)(.*?)["\']', content)

        all_local_references = set(md_links + md_images + html_srcs + html_hrefs)

        for ref in all_local_references:
            ref_clean = ref.split('#')[0].split('?')[0].strip()
            if not ref_clean:
                continue
            if ref_clean.startswith('/') or ref_clean.startswith('http'):
                continue
            target_path = os.path.normpath(os.path.join(self.root_dir, ref_clean))
            with self.subTest(reference=ref):
                self.assertTrue(os.path.exists(target_path))


if __name__ == "__main__":
    unittest.main()
