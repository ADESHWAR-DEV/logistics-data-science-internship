import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

from sklearn.cluster import KMeans

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("Libraries imported successfully.")

total_shipments = len(df)

late_shipments = df["Late_delivery_risk"].sum()

late_delivery_rate = (
    late_shipments / total_shipments
) * 100

on_time_delivery_rate = 100 - late_delivery_rate

print(f"Total shipments: {total_shipments}")
print(f"Late delivery rate: {late_delivery_rate:.2f}%")
print(f"On-time delivery rate: {on_time_delivery_rate:.2f}%")

kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Shipments",
        "Late Delivery Rate",
        "On-Time Delivery Rate"
    ],
    "Value": [
        total_shipments,
        late_delivery_rate,
        on_time_delivery_rate
    ]
})

display(kpi_summary)

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x="Shipping_Mode",
    hue="Late_delivery_risk"
)

plt.title("Late Delivery Risk by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Number of Shipments")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x="Market",
    hue="Late_delivery_risk"
)

plt.title("Late Delivery Risk by Market")
plt.xlabel("Market")
plt.ylabel("Shipments")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
