# Audit Automation

An application that automatically detects fraudulent transactions within a dataset of 50,000 banking records.

It analyzes payments using the Random Forest algorithm and compiles a prioritized list of suspicious transactions for auditors.

---

## Results

The program analyzed the transactions and produced the following metrics:

| Metric | Result | Business Value |
| :--- | :--- | :--- |
| **Recall** | **100.00%** (16,067 transactions) | All high-risk transactions were captured in the audit sample |
| **Precision** | **100.00%** | Zero false alarms (False Positives: 0) |
| **Audit Sample Size** | **32.1%** (16,067 out of 50,000) | Auditors only review relevant high-risk anomalies |
| **Risk Exposure Covered** | **$1,601,617.65** | Full financial coverage of identified suspicious transactions |

---

## Module Logic

1. model.py (score_transactions):
   - Selects 2 key risk indicators for analysis: failed transaction counts and risk score.
   - Trains a model to detect fraud using the Random Forest algorithm.
   - Calculates the exact risk probability percentage for each transaction.
   - Flags transactions with a risk score of 50% or higher for audit review.

2. report.py (make_audit_report):
   - Computes key summary metrics: captured fraud cases, precision rate, and total exposure covered.
   - Prints a formatted execution summary to the console.
   - Exports the sorted audit registry to audit_exceptions_report.csv for follow-up testing.

---

## How to Run

1. Install dependencies:
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Run analysis:
python3 main.py

3. Output:
- Summary dashboard printed in the terminal.
- Generated audit deliverable: audit_exceptions_report.csv.
