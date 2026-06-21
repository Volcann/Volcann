name: Feature Request
description: Propose an automation improvement, asset style, or layout update
labels: [enhancement]
body:
  - type: markdown
    attributes:
      value: Thank you for suggesting a new idea! Please fill in the details below.
  - type: textarea
    id: feature-description
    attributes:
      label: Feature Description
      placeholder: Describe the enhancement or idea clearly
    validations:
      required: true
  - type: textarea
    id: use-case
    attributes:
      label: Use Case & Motivation
      placeholder: Explain why this is beneficial
    validations:
      required: true
