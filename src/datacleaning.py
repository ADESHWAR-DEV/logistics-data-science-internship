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

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

display(df.info())

missing_values = (
    df.isnull()
      .sum()
      .sort_values(ascending=False)
)

display(missing_values.head(20))

duplicate_count = df.duplicated().sum()

print("Duplicate rows:", duplicate_count)

display(df.describe(include="all").T)

