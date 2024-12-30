# Portfolio Analytics Hub

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=bugs)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=coverage)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=WilliamSahlstrom_portfolio-analytics-hub&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=WilliamSahlstrom_portfolio-analytics-hub)


## Description

The **Portfolio Analytics Hub** is a full-stack web application designed to showcase portfolio projects and analytics capabilities. It highlights interactive visualizations, decision support systems, machine learning integrations, and DevOps pipelines.

This app is hosted on **Netlify** (frontend) and **Render** (backend) with integrated CI/CD pipelines and code quality checks via SonarCloud.

---

## Features

- **Frontend**: Built with React.js, hosted on Netlify.
- **Backend**: Flask-powered REST API hosted on Render.
- **Database**: MySQL integration for dynamic content storage.
- **Code Quality**: Monitored and analyzed using SonarCloud.
- **CI/CD**: Automated workflows for build, test, and deploy.
- **Analytics**: Demonstrates descriptive, predictive, and prescriptive analytics.

---

## Installation

### Prerequisites

- Node.js (for frontend development)
- Python 3.11+ (for backend development)
- MySQL (local or cloud-hosted)
- Git (to clone the repository)

### Clone the Repository

```bash
git clone https://github.com/WilliamSahlstrom/portfolio-analytics-hub.git
cd portfolio-analytics-hub
```

## Usage

### Backend

1. Navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Run the Flask app locally:
    ```bash
    flask run
    ```


