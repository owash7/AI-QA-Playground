# Dynamic Elements Test Cases
Application: https://the-internet.herokuapp.com/dynamic_loading

## Functional Test Cases

| Test Case ID | Description                              | Steps                                                        | Expected Result                                     |
|--------------|------------------------------------------|--------------------------------------------------------------|-----------------------------------------------------|
| TC-DYN-001   | Verify element appears after loading     | 1. Navigate to Dynamic Loading Example 1 <br> 2. Click Start | Loading indicator appears, followed by text display |
| TC-DYN-002   | Verify hidden element becomes visible    | Navigate to Example 1, click Start                           | Hidden text becomes visible after loading           |
| TC-DYN-003   | Verify element is rendered after loading | Navigate to Example 2, click Start                           | Element is added to DOM after loading               |
| TC-DYN-004   | Validate loading spinner visibility      | Click Start                                                  | Spinner displays during loading                     |

## Edge & Timing Test Cases

| Test Case ID | Description                                     | Steps                         | Expected Result                        |
|--------------|-------------------------------------------------|-------------------------------|----------------------------------------|
| TC-DYN-005   | Refresh page during loading                     | Click Start → Refresh browser | Page resets cleanly                    |
| TC-DYN-006   | Click Start multiple times                      | Click Start repeatedly        | App handles action gracefully          |
| TC-DYN-007   | Navigate away during loading                    | Click Start → Change page     | No crash or UI freeze                  |
| TC-DYN-008   | Verify timeout handling                         | Simulate slow load            | Message appears once loading completes |
| TC-DYN-009   | Verify element visibility without explicit wait | Observe behavior              | Element should not appear prematurely  |
