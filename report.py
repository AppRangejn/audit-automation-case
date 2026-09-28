import pandas as pd

def make_audit_report(data: pd.DataFrame, output_file: str = "audit_exceptions_report.csv") -> None:
    transactions_to_audit = data[data['Need_Audit'] == True]

    total_transactions = len(data)
    total_flagged = len(transactions_to_audit)
    total_fraud = int(data['Fraud_Label'].sum())

    caught_fraud = int(transactions_to_audit['Fraud_Label'].sum())
    false_alarms = total_flagged - caught_fraud

    recall = (caught_fraud / total_fraud) * 100
    precision = (caught_fraud / total_flagged) * 100

    total_risk_money = transactions_to_audit['Transaction_Amount'].sum()
    saved_money = transactions_to_audit.loc[transactions_to_audit['Fraud_Label'] == 1, 'Transaction_Amount'].sum()

    print("AUDIT")
    print(f"Total Transactions:        {total_transactions:,}")
    print(f"Sampled for Audit:         {total_flagged:,} ({total_flagged / total_transactions * 100:.1f}%)")
    print(f"Target Exceptions (Fraud): {total_fraud:,}")
    print(f"True Positives (Recall):   {caught_fraud:,} ({recall:.2f}%)")
    print(f"False Positives:           {false_alarms}")
    print(f"Sampling Precision:        {precision:.2f}%")
    print(f"Total Risk Exposure:       ${total_risk_money:,.2f}")
    print(f"Intercepted Exposure:      ${saved_money:,.2f}")

    columns_to_export = [
        'Transaction_ID',
        'User_ID',
        'Transaction_Amount',
        'Risk_Probability',
        'Audit_Score',
        'Fraud_Label'
    ]
    transactions_to_audit[columns_to_export].sort_values(
        by='Risk_Probability',
        ascending=False
    ).to_csv(output_file, index=False)
