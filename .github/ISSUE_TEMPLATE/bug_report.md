name: Bug Report
description: Report a bug or issue with workflow execution or asset rendering
labels: [bug]
body:
  - type: markdown
    attributes:
      value: Thank you for reporting! Please fill in the details below.
  - type: textarea
    id: describe-bug
    attributes:
      label: Bug Description
      placeholder: Describe the problem clearly
    validations:
      required: true
  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Steps to Reproduce
      placeholder: List the exact steps or trigger conditions
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Workflow Logs or Error Messages
      placeholder: Paste any error messages from the actions tab here
    validations:
      required: false
