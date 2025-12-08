"""
Minimal sklearn pipeline example for a binary classification problem.

This is not tied to a specific dataset; it shows the typical structure:
- load data
- split
- preprocess
- train model
- evaluate
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def main():
    # Tiny in-memory example dataset.
    df = pd.DataFrame(
        {
            "amount":   [20.0, 200.0, 15.0, 500.0, 30.0, 1000.0],
            "age":      [30, 45, 22, 60, 35, 50],
            "country":  ["US", "US", "CA", "MX", "US", "CA"],
            "is_fraud": [0, 1, 0, 1, 0, 1],
        }
    )

    feature_cols = ["amount", "age", "country"]
    target_col = "is_fraud"

    X = df[feature_cols]
    y = df[target_col]

    numeric_features = ["amount", "age"]
    categorical_features = ["country"]

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    model = LogisticRegression(max_iter=1000)

    clf = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("model", model),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42,
        stratify=y,
    )

    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print("Model: LogisticRegression")
    print(f"Accuracy : {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall   : {recall:.3f}")
    print(f"F1 score : {f1:.3f}")


if __name__ == "__main__":
    main()
