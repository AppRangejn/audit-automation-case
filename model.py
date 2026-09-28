import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def score_transactions(data: pd.DataFrame) -> pd.DataFrame:
    data = data.copy()

    features = ['Failed_Transaction_Count_7d', 'Risk_Score']
    X = data[features]
    y = data['Fraud_Label']

    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X, y)

    data['Risk_Probability'] = model.predict_proba(X)[:, 1].round(4)
    data['Audit_Score'] = (data['Risk_Probability'] * 100).astype(int)

    data['Need_Audit'] = data['Risk_Probability'] >= 0.50

    return data
