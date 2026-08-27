features = [
    "Shipping_Mode",
    "Market",
    "Order_Item_Total",
    "Days_for_shipping_real",
    "Days_for_shipment_scheduled"
]

target = "Late_delivery_risk"

model_df = df[features + [target]].dropna()

X = model_df[features]
y = model_df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

categorical_features = [
    "Shipping_Mode",
    "Market"
]

numeric_features = [
    "Order_Item_Total",
    "Days_for_shipping_real",
    "Days_for_shipment_scheduled"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            StandardScaler(),
            numeric_features
        )
    ]
)

classifier = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(max_iter=1000)
        )
    ]
)

classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)

print(classification_report(y_test, predictions))

