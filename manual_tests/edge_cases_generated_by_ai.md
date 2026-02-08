# AI-Generated Edge Cases – Login

## Identified Risk-Based Scenarios

- Multiple failed login attempts in succession
- Session persistence after logout
- Browser back navigation after logout
- Input field handling of whitespace
- Error message consistency and clarity

## Additional Edge Test Cases

| Test Case ID | Description                                            | Risk Addressed                |
|--------------|--------------------------------------------------------|-------------------------------|
| TC-LGN-011   | Attempt login after browser refresh mid-authentication | Session handling              |
| TC-LGN-012   | Navigate directly to /secure URL without login         | Authorization enforcement     |
| TC-LGN-013   | Click login button multiple times rapidly              | Duplicate submission handling |
| TC-LGN-014   | Login using copied/pasted credentials                  | Input handling                |
| TC-LGN-015   | Open login page in multiple tabs and authenticate      | Session consistency           |

## Notes
These cases were generated using AI assistance and reviewed to ensure relevance, realism, and alignment with QA best practices.
