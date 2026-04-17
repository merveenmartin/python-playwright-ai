import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from _pytest.reports import TestReport
from ai.debugger import analyze_test_failure


def pytest_runtest_logreport(report: TestReport) -> None:
    if report.failed and report.when == "call":
        print(f"\n{'=' * 60}")
        print("AI FAILURE ANALYSIS")
        print("=" * 60)
        analysis = analyze_test_failure(
            test_name=report.nodeid,
            error_message=str(report.longrepr),
            log_snippet=report.capstdout or "No logs captured",
        )
        print(analysis)
        print("=" * 60)

