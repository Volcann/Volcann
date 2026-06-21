# Contributing to Volcann

Thank you for your interest in improving the Volcann repository! Please follow these guidelines:

## Code of Conduct

By participating in this project, you agree to abide by the Code of Conduct.

## Getting Started

1. Fork the repository and clone it locally.
2. Initialize the development environment and install verification hooks:
   ```bash
   make setup
   ```

## Development and Verification Flow

* Do not add comments or docstrings to workflow configurations, scripts, or test code.
* Ensure all workflow YAML files are valid and follow guidelines.
* Run the validation suite to check XML well-formedness of SVG assets and verify local link integrity:
   ```bash
   make test
   ```
* Before committing, execute `make lint` to run the formatting and style check rules.

## Pull Request Guidelines

1. Make changes in a descriptive branch.
2. Ensure all tests run and pass.
3. Submit a pull request using the provided template.
