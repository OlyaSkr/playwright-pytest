# Playwright - Pytest 🚀

## Project Description 📄

This project contains automated tests for [Automation Exercise](https://automationexercise.com).  
Tests are implemented using **pytest** with **Playwright**, following the **Page Object Model (POM)** pattern.

The framework supports:

- ⚡ **Parallel execution** of tests
- 🌐 **Multiple browsers** (Chromium, Firefox, Webkit)
- 🖥️ **Consistent viewport** (1920x1080)
- 📊 **Reporting via Allure**

---

## Requirements 🛠️

- Python 3.10+
- [Playwright](https://playwright.dev/python/docs/intro)
- pytest
- pytest-playwright
- pytest-xdist (for parallel execution)
- Allure commandline

Optional:

- Any browser installed by Playwright (chromium, firefox, webkit)

## Project Structure 📁

```

├── helpers/           # Helper module to generate random user and payment data
├── pages/             # Page Object files
├── test_data/         # Test data files
├── tests/             # Test specifications
├── conftest.py        # Pytest fixtures and hooks
├── pytest.ini         # Pytest configuration
├── requirements.txt   # Project dependencies

```

## Installation Steps 💻

### 1. Clone the repository:

```bash
git clone https://github.com/OlyaSkr/playwright-pytest.git
cd <playwright-pytest>
```

### 2. Create a virtual environment:

#### Linux/macOS

```
python -m venv venv
source venv/bin/activate
```

#### Windows

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies:

```
pip install -r requirements.txt
```

### 4. Install Playwright browsers:

```
playwright install
```

### 5. Install Allure commandline:

- Mac/Linux (brew or scoop)

```
brew install allure
```

- Windows (download from [Allure site](https://allurereport.org/docs/#_installing_a_commandline))

## Running Tests ▶️

### 1. Run all tests on the default browser (Chromium):

```
pytest
```

### 2. Run tests on a specific browsers:

#### runs tests in Chromium (default):

```
pytest --browser chromium
```

#### runs tests in Firefox:

```
pytest --browser=firefox
```

#### runs tests in WebKit (Safari engine):

```
pytest --browser webkit
```

### 3. Run tests in parallel:

To speed up execution, use pytest-xdist:

- n 4 → runs tests in 4 parallel workers in Chromium:

```
pytest -n 4 --browser chromium
```

- n auto → uses all available CPU cores in firefox:

```
pytest -n auto --browser firefox
```

### 4. Run a specific test file:

```
pytest tests/test_login.py
```

### 5. Run a specific test case:

```
pytest -k "test_login_with_incorrect_email_and_password"
```

## Generating Allure Report 📊

### Generate an allure reprot:

```
allure generate reports/allure-results -o reports/allure-report --clean
```

### Open an allure report:

```
allure open reports/allure-report
```
