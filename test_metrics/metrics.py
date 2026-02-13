import csv
from datetime import datetime
import os
import gspread
from google.oauth2.service_account import Credentials

class TestMetrics:
    def __init__(self):
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.start_time = datetime.now()

    def record_result(self, outcome):
        self.total += 1
        if outcome == "passed":
            self.passed += 1
        elif outcome == "failed":
            self.failed += 1
        elif outcome == "skipped":
            self.skipped += 1

    def save_to_csv(self):
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()

        failure_rate = (
            (self.failed / self.total) * 100 if self.total > 0 else 0
        )

        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, "test_metrics.csv")

        with open(file_path, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                self.total,
                self.passed,
                self.failed,
                self.skipped,
                f"{duration:.2f}",
                f"{failure_rate:.2f}"
            ])

    def save_to_google_sheets(self):
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()

        failure_rate = (
            (self.failed / self.total) * 100 if self.total > 0 else 0
        )

        # Build path to credentials file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        credentials_path = os.path.join(base_dir, "..", "credentials", "google_credentials.json")

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = Credentials.from_service_account_file(
            credentials_path,
            scopes=scopes
        )

        client = gspread.authorize(creds)

        sheet_id = "1X_DfJWwCDe9lEdRVSgCLDUIVz8PL1jtmPjYoJsj_qEw"
        sheet = client.open_by_key(sheet_id).sheet1

        sheet.append_row([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            self.total,
            self.passed,
            self.failed,
            self.skipped,
            round(duration, 2),
            round(failure_rate, 2)
        ])


