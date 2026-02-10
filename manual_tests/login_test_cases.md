# Login Test Cases
Application: https://the-internet.herokuapp.com/login

## Functional Test Cases

| Test Case ID | Description                                   | Steps                                                                                                       | Expected Result                                              |
|--------------|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| TC-LGN-001   | Login with valid credentials                  | 1. Navigate to login page <br> 2. Enter valid username <br> 3. Enter valid password <br> 4. Click Login     | User is successfully logged in and redirected to secure area |
| TC-LGN-002   | Login with invalid username                   | 1. Navigate to login page <br> 2. Enter invalid username <br> 3. Enter valid password <br> 4. Click Login   | Error message displayed indicating invalid username          |
| TC-LGN-003   | Login with invalid password                   | 1. Navigate to login page <br> 2. Enter valid username <br> 3. Enter invalid password <br> 4. Click Login   | Error message displayed indicating invalid password          |
| TC-LGN-004   | Login with both username and password invalid | 1. Navigate to login page <br> 2. Enter invalid username <br> 3. Enter invalid password <br> 4. Click Login | Error message displayed                                      |
| TC-LGN-005   | Logout after successful login                 | 1. Login with valid credentials <br> 2. Click Logout                                                        | User is logged out and redirected to login page              |

## Edge & Negative Test Cases

| Test Case ID | Description                              | Steps                                             | Expected Result                           |
|--------------|------------------------------------------|---------------------------------------------------|-------------------------------------------|
| TC-LGN-006   | Submit login form with empty username    | Leave username empty, enter password, click Login | Error message displayed                   |
| TC-LGN-007   | Submit login form with empty password    | Enter username, leave password empty, click Login | Error message displayed                   |
| TC-LGN-008   | Submit login form with both fields empty | Leave both fields empty, click Login              | Error message displayed                   |
| TC-LGN-009   | Use leading/trailing spaces in username  | Enter username with spaces, valid password        | Login fails or trims spaces appropriately |
| c            |

