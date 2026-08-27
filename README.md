# Strategic Planning and Data Exploration in Logistics

## Internship Task 1

This project presents a data-driven approach to logistics and supply-chain
planning using Python.

The project focuses on shipment performance, delivery risk, logistics KPIs,
customer/market segmentation, predictive analytics and route optimization.

---

## Project Objective

The objective of this project is to demonstrate how data science can be
applied to common logistics challenges such as:

- Late deliveries
- Delivery-time variability
- Shipment performance
- Demand and capacity planning
- Customer/market segmentation
- Transportation efficiency
- Route optimization

The project follows an end-to-end data science workflow:

Business Understanding
        ↓
Data Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
KPI Analysis
        ↓
Predictive Modelling
        ↓
Clustering
        ↓
Route Optimization
        ↓
Business Recommendations

---

## Dataset

The project uses the publicly available:

**DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS**

Dataset source:

Mendeley Data:
https://data.mendeley.com/datasets/8gx2fvg2k6/1

DOI:

10.17632/8gx2fvg2k6

The dataset contains supply-chain transaction information and is used for
educational and analytical purposes.

The raw dataset is not included in this repository. Follow the instructions
inside the `data/README.md` file to obtain the dataset.

---

## Key Performance Indicators

The project evaluates several logistics KPIs.

### 1. On-Time Delivery Rate

On-Time Delivery Rate =
(On-Time Shipments / Total Eligible Shipments) × 100

### 2. Late Delivery Rate

Late Delivery Rate =
(Late Shipments / Total Eligible Shipments) × 100

### 3. Average Delivery Lead Time

Average Delivery Lead Time =
Mean(Actual Delivery Date - Shipment Date)

### 4. Delivery-Time Variability

Measured using standard deviation and percentile-based statistics.

### 5. Cancellation Rate

Cancellation Rate =
(Cancelled Orders / Total Orders) × 100

Additional KPIs include transportation cost per shipment,
vehicle utilization and route distance per successful delivery when the
required operational data is available.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google OR-Tools
- Jupyter Notebook

---

## Data Science Techniques

### Exploratory Data Analysis

Used to identify:

- Delivery trends
- Regional performance
- Shipping-mode performance
- Product-category behaviour
- Outliers
- Correlations

### Classification

A classification model is proposed to predict whether a shipment is likely
to experience late delivery.

### Regression

Regression can be used to estimate delivery time.

### Clustering

K-Means clustering is used to identify groups of markets/customers with
similar logistics characteristics.

### Forecasting

Historical shipment/order volume can be aggregated over time to support
future capacity planning.

### Route Optimization

Google OR-Tools can be used to solve Vehicle Routing Problems subject to
capacity and time-window constraints.

---

## Repository Structure

```text
logistics-data-science-internship/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── Task_1_Logistics_Data_Analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── kpi_analysis.py
│   ├── predictive_model.py
│   ├── clustering.py
│   └── route_optimization.py
│
├── outputs/
│   ├── figures/
│   └── tables/
│
└── report/
    └── Task_1_Strategic_Planning_and_Data_Exploration_in_Logistics.docx
