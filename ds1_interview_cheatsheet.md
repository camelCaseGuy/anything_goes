# Data Scientist I – Interview Cheatsheet

This file is a quick reference for concepts I expect to be asked about
for an entry-level / DS1 role (with banking context).

---

## 1. SQL patterns

**Joins**

```sql
SELECT
    c.customer_id,
    c.company_name,
    o.order_id,
    o.order_date
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id;
```

**Aggregations**

```sql
SELECT
    customer_id,
    COUNT(*) AS num_orders,
    SUM(total_amount) AS total_spend
FROM orders
GROUP BY customer_id
HAVING COUNT(*) >= 3;
```

**Window functions – last order per customer**

```sql
SELECT *
FROM (
    SELECT
        customer_id,
        order_id,
        order_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY order_date DESC
        ) AS rn
    FROM orders
) t
WHERE rn = 1;
```

**CASE expressions**

```sql
SELECT
    company_name,
    CASE
        WHEN country = 'USA' THEN 'Local'
        ELSE 'Foreign'
    END AS market_segment
FROM customers;
```

---

## 2. Python + pandas patterns

**Basic exploration**

```python
import pandas as pd

df = pd.read_csv("data.csv")

df.head()
df.info()
df.describe()

# Filter
recent = df[df["event_date"] >= "2024-01-01"]

# Group and aggregate
agg = (
    df.groupby("customer_id")["amount"]
      .agg(["count", "sum", "mean"])
      .reset_index()
)
```

**Joining / merging**

```python
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

orders_with_cust = orders.merge(
    customers,
    on="customer_id",
    how="left"
)
```

---

## 3. Typical ML workflow (sklearn style)

High-level steps I would describe in an interview:

1. **Understand the business problem**  
   - e.g., detect fraudulent transactions, predict churn, rank leads.

2. **Get and explore the data**  
   - inspect schema, missingness, basic distributions.

3. **Preprocess / feature engineering**  
   - handle missing values  
   - encode categoricals  
   - scale numeric features if necessary  
   - create domain features (ratios, time-based features, etc.).

4. **Train/test (and validation) split**

```python
from sklearn.model_selection import train_test_split

X = df[feature_cols]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

5. **Choose a baseline model**

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

6. **Evaluate**

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall    = recall_score(y_test, y_pred)
f1        = f1_score(y_test, y_pred)
```

7. **Iterate / tune / compare models**  
   - try tree-based models, regularization, class weights, etc.

8. **Communicate results**  
   - focus on impact: precision/recall trade-offs, business thresholds, and how stakeholders use the predictions.

---

## 4. Evaluation metrics – quick definitions

For a binary classification problem (e.g., fraud / not fraud):

- **Accuracy**:  
  `(TP + TN) / (TP + TN + FP + FN)`  
  *“Of all predictions, how many did we get right?”*

- **Precision**:  
  `TP / (TP + FP)`  
  *“When we predict positive, how often are we correct?”*

- **Recall (Sensitivity / TPR)**:  
  `TP / (TP + FN)`  
  *“Of all actual positives, how many did we catch?”*

- **F1 score**:  
  harmonic mean of precision and recall  
  *Balances precision and recall when classes are imbalanced.*

- **ROC-AUC**:  
  probability that the model ranks a random positive higher than a random negative.

I can also talk about **confusion matrices** to make these metrics concrete.

---

## 5. Feature engineering ideas

Examples I can mention:

- **Missing values**
  - numeric: median, mean, or domain-specific default  
  - categorical: `"Unknown"` category or separate flag

- **Categorical encoding**
  - one-hot encoding for low/medium cardinality  
  - target / frequency encoding for high cardinality (with care to avoid leakage)

- **Scaling**
  - `StandardScaler` or `MinMaxScaler` for models like logistic regression, SVMs, KNN

- **Date / time**
  - extract year, month, day of week, hour  
  - time since last event, rolling counts in last N days

- **Domain-specific**
  - for transactions: average amount per customer, ratio of current amount to typical amount, merchant risk signals, time-of-day anomalies.

---

## 6. Banking / fraud / risk examples (how I’d talk about them)

**Fraud detection (classification)**

- **Goal**: flag suspicious transactions for review.  
- **Features**: transaction amount, time, location, device, previous customer behavior.  
- **Models**: logistic regression, tree-based models (RandomForest, XGBoost).  
- **Metrics**: precision/recall, F1, PR-AUC – sometimes prioritize recall to catch more fraud, but with acceptable false positives.  

**Credit risk (default prediction)**

- **Goal**: predict probability of default or delinquency.  
- **Features**: income, utilization, payment history, number of recent inquiries, length of credit history.  
- **Outputs**: probability score that feeds into risk bands / pricing decisions.

**Customer churn (retention)**

- **Goal**: predict which customers are likely to leave or become inactive.  
- **Features**: product usage, complaints, service interactions, drop in activity.  
- **Action**: targeted retention offers, outreach, or product changes.

---

## 7. Behavioral / communication notes

Key points I may remind myself of:

- Keep answers **short and structured** (30–60 seconds).  
- Use **S.T.A.R.** for stories:
  - Situation
  - Task
  - Action
  - Result
- Emphasize:
  - collaboration with stakeholders
  - documenting work
  - being careful with data quality and assumptions
  - learning mindset (continuous improvement).
