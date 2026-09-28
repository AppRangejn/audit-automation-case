import pandas as pd
from model import score_transactions
from report import make_audit_report

DATA_PATH = "data/synthetic_fraud_dataset.csv"
REPORT_PATH = "audit_exceptions_report.csv"


def main():
    data = pd.read_csv(DATA_PATH)

    analyzed_data = score_transactions(data)

    make_audit_report(analyzed_data, output_file=REPORT_PATH)


if __name__ == "__main__":
    main()

