# AI-Assisted QA Automation Playground

This project demonstrates how AI tools can be responsibly integrated into modern Quality Assurance workflows.

The goal is not to replace QA expertise, but to enhance:
- Test design
- Automation efficiency
- Visual validation
- Defect analysis and reporting

## 🔧 Tech Stack
- Selenium (Python)
- Applitools (Visual AI Testing)
- ChatGPT (Test generation, analysis, and automation assistance)
- GitHub Actions

## 🧪 Project Modules

### 1. AI-Generated Manual Test Cases
- Created functional and edge-case test scenarios using AI
- Reviewed and refined outputs using QA best practices
- Stored in markdown for traceability

### 2. AI-Assisted Automation
- Converted manual tests into Selenium automation
- Used AI to accelerate script creation
- Improved reliability with waits, assertions, and selector optimization

### 3. AI Visual Testing
- Integrated Applitools for visual regression testing
- Detected UI inconsistencies missed by functional tests

### 4. Defect Analysis & Reporting
- Used AI to analyze test failures
- Generated professional bug reports
- Validated accuracy before documentation

### 5. CI Integration
- Designed automation to be CI-ready using pytest fixtures and environment-based configuration
- Reduced flaky failures with condition-based waits instead of static delays
- Structured tests for easy integration into GitHub Actions or other CI pipelines


## 📁 Repository Structure

## 📌 Current Status
- Manual test cases completed for Login and Dynamic Elements 
- Edge cases generated and reviewed using AI assistance
- Automation and visual testing complete
- Selenium + pytest automation
- Explicit waits to reduce flaky tests
- Handling real browser interference (e.g. password manager popups)
- AI-powered visual testing using Applitools

## Automation
✅ Login Automation
- The login flow is covered with both functional and edge-case scenarios, including:
    Valid login and logout flows
    Invalid username and password handling
    Empty credentials and whitespace edge cases
    Session behavior after logout and page refresh
- Tests use explicit waits to ensure stability and reliability and include logic to handle real browser interruptions (such as password manager popups) to reduce flakiness.

## Visual Testing
✅ Visual regression testing is implemented using Applitools Eyes to detect UI changes that functional assertions may miss.
These tests validate:
- Page layout and structure
- Visual consistency after login
- UI regressions caused by styling or DOM changes

