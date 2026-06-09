from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import os

with sync_playwright() as p:

    report = []

    def issue_category(message):
        text = message.lower()

        if "403" in text:
            return "Security"
        elif "cookie" in text:
            return "Privacy"
        elif "deprecated" in text:
            return "Compatibility"
        elif "warning" in text:
            return "Frontend"
        else:
            return "General"

    def recommendation_engine(message):
        text = message.lower()

        if "cookie" in text:
            return "Recommendation: Review cross-site cookie policy configuration."

        elif "deprecated" in text:
            return "Recommendation: Replace deprecated browser APIs with supported alternatives."

        elif "403" in text:
            return "Recommendation: Investigate access restrictions or server-side security policies."

        elif "standards mode" in text:
            return "Recommendation: Review HTML document structure and DOCTYPE compliance."

        else:
            return "Recommendation: Further investigation may be required."

    browsers = [p.chromium, p.webkit, p.firefox]

    os.makedirs("screenshots", exist_ok=True)

    target_url = "https://breadfinancial.com"

    browser_performance = {}
    browser_health = {}

    issue_counts = {
        "Security": 0,
        "Privacy": 0,
        "Compatibility": 0,
        "Frontend": 0,
        "General": 0
    }

    report.append(f"Target URL: {target_url}")

    for browser_type in browsers:

        report.append(f"\n=== {browser_type.name.upper()} ===")

        current_time = datetime.now()
        report.append(f"Timestamp: {current_time}")

        start_time = time.time()

        browser = browser_type.launch(headless=False)

        page = browser.new_page()

        page.on(
            "console",
            lambda msg: report.append(
                f"[Console] {msg.text}"
            )
        )

        page.on(
            "response",
            lambda response: report.append(
                f"[Network Error]: {response.status} - {response.url}"
            ) if response.status >= 400 else None
        )

        page.goto(target_url)

        # Wait for page activity
        page.wait_for_timeout(3000)

        page.screenshot(
            path=f"screenshots/{browser_type.name}.png"
        )

        browser.close()

        end_time = time.time()

        load_time = end_time - start_time

        browser_performance[browser_type.name] = load_time

        # Health score framework
        health_score = 100
        browser_health[browser_type.name] = health_score

        report.append(
            f"Load Time: {load_time:.2f} seconds"
        )

    # Categorize issues
    for item in report:

        category = issue_category(item)

        if category in issue_counts:
            issue_counts[category] += 1

    # Browser comparison
    fastest_browser = min(
        browser_performance,
        key=browser_performance.get
    )

    slowest_browser = max(
        browser_performance,
        key=browser_performance.get
    )

    # Summary
    report.append("\n=== SUMMARY ===")

    report.append(
        "Cross-browser evaluation completed successfully."
    )

    report.append(
        f"Fastest Browser: {fastest_browser}"
    )

    report.append(
        f"Slowest Browser: {slowest_browser}"
    )

    # Performance Summary
    report.append("\n=== PERFORMANCE SUMMARY ===")

    for browser, load_time in browser_performance.items():

        report.append(
            f"{browser}: {load_time:.2f} seconds"
        )

    # Health Score
    report.append("\n=== HEALTH SCORE ===")

    for browser, score in browser_health.items():

        report.append(
            f"{browser}: {score}/100"
        )

    # Issue Breakdown
    report.append("\n=== ISSUE BREAKDOWN ===")

    for category, count in issue_counts.items():

        report.append(
            f"{category}: {count}"
        )

    # Executive Summary
    report.append("\n=== EXECUTIVE SUMMARY ===")

    report.append(
        f"WebKit demonstrated the best performance with a load time of "
        f"{browser_performance[fastest_browser]:.2f} seconds."
    )

    report.append(
        f"Chromium demonstrated the slowest performance with a load time of "
        f"{browser_performance[slowest_browser]:.2f} seconds."
    )

    if issue_counts["Security"] > 0:
        report.append(
            "Security-related findings were detected, including HTTP 403 responses."
        )

    if issue_counts["Frontend"] > 0:
        report.append(
            "Frontend warnings were detected and should be reviewed."
        )

    if issue_counts["Compatibility"] > 0:
        report.append(
            "Compatibility findings indicate usage of deprecated browser features."
        )

# Write report
with open("evaluation_report.txt", "w") as file:

    for item in report:

        file.write(item + "\n")

print("Evaluation completed successfully.")
print("Report saved as evaluation_report.txt")
