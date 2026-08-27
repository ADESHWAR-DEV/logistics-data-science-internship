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

df = pd.read_csv(
    "../data/DataCoSupplyChainDataset.csv",
    encoding="latin1"
)

print("Dataset shape:", df.shape)

display(df.head())

print(df.columns.tolist())

market_features = df.groupby("Market").agg(
    total_orders=("Order_Id", "count"),
    average_order_value=("Order_Item_Total", "mean"),
    average_shipping_days=("Days_for_shipping_real", "mean"),
    late_delivery_rate=("Late_delivery_risk", "mean")
)

display(market_features)

scaler = StandardScaler()

X_cluster = scaler.fit_transform(
    market_features
)

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

market_features["Cluster"] = (
    kmeans.fit_predict(X_cluster)
)

display(market_features)
