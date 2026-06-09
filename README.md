# AI-Web-Evaluator

## Overview

AI-Web-Evaluator is a Python-based cross-browser website evaluation framework built using Playwright. The tool automatically evaluates website behavior across Chromium, WebKit, and Firefox while collecting performance metrics, browser console messages, network errors, screenshots, and categorized findings.

The objective of this project is to provide automated browser compatibility and performance analysis that can be used by QA Engineers, Developers, Product Teams, and Engineering Leadership to quickly identify potential issues affecting website quality.

---

## Features

### Cross-Browser Testing

* Chromium
* WebKit
* Firefox

### Performance Monitoring

* Page load time measurement
* Browser performance comparison
* Fastest browser detection
* Slowest browser detection

### Console Monitoring

* JavaScript warnings
* JavaScript errors
* Browser compatibility warnings

### Network Monitoring

* HTTP error detection
* Failed request tracking
* Security response monitoring (403, 404, 500, etc.)

### Screenshot Capture

* Automatic screenshot generation
* Browser-specific evidence collection

### Issue Categorization

* Security Issues
* Privacy Issues
* Compatibility Issues
* Frontend Issues
* General Findings

### Executive Reporting

* Structured evaluation report
* Browser comparison summary
* Executive-level findings summary

---

## Technology Stack

* Python 3
* Playwright
* Chromium
* WebKit
* Firefox

---

## Project Structure

AI-Web-Evaluator/

├── main.py

├── README.md

├── requirements.txt

├── evaluation_report.txt

├── screenshots/

│   ├── chromium.png

│   ├── webkit.png

│   └── firefox.png

├── reports/

│   └── sample_report.txt

└── docs/

```
└── architecture.txt
```

---

## Installation

### Install Python Dependencies

```bash
pip install playwright
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Run the Project

```bash
python3 main.py
```

---

## Sample Output

## Browser Screenshots

### Chromium

![Chromium](screenshots/chromium.png)

### WebKit

![WebKit](screenshots/webkit.png)

### Firefox

![Firefox](screenshots/firefox.png)
=== SUMMARY ===

Cross-browser evaluation completed successfully.

Fastest Browser: webkit

Slowest Browser: chromium

=== PERFORMANCE SUMMARY ===

chromium: 12.53 seconds

webkit: 4.53 seconds

firefox: 4.72 seconds

=== ISSUE BREAKDOWN ===

Security: 5

Privacy: 0

Compatibility: 1

Frontend: 4

General: 12
```

---

## Key Capabilities

* Automated browser compatibility testing
* Website performance benchmarking
* Console error and warning monitoring
* Network error detection
* Screenshot-based evidence collection
* Issue classification and reporting
* Executive summary generation

---

## Future Enhancements

* AI-generated recommendations
* Dynamic browser health scoring
* Historical trend analysis
* Multi-page website evaluation
* Dashboard visualization
* PDF report generation
* AI-powered issue prioritization

---

## Business Value

This framework helps engineering teams quickly identify:

* Browser-specific compatibility issues
* Performance bottlenecks
* Security-related findings
* Frontend code quality concerns
* Website behavior differences across browsers

The generated reports provide both technical findings and executive-level summaries, enabling faster decision-making and issue prioritization.

---

## Author

Rupa Chintamaneni

QA Automation Engineer | Python Automation | Playwright | Browser Testing | AI Engineering

---

## Version

AI-Web-Evaluator v1.0
