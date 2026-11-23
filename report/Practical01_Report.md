# CET3001 – Educational Data Mining and Learning Analytics

# PRACTICAL FILE

---

## COVER PAGE

| Field | Details |
|---|---|
| **Name** | SHRIYASH SAHU |
| **Registration Number** | 24BET10001 |
| **Course Code** | CET3001 |
| **Subject** | Educational Data Mining and Learning Analytics |
| **Practical Number** | 01 |
| **Practical Title** | Exploratory Data Analysis of Student Performance |
| **Date** | November 2026 |

---

## 1. AIM

To perform a comprehensive Exploratory Data Analysis (EDA) on the UCI Student Performance dataset (`student-mat.csv`) in order to:

1. Inspect and understand the structure, attributes, and quality of the dataset.
2. Calculate descriptive statistics (mean, median, mode, variance, standard deviation, quartiles, skewness, and kurtosis) for key academic variables.
3. Visualize grade distributions using histograms, box plots, scatter plots, and violin plots.
4. Explore relationships between variables using correlation analysis and heatmaps.
5. Identify and analyse outliers using the Interquartile Range (IQR) method.
6. Demonstrate neural network simulation using TensorFlow Playground.
7. Optionally, train an MLP classifier to predict student pass/fail outcomes and evaluate its performance using standard classification metrics.

---

## 2. APPARATUS / TOOLS REQUIRED

| Category | Details |
|---|---|
| **Operating System** | macOS |
| **Programming Language** | Python 3.x |
| **IDE / Environment** | Google Colab / Jupyter Notebook / Terminal |
| **Primary Platform** | TensorFlow Playground (https://playground.tensorflow.org/) |
| **Dataset** | UCI Student Performance Dataset – Mathematics (`student-mat.csv`) |
| **Dataset Source** | https://archive.ics.uci.edu/dataset/320/student+performance |
| **Libraries** | `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn` |
| **Visualization** | Matplotlib 3.11, Seaborn 0.13 |
| **ML Framework** | scikit-learn 1.9 (`MLPClassifier`) |
| **Document Tools** | Markdown, Python `nbformat` |

---

## 3. THEORY

### 3.1 Exploratory Data Analysis (EDA)

Exploratory Data Analysis is a systematic approach to analysing datasets using statistical summaries and graphical representations before applying formal modelling. Coined by John Tukey (1977), EDA helps analysts understand data distributions, detect anomalies, discover patterns, and formulate hypotheses.

In Educational Data Mining (EDM), EDA is the foundational step that reveals:
- Academic performance distributions
- Relationships between socio-demographic factors and grades
- Anomalies (dropouts, exceptional performers)
- Data quality issues (missing values, inconsistencies)

### 3.2 Descriptive Statistics

**Measures of Central Tendency:**

- **Mean (Arithmetic Average):**

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

where $\bar{x}$ is the mean, $n$ is the number of observations, and $x_i$ is the $i$-th observation.

- **Median:** The middle value when data is sorted in ascending order. For $n$ observations:
  - If $n$ is odd: Median = $x_{(n+1)/2}$
  - If $n$ is even: Median = $\frac{x_{n/2} + x_{n/2+1}}{2}$

- **Mode:** The most frequently occurring value in the dataset.

**Measures of Dispersion:**

- **Variance:**

$$\sigma^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

where $\sigma^2$ is the sample variance.

- **Standard Deviation:**

$$\sigma = \sqrt{\sigma^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

- **Range:** $R = x_{\max} - x_{\min}$

- **Interquartile Range (IQR):** $\text{IQR} = Q_3 - Q_1$, where $Q_1$ and $Q_3$ are the 25th and 75th percentiles.

**Measures of Shape:**

- **Skewness:** Measures asymmetry of the distribution.

$$\text{Skewness} = \frac{n}{(n-1)(n-2)} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{\sigma}\right)^3$$

  - Skewness > 0: Right-skewed (tail extends right)
  - Skewness < 0: Left-skewed (tail extends left)
  - Skewness ≈ 0: Approximately symmetric

- **Kurtosis:** Measures the "tailedness" of the distribution (excess kurtosis, relative to normal distribution).

$$\text{Kurtosis} = \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{\sigma}\right)^4 - \frac{3(n-1)^2}{(n-2)(n-3)}$$

### 3.3 Correlation Analysis

**Pearson Correlation Coefficient** measures the linear relationship between two continuous variables:

$$r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \cdot \sum_{i=1}^{n} (y_i - \bar{y})^2}}$$

- $r = +1$: Perfect positive linear correlation
- $r = -1$: Perfect negative linear correlation
- $r = 0$: No linear correlation
- $|r| > 0.7$: Strong correlation
- $0.3 < |r| < 0.7$: Moderate correlation
- $|r| < 0.3$: Weak correlation

### 3.4 Outlier Detection – IQR Method

An outlier is an observation that falls significantly outside the range of other observations. The IQR method identifies outliers as follows:

1. Calculate $Q_1$ (25th percentile) and $Q_3$ (75th percentile)
2. Compute $\text{IQR} = Q_3 - Q_1$
3. Define bounds:
   - Lower Bound = $Q_1 - 1.5 \times \text{IQR}$
   - Upper Bound = $Q_3 + 1.5 \times \text{IQR}$
4. Any observation below the lower bound or above the upper bound is classified as an outlier.

### 3.5 Data Visualization Techniques

| Technique | Purpose |
|---|---|
| **Histogram** | Shows frequency distribution of a single continuous variable |
| **Box Plot** | Displays median, quartiles, range, and outliers |
| **Scatter Plot** | Shows relationship between two continuous variables |
| **Violin Plot** | Combines box plot with kernel density estimation |
| **Heatmap** | Colour-coded matrix for visualizing correlations |
| **Pair Plot** | Grid of scatter plots and distributions for multiple variables |

### 3.6 Multi-Layer Perceptron (MLP) Neural Network

The MLP classifier used in Section G (optional extension) is a feedforward artificial neural network. It is relevant here because it performs the pass/fail classification task on the real student dataset.

**Architecture (as implemented):**
- **Input layer:** 30 features (13 numerical + 17 encoded categorical)
- **Hidden layer 1:** 64 neurons, ReLU activation
- **Hidden layer 2:** 32 neurons, ReLU activation
- **Output layer:** 1 neuron, sigmoid/logistic activation (binary classification)

**ReLU Activation Function:**

$$f(x) = \max(0, x)$$

**Cross-Entropy Loss (Binary):**

$$\mathcal{L} = -\frac{1}{n} \sum_{i=1}^{n} [y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]$$

where $y_i$ is the true label and $\hat{y}_i$ is the predicted probability.

**Adam Optimizer** adaptively adjusts learning rates using first and second moment estimates of the gradients.

### 3.7 Classification Metrics

Since a classification model is implemented in the optional extension, the following metrics are relevant:

- **True Positive (TP):** Correctly predicted as Pass
- **True Negative (TN):** Correctly predicted as Fail
- **False Positive (FP):** Predicted Pass but actually Fail
- **False Negative (FN):** Predicted Fail but actually Pass

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

$$\text{Precision} = \frac{TP}{TP + FP}$$

$$\text{Recall (Sensitivity)} = \frac{TP}{TP + FN}$$

$$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

### 3.8 TensorFlow Playground – Neural Network Simulator

TensorFlow Playground is an interactive web-based visualization tool that demonstrates how neural networks work. It provides:
- **Built-in synthetic datasets:** Circle, Exclusive OR (XOR), Gaussian, Spiral
- **Configurable parameters:** Hidden layers (1–6), neurons per layer (1–8), activation functions (ReLU, Tanh, Sigmoid, Linear), learning rate, regularization, noise level, batch size, train/test ratio
- **Input features:** $X_1$, $X_2$, $X_1^2$, $X_2^2$, $X_1 X_2$, $\sin(X_1)$, $\sin(X_2)$
- **Real-time visualization:** Decision boundary, neuron weights, training/test loss

> **Important Note:** TensorFlow Playground uses its own built-in synthetic 2D datasets for demonstration. These are **not** related to the UCI Student Performance dataset. The Playground is used here solely to demonstrate neural network concepts (architecture, training, decision boundaries) in a visual and interactive manner.

---

## 4. METHODOLOGY / PROCEDURE

### Part I: EDA on UCI Student Performance Dataset (Python)

1. **Environment Setup:** Install Python libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `scikit-learn`).
2. **Dataset Acquisition:** Download the UCI Student Performance dataset from https://archive.ics.uci.edu/dataset/320/student+performance. Extract `student-mat.csv` (Mathematics course, 395 records, 33 attributes).
3. **Dataset Loading:** Read the CSV file using `pandas.read_csv()` with semicolon (`;`) separator.
4. **Data Inspection:**
   - Display first and last 5 records using `df.head()` and `df.tail()`.
   - Check dimensions using `df.shape`.
   - Examine data types using `df.dtypes`.
   - Identify numerical and categorical columns.
   - Check for missing values using `df.isnull().sum()`.
   - Check for duplicate rows using `df.duplicated().sum()`.
5. **Descriptive Statistics:**
   - Use `df.describe()` for summary statistics.
   - Calculate mean, median, mode, variance, standard deviation, quartiles, IQR, skewness, and kurtosis for key variables (`studytime`, `failures`, `absences`, `G1`, `G2`, `G3`).
6. **Visualization:**
   - Plot histogram of G3 with mean and median lines.
   - Plot box plot of G3 with annotated quartiles.
   - Plot box plots for all key variables.
   - Plot bar chart and violin plot for studytime vs G3.
   - Plot scatter plot of G1 vs G3 with trend line and Pearson correlation.
   - Plot scatter plot of G2 vs G3.
   - Calculate full correlation matrix and plot heatmap.
   - Plot grade comparison (G1, G2, G3 overlaid histograms).
   - Generate pair plot of key variables.
7. **Outlier Detection:**
   - For each key variable, calculate Q1, Q3, IQR, lower and upper bounds.
   - Identify and count outliers.
   - Visualize outliers with scatter plots showing IQR bounds.
8. **Save all outputs** (figures as PNG, statistics as CSV).

### Part II: Neural Network Simulation (TensorFlow Playground)

9. Open https://playground.tensorflow.org/ in a web browser.
10. **Experiment 1 – Circle Dataset:**
    - Select the Circle dataset (concentric circles).
    - Set noise ≈ 10–15, train/test ratio = 50%.
    - Configure 2 hidden layers with 4 neurons each.
    - Set activation = ReLU, learning rate = 0.03.
    - Select input features: $X_1$ and $X_2$.
    - Click the Play button and train for 200+ epochs.
    - Observe the decision boundary, training loss, and test loss.
    - Capture a screenshot.
11. **Experiment 2 – Spiral Dataset:**
    - Select the Spiral dataset.
    - Use 3 hidden layers (6, 4, 2 neurons).
    - Set activation = Tanh.
    - Add all input features ($X_1$, $X_2$, $X_1^2$, $X_2^2$, $X_1 X_2$, $\sin(X_1)$, $\sin(X_2)$).
    - Train for 400+ epochs.
    - Capture a screenshot.

### Part III: Optional ML Extension (MLP Classifier)

12. Create a binary target: Pass (G3 ≥ 10) / Fail (G3 < 10).
13. **Prevent target leakage:** Exclude G1 and G2 from features (they are intermediate grades highly correlated with G3).
14. Encode categorical features using `LabelEncoder`.
15. Split data 80/20 (stratified) for training and testing.
16. **Scale features** using `StandardScaler` fitted on training data only.
17. Train an MLP classifier with architecture (64, 32), ReLU activation, Adam optimizer.
18. Evaluate using accuracy, precision, recall, F1-score, and confusion matrix.
19. Plot training loss curve and feature importance.

---

## 5. ALGORITHM / ARCHITECTURE / WORKFLOW

### 5.1 EDA Workflow

```
┌─────────────────────┐
│  Dataset Acquisition │
│  (UCI Repository)    │
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  Data Loading        │
│  (pandas read_csv)   │
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  Data Inspection     │
│  - Shape, dtypes     │
│  - Head/Tail         │
│  - Missing values    │
│  - Duplicates        │
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  Descriptive Stats   │
│  - Mean, Median, Mode│
│  - Var, Std, IQR     │
│  - Skewness, Kurtosis│
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  Visualization       │
│  - Histograms        │
│  - Box plots         │
│  - Scatter plots     │
│  - Correlation map   │
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  Outlier Detection   │
│  (IQR Method)        │
└─────────┬───────────┘
          ▼
┌─────────────────────┐
│  Interpretation &    │
│  Reporting           │
└─────────────────────┘
```

### 5.2 EDA Pseudocode

```
ALGORITHM: Exploratory Data Analysis of Student Performance

INPUT: student-mat.csv (395 records × 33 attributes)
OUTPUT: Statistics, visualizations, outlier analysis

1. LOAD dataset with separator = ';'
2. DISPLAY shape, first 5 rows, last 5 rows
3. IDENTIFY numerical_columns, categorical_columns
4. CHECK missing_values ← sum of null values per column
5. CHECK duplicates ← count of duplicate rows
6. FOR EACH column IN [studytime, failures, absences, G1, G2, G3]:
       COMPUTE mean, median, mode
       COMPUTE variance, std_deviation
       COMPUTE min, max, range
       COMPUTE Q1, Q2, Q3, IQR
       COMPUTE skewness, kurtosis
       PRINT statistics
7. PLOT histogram of G3 with mean and median lines
8. PLOT box plot of G3 with annotated quartiles
9. PLOT scatter(G1, G3) with trend line
   COMPUTE Pearson_r(G1, G3)
10. COMPUTE correlation_matrix for all numerical columns
    PLOT heatmap of correlation_matrix
11. FOR EACH column IN [absences, G1, G2, G3, failures, age, studytime]:
       Q1 ← 25th percentile
       Q3 ← 75th percentile
       IQR ← Q3 - Q1
       lower ← Q1 - 1.5 × IQR
       upper ← Q3 + 1.5 × IQR
       outliers ← rows WHERE value < lower OR value > upper
       REPORT count(outliers), percentage
12. SAVE all figures and statistics
```

### 5.3 MLP Classifier Architecture

```
Input Layer          Hidden Layer 1       Hidden Layer 2       Output Layer
(30 features)        (64 neurons)         (32 neurons)         (1 neuron)
                     ReLU                 ReLU                 Sigmoid
  ┌───┐             ┌───┐               ┌───┐               ┌───┐
  │ x₁│────────────▶│ h₁│──────────────▶│ h₁│──────────────▶│   │
  │ x₂│             │ h₂│               │ h₂│               │ ŷ │
  │ . │             │ . │               │ . │               │   │
  │ . │             │ . │               │ . │               └───┘
  │x₃₀│             │h₆₄│               │h₃₂│         Pass(1)/Fail(0)
  └───┘             └───┘               └───┘
```

### 5.4 TensorFlow Playground Configuration

**Experiment 1 (Circle):**
| Parameter | Value |
|---|---|
| Dataset | Circle (concentric) |
| Problem Type | Classification |
| Input Features | X₁, X₂ |
| Hidden Layers | 2 |
| Neurons per Layer | 4, 4 |
| Activation | ReLU |
| Learning Rate | 0.03 |
| Noise | ~10–15 |
| Train/Test Ratio | 50% |
| Target Epochs | 200+ |

**Experiment 2 (Spiral):**
| Parameter | Value |
|---|---|
| Dataset | Spiral |
| Problem Type | Classification |
| Input Features | X₁, X₂, X₁², X₂², X₁X₂, sin(X₁), sin(X₂) |
| Hidden Layers | 3 |
| Neurons per Layer | 6, 4, 2 |
| Activation | Tanh |
| Learning Rate | 0.03 |
| Noise | ~0 |
| Train/Test Ratio | 50% |
| Target Epochs | 400+ |

---

## 6. PROGRAM / IMPLEMENTATION

### 6.1 Complete Python Implementation

The following code was executed using Python 3.x. The complete script is available at: `code/practical01_eda.py`

```python
#!/usr/bin/env python3
"""
CET3001 – Educational Data Mining and Learning Analytics
Practical 01: Exploratory Data Analysis of Student Performance
Student: SHRIYASH SAHU | Reg No: 24BET10001
"""

import os, warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ── Configuration ──
DATA_PATH = '../data/student-mat.csv'
OUTPUT_DIR = '../outputs'
os.makedirs(OUTPUT_DIR, exist_ok=True)
sns.set_theme(style='whitegrid', palette='Set2', font_scale=1.1)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.bbox'] = 'tight'
```

**Explanation:** Import all required libraries. Set Matplotlib to non-interactive (`Agg`) backend for headless execution. Configure Seaborn theme for consistent, professional plots.

```python
# ═══════════════════════════════════════════════
# SECTION A: DATASET LOADING AND INSPECTION
# ═══════════════════════════════════════════════
df = pd.read_csv(DATA_PATH, sep=';')
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(df.head())     # First 5 records
print(df.tail())     # Last 5 records
print(df.dtypes)     # Column data types

num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
print(f"Numerical columns ({len(num_cols)}): {num_cols}")
print(f"Categorical columns ({len(cat_cols)}): {cat_cols}")

# Check data quality
print(f"Total missing values: {df.isnull().sum().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")
```

**Explanation:** Load the dataset with semicolon separator. The dataset contains 395 records and 33 attributes. Split columns into numerical (16) and categorical (17). Data quality checks confirm zero missing values and zero duplicates.

```python
# ═══════════════════════════════════════════════
# SECTION C: DESCRIPTIVE STATISTICS
# ═══════════════════════════════════════════════
focus_cols = ['studytime', 'failures', 'absences', 'G1', 'G2', 'G3']

desc_all = df[num_cols].describe().T
desc_all['median'] = df[num_cols].median()
desc_all['mode'] = df[num_cols].mode().iloc[0]
desc_all['variance'] = df[num_cols].var()
desc_all['skewness'] = df[num_cols].skew()
desc_all['kurtosis'] = df[num_cols].kurtosis()
desc_all['IQR'] = desc_all['75%'] - desc_all['25%']
print(desc_all)

# Detailed per-variable statistics
for col in focus_cols:
    data = df[col]
    print(f"\n{col}:")
    print(f"  Mean={data.mean():.4f}, Median={data.median():.4f}, "
          f"Mode={data.mode().iloc[0]}")
    print(f"  Var={data.var():.4f}, StdDev={data.std():.4f}")
    print(f"  Min={data.min()}, Max={data.max()}, Range={data.max()-data.min()}")
    print(f"  Q1={data.quantile(0.25)}, Q3={data.quantile(0.75)}, "
          f"IQR={data.quantile(0.75)-data.quantile(0.25)}")
    print(f"  Skewness={data.skew():.4f}, Kurtosis={data.kurtosis():.4f}")
```

**Explanation:** Compute comprehensive descriptive statistics for all numerical columns. The `.describe().T` method provides count, mean, std, min, quartiles, and max. Additional measures (median, mode, variance, skewness, kurtosis, IQR) are appended.

```python
# ═══════════════════════════════════════════════
# SECTION D: VISUALIZATIONS
# ═══════════════════════════════════════════════

# D1: Histogram of G3
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['G3'], bins=21, range=(-0.5, 20.5),
        edgecolor='black', color='#4C72B0', alpha=0.85)
ax.set_xlabel('Final Grade (G3)')
ax.set_ylabel('Number of Students')
ax.set_title('Figure 1: Distribution of Final Grades (G3)')
ax.axvline(df['G3'].mean(), color='red', linestyle='--', lw=2,
           label=f"Mean = {df['G3'].mean():.2f}")
ax.axvline(df['G3'].median(), color='green', linestyle='-.', lw=2,
           label=f"Median = {df['G3'].median():.2f}")
ax.legend()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig01_histogram_G3.png'))
```

**Explanation:** 21 bins map to each integer grade (0–20). Mean and median vertical lines help identify distribution shape. The histogram reveals a notable spike at G3 = 0 (dropouts).

```python
# D5: Scatter Plot G1 vs G3 with Trend Line
fig, ax = plt.subplots(figsize=(10, 7))
scatter = ax.scatter(df['G1'], df['G3'], c=df['G2'], cmap='viridis',
                     alpha=0.7, edgecolors='gray', s=60)
plt.colorbar(scatter, ax=ax, label='G2')
z = np.polyfit(df['G1'], df['G3'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['G1'].min(), df['G1'].max(), 100)
ax.plot(x_line, p(x_line), 'r--', lw=2,
        label=f'Trend: G3 = {z[0]:.2f}·G1 + {z[1]:.2f}')
r, pval = stats.pearsonr(df['G1'], df['G3'])
ax.set_title(f'Figure 5: G1 vs G3 (r = {r:.3f}, p < 0.001)')
ax.legend()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig05_scatter_G1_vs_G3.png'))
```

**Explanation:** Scatter plot with colour-coded G2 values shows the three-grade relationship. A linear trend line is fitted using `numpy.polyfit`. Pearson correlation coefficient is computed using `scipy.stats.pearsonr`.

```python
# D7: Correlation Heatmap
corr_matrix = df[num_cols].corr()
fig, ax = plt.subplots(figsize=(16, 13))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f',
            cmap='RdBu_r', center=0, square=True, linewidths=0.5,
            ax=ax, annot_kws={'size': 8}, vmin=-1, vmax=1)
ax.set_title('Figure 7: Correlation Heatmap')
plt.savefig(os.path.join(OUTPUT_DIR, 'fig07_correlation_heatmap.png'))
```

**Explanation:** Lower-triangular correlation heatmap using Red-Blue diverging colour map. `annot=True` displays Pearson coefficients. The mask hides the redundant upper triangle.

```python
# ═══════════════════════════════════════════════
# SECTION E: OUTLIER DETECTION (IQR METHOD)
# ═══════════════════════════════════════════════
outlier_cols = ['absences', 'G1', 'G2', 'G3', 'failures', 'age', 'studytime']

for col in outlier_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"{col}: Q1={Q1}, Q3={Q3}, IQR={IQR}, "
          f"Bounds=[{lower:.2f}, {upper:.2f}], Outliers={len(outliers)}")
```

**Explanation:** For each variable, compute quartiles and IQR, then classify values beyond 1.5×IQR from quartiles as outliers. This is the standard Tukey fence method.

```python
# ═══════════════════════════════════════════════
# SECTION G: MLP CLASSIFIER (Optional Extension)
# ═══════════════════════════════════════════════
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Binary target: Pass (G3 >= 10) / Fail (G3 < 10)
df['pass_fail'] = (df['G3'] >= 10).astype(int)

# Exclude G1, G2 to prevent target leakage
feature_cols = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures',
                'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health',
                'absences', 'school', 'sex', 'address', 'famsize', 'Pstatus',
                'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup',
                'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic']

# Encode categoricals
df_ml = df.copy()
for col in df_ml.select_dtypes(include=['object']).columns:
    df_ml[col] = LabelEncoder().fit_transform(df_ml[col])

X = df_ml[feature_cols]
y = df_ml['pass_fail']

# 80-20 stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# Scale using TRAINING data only
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train MLP
mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu',
                    solver='adam', max_iter=500, random_state=42,
                    early_stopping=True, validation_fraction=0.15,
                    n_iter_no_change=20, learning_rate_init=0.001)
mlp.fit(X_train_scaled, y_train)
y_pred = mlp.predict(X_test_scaled)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))
```

**Explanation:** 
- **Target definition:** Portuguese grading system uses 10/20 as passing threshold.
- **Target leakage prevention:** G1 and G2 are excluded because they are intermediate grades that directly predict G3 with r > 0.80, making the prediction trivially easy but practically useless.
- **Scaling:** `StandardScaler` is fitted on training data only; the test data is transformed using the same parameters.
- **Early stopping:** Training halts when validation performance doesn't improve for 20 consecutive iterations.

> The complete, executable source code is in `code/practical01_eda.py` and the Jupyter notebook version is in `code/Practical01_EDA_StudentPerformance.ipynb`.

---

## 7. OUTPUT / SIMULATION

### 7.1 Dataset Inspection Output

**Dataset Dimensions:** 395 rows × 33 columns

**First 5 Records:**

| # | school | sex | age | address | famsize | Medu | Fedu | studytime | failures | absences | G1 | G2 | G3 |
|---|--------|-----|-----|---------|---------|------|------|-----------|----------|----------|----|----|----|
| 0 | GP | F | 18 | U | GT3 | 4 | 4 | 2 | 0 | 6 | 5 | 6 | 6 |
| 1 | GP | F | 17 | U | GT3 | 1 | 1 | 2 | 0 | 4 | 5 | 5 | 6 |
| 2 | GP | F | 15 | U | LE3 | 1 | 1 | 2 | 3 | 10 | 7 | 8 | 10 |
| 3 | GP | F | 15 | U | GT3 | 4 | 2 | 3 | 0 | 2 | 15 | 14 | 15 |
| 4 | GP | F | 16 | U | GT3 | 3 | 3 | 2 | 0 | 4 | 6 | 10 | 10 |

**Data Quality:**
- Missing values: **0**
- Duplicate rows: **0**
- Numerical columns: **16**
- Categorical columns: **17**

**Key Categorical Distributions:**

| Variable | Category | Count |
|---|---|---|
| school | GP (Gabriel Pereira) | 349 |
| school | MS (Mousinho da Silveira) | 46 |
| sex | Female | 208 |
| sex | Male | 187 |
| higher (wants higher education) | Yes | 375 |
| higher | No | 20 |
| internet | Yes | 329 |
| internet | No | 66 |

**Students with G3 = 0 (possible dropouts): 38**

### 7.2 Descriptive Statistics

**Key Variables Summary (Actual Computed Values):**

| Statistic | studytime | failures | absences | G1 | G2 | G3 |
|---|---|---|---|---|---|---|
| **Mean** | 2.0354 | 0.3342 | 5.7089 | 10.9089 | 10.7139 | 10.4152 |
| **Median** | 2.0000 | 0.0000 | 4.0000 | 11.0000 | 11.0000 | 11.0000 |
| **Mode** | 2 | 0 | 0 | 10 | 9 | 10 |
| **Variance** | 0.7043 | 0.5530 | 64.0495 | 11.0171 | 14.1489 | 20.9896 |
| **Std Dev** | 0.8392 | 0.7437 | 8.0031 | 3.3192 | 3.7615 | 4.5814 |
| **Minimum** | 1 | 0 | 0 | 3 | 0 | 0 |
| **Maximum** | 4 | 3 | 75 | 19 | 19 | 20 |
| **Range** | 3 | 3 | 75 | 16 | 19 | 20 |
| **Q1** | 1.0 | 0.0 | 0.0 | 8.0 | 9.0 | 8.0 |
| **Q2 (Median)** | 2.0 | 0.0 | 4.0 | 11.0 | 11.0 | 11.0 |
| **Q3** | 2.0 | 0.0 | 8.0 | 13.0 | 13.0 | 14.0 |
| **IQR** | 1.0 | 0.0 | 8.0 | 5.0 | 4.0 | 6.0 |
| **Skewness** | 0.6321 | 2.3870 | 3.6716 | 0.2406 | −0.4316 | −0.7327 |
| **Kurtosis** | −0.0144 | 5.0047 | 21.7191 | −0.6938 | 0.6277 | 0.4034 |

### 7.3 Visualizations

#### Figure 1: Histogram of Final Grades (G3)
![Figure 1: Histogram of G3](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig01_histogram_G3.png)

The histogram shows the distribution of final grades across all 395 students. Notable features include a spike at G3 = 0 (38 students, possible dropouts) and a roughly bell-shaped distribution for the remaining students centred around 10–11.

#### Figure 2: Box Plot of Final Grades (G3)
![Figure 2: Box Plot of G3](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig02_boxplot_G3.png)

The box plot displays Q1 = 8, Median = 11, Q3 = 14 with IQR = 6. No outliers are detected by the IQR method for G3, as the full 0–20 range falls within the whiskers.

#### Figure 3: Box Plots of Key Variables
![Figure 3: Box Plots](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig03_boxplots_key_vars.png)

Box plots for `studytime`, `failures`, `absences`, `G1`, `G2`, and `G3`. The `absences` variable shows the most extreme outliers (up to 75), while `failures` has a highly concentrated distribution at 0.

#### Figure 4: Study Time vs Final Grade (G3)
![Figure 4: Study Time vs G3](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig04_studytime_vs_G3.png)

Left: Mean G3 by study time category. Right: Violin plot showing full grade distributions per study time group. Students with longer study times tend to have slightly higher average grades, but the effect is modest.

#### Figure 5: Scatter Plot – G1 vs G3
![Figure 5: G1 vs G3](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig05_scatter_G1_vs_G3.png)

Strong positive correlation (r = 0.801, p < 0.001). First period grades are a strong predictor of final grades. The colour encoding by G2 reveals a consistent progression across all three grading periods.

#### Figure 6: Scatter Plot – G2 vs G3
![Figure 6: G2 vs G3](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig06_scatter_G2_vs_G3.png)

Very strong positive correlation (r = 0.905, p < 0.001). G2 is the single strongest predictor of G3, confirming that second-period performance closely tracks final outcomes.

#### Figure 7: Correlation Heatmap
![Figure 7: Correlation Heatmap](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig07_correlation_heatmap.png)

Lower-triangular heatmap showing Pearson correlations between all 16 numerical variables. Key observations: G1–G2 (0.85), G2–G3 (0.90), G1–G3 (0.80) form a strongly correlated grade cluster. `failures` has the strongest negative correlation with G3 (−0.36). `Dalc`–`Walc` correlation (0.65) reflects consistent alcohol consumption patterns.

#### Figure 8: Outlier Detection (IQR Method)
![Figure 8: Outlier Detection](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig08_outlier_detection.png)

Scatter plots with IQR bounds for seven key variables. Red points indicate outliers. `absences` (15 outliers, 3.8%) and `failures` (83 outliers, 21.0%) have the most significant outlier presence.

#### Figure 9: Grade Distribution Comparison (G1, G2, G3)
![Figure 9: Grade Comparison](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig09_grade_comparison.png)

#### Figure 10: Pair Plot of Key Variables
![Figure 10: Pair Plot](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig10_pairplot.png)

#### Figure 11: Final Grade Distribution by Gender
![Figure 11: Gender Grades](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig11_gender_grades.png)

### 7.4 Correlations with Final Grade (G3)

| Variable | Correlation with G3 | Strength |
|---|---|---|
| G2 | +0.905 | Very Strong Positive |
| G1 | +0.801 | Strong Positive |
| Medu | +0.217 | Weak Positive |
| Fedu | +0.152 | Weak Positive |
| studytime | +0.098 | Very Weak Positive |
| famrel | +0.051 | Negligible |
| absences | +0.034 | Negligible |
| freetime | +0.011 | Negligible |
| Walc | −0.052 | Negligible |
| Dalc | −0.055 | Negligible |
| health | −0.061 | Negligible |
| traveltime | −0.117 | Weak Negative |
| goout | −0.133 | Weak Negative |
| age | −0.162 | Weak Negative |
| **failures** | **−0.360** | **Moderate Negative** |

### 7.5 Outlier Detection Results

| Variable | Q1 | Q3 | IQR | Lower Bound | Upper Bound | Outlier Count | Outlier % |
|---|---|---|---|---|---|---|---|
| absences | 0.0 | 8.0 | 8.0 | −12.0 | 20.0 | 15 | 3.8% |
| G1 | 8.0 | 13.0 | 5.0 | 0.5 | 20.5 | 0 | 0.0% |
| G2 | 9.0 | 13.0 | 4.0 | 3.0 | 19.0 | 13 | 3.3% |
| G3 | 8.0 | 14.0 | 6.0 | −1.0 | 23.0 | 0 | 0.0% |
| failures | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 83 | 21.0% |
| age | 16.0 | 18.0 | 2.0 | 13.0 | 21.0 | 1 | 0.3% |
| studytime | 1.0 | 2.0 | 1.0 | −0.5 | 3.5 | 27 | 6.8% |

**Notable outlier values in `absences`:** 21, 22, 22, 22, 23, 24, 25, 26, 28, 30, 38, 40, 54, 56, 75

**G2 outliers:** All 13 outliers have G2 = 0, indicating students who likely dropped out or did not take the second period exam.

### 7.6 TensorFlow Playground Simulation

The TensorFlow Playground web platform (https://playground.tensorflow.org/) was inspected and simulated using Google Chrome. Below are the verified platform inspection findings and the results of two live neural network training experiments.

#### 7.6.1 Platform Capabilities & Built-in Model Options
- **Available Datasets (Classification):** Circle (concentric rings), Exclusive OR (XOR), Gaussian clusters, Spiral.
- **Available Datasets (Regression):** Plane, Multi-Gaussian.
- **Input Feature Transformations:** $X_1$, $X_2$, $X_1^2$, $X_2^2$, $X_1 X_2$, $\sin(X_1)$, $\sin(X_2)$.
- **Activation Functions:** ReLU, Tanh, Sigmoid, Linear.
- **Regularization Types:** None, L1, L2 (with rates from 0 to 10).
- **Learning Rates:** 0.00001 to 10 (default: 0.03).
- **Hidden Layers:** Configurable from 0 up to 6 hidden layers; 1 to 8 neurons per layer.
- **Problem Types:** Classification, Regression.

#### Figure 15: TensorFlow Playground – Default Interface
![Figure 15: Default Playground Interface](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/screenshots/tf_playground_default.png)

---

#### 7.6.2 Experiment 1: Circle Dataset (Non-linear Classification with ReLU)

**Configuration:**
- **Dataset:** Circle (two concentric classes)
- **Features:** $X_1, X_2$ (raw 2D coordinates)
- **Hidden Layers:** 2 layers (Layer 1: 4 neurons, Layer 2: 4 neurons)
- **Activation:** ReLU
- **Learning Rate:** 0.03
- **Regularization:** None
- **Batch Size:** 10
- **Noise:** 15
- **Ratio of training to test data:** 50%

**Observed Training Dynamics & Execution Output:**
- **Epoch Count Reached:** 302 epochs
- **Final Training Loss:** 0.001
- **Final Test Loss:** 0.002
- **Decision Boundary Formation:** Initially at epoch 62, the training loss was 0.035 and test loss was 0.033 with an approximate polygonal boundary. By epoch 182, the loss dropped to 0.003 / 0.004. By epoch 302, the network formed a distinct circular decision boundary encapsulating the inner cluster, demonstrating that piecewise linear ReLU activations combine across two hidden layers to construct a closed non-linear convex region.

#### Figure 16: TensorFlow Playground – Circle Dataset (Trained Model)
![Figure 16: Circle Dataset Trained](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/screenshots/tf_playground_circle_trained.png)

---

#### 7.6.3 Experiment 2: Spiral Dataset (Complex Manifold with Tanh & Engineered Features)

**Configuration:**
- **Dataset:** Spiral (interleaved non-linear spiral arms)
- **Features:** All 7 input features ($X_1, X_2, X_1^2, X_2^2, X_1 X_2, \sin(X_1), \sin(X_2)$)
- **Hidden Layers:** 3 layers (Layer 1: 6 neurons, Layer 2: 4 neurons, Layer 3: 2 neurons)
- **Activation:** Tanh
- **Learning Rate:** 0.03
- **Regularization:** None
- **Batch Size:** 10
- **Noise:** 0
- **Ratio of training to test data:** 50%

**Observed Training Dynamics & Execution Output:**
- **Epoch Count Reached:** 484 epochs
- **Final Training Loss:** 0.001
- **Final Test Loss:** 0.002
- **Decision Boundary Formation:** The spiral problem is notorious for having intricate topological curvature. By utilizing sinusoidal and polynomial feature transformations alongside a 3-layer architecture with smooth Tanh activations, the network learns smooth interlocking decision bands that follow the spiral curvature accurately, achieving test loss of 0.002.

#### Figure 17: TensorFlow Playground – Spiral Dataset (Trained Model)
![Figure 17: Spiral Dataset Trained](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/screenshots/tf_playground_spiral_trained.png)

### 7.7 MLP Classifier Results (Optional Extension)

**Pass/Fail Distribution:**
| Class | Count | Percentage |
|---|---|---|
| Pass (G3 ≥ 10) | 265 | 67.1% |
| Fail (G3 < 10) | 130 | 32.9% |

**Train/Test Split:** 316 training samples / 79 test samples (80/20 stratified)

**Classification Results:**

| Metric | Fail | Pass | Weighted Avg |
|---|---|---|---|
| **Precision** | 0.38 | 0.68 | 0.58 |
| **Recall** | 0.12 | 0.91 | 0.65 |
| **F1-Score** | 0.18 | 0.77 | 0.58 |
| **Support** | 26 | 53 | 79 |

**Overall Accuracy: 0.6456 (64.56%)**

**Confusion Matrix:**

|  | Predicted Fail | Predicted Pass |
|---|---|---|
| **Actual Fail** | TN = 3 | FP = 23 |
| **Actual Pass** | FN = 5 | TP = 48 |

**Computed Metrics (for Pass class):**
- Precision = TP/(TP+FP) = 48/(48+23) = **0.6761**
- Recall = TP/(TP+FN) = 48/(48+5) = **0.9057**
- F1-Score = 2×(0.6761×0.9057)/(0.6761+0.9057) = **0.7742**

#### Figure 12: Confusion Matrix
![Figure 12: Confusion Matrix](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig12_confusion_matrix.png)

#### Figure 13: MLP Training Loss Curve
![Figure 13: Training Loss](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig13_training_loss.png)

#### Figure 14: Feature Importance (Permutation)
![Figure 14: Feature Importance](file:///Users/shriyashsahu/Documents/Edu.Datamining/Practical01/outputs/fig14_feature_importance.png)

---

## 8. RESULTS AND INTERPRETATION

### 8.1 Dataset Characteristics

The UCI Student Performance dataset for the Mathematics course contains **395 student records** with **33 attributes** covering demographics, family background, school-related factors, lifestyle habits, and three grading periods (G1, G2, G3). The dataset is clean with **zero missing values** and **zero duplicate records**, making it suitable for direct analysis without imputation.

### 8.2 Statistical Findings

1. **Final Grade (G3)** has a mean of **10.42** and standard deviation of **4.58** on the 0–20 scale. The negative skewness (−0.73) indicates a slight left skew, pulled by the 38 students who scored zero (likely dropouts).

2. **Absences** is the most dispersed variable with variance = 64.05, range = 75, and extreme positive skewness (3.67) and kurtosis (21.72), indicating a heavily right-tailed distribution. Most students have few absences, but some have exceptionally many.

3. **Failures** shows extreme concentration at zero (mode = 0, median = 0), with 66.6% of students having no past failures. The IQR is 0, which means the IQR method flags any non-zero failure count as an "outlier" — a statistical artifact rather than a true anomaly.

4. **Study time** has modest variation (mean = 2.04, std = 0.84) with most students studying 2–5 hours per week. The correlation with G3 is weak (r = 0.098), suggesting study time alone is not a strong predictor.

### 8.3 Correlation Insights

- **G2 → G3** (r = 0.905) and **G1 → G3** (r = 0.801) are the strongest predictors of final grades, confirming that prior academic performance is the best indicator of final outcomes. This is expected but highlights the temporal consistency of student performance.
- **Failures → G3** (r = −0.360) is the strongest negative correlation among non-grade variables, indicating that students with past class failures tend to perform significantly worse.
- **Mother's education (Medu → G3, r = 0.217)** has a stronger positive relationship than father's education (Fedu, r = 0.152), suggesting parental education, particularly maternal, may influence student outcomes.
- **Social and lifestyle factors** (going out, alcohol consumption) show weak negative correlations with grades, indicating a mild but consistent association.

### 8.4 Outlier Analysis

- **Absences:** 15 outliers (3.8%) with values ranging from 21 to 75. These represent students with unusually high absenteeism. **Recommendation: Retain** — these are genuine data points representing students who may need academic intervention. Removing them would bias the analysis.
- **G2:** 13 outliers (3.3%), all with G2 = 0. These likely represent students who dropped out before the second period. **Recommendation: Flag but retain** — they carry important information about student dropout patterns.
- **Failures:** 83 "outliers" (21.0%) are a statistical artifact. The IQR = 0 makes any non-zero value technically outside the bounds. **Recommendation: Do not treat as outliers** — having 1–3 past failures is a meaningful characteristic, not an anomaly.
- **Age:** Only 1 outlier (age = 22). **Recommendation: Retain** — an unusual but valid data point.

### 8.5 MLP Classifier Interpretation

The MLP classifier achieved **64.6% accuracy** for pass/fail prediction. Key observations:

1. **Moderate accuracy** is expected because G1 and G2 were intentionally excluded to prevent target leakage. Without these strong predictors, the model must rely on weaker socio-demographic and behavioural features.
2. **High recall for Pass (91%)** but very low recall for Fail (12%) indicates the model is biased toward predicting Pass, partly due to class imbalance (67% Pass vs 33% Fail).
3. The model correctly identifies most passing students but struggles to identify at-risk students — the more educationally important task.
4. **Feature importance** analysis (permutation importance) can reveal which socio-demographic factors contribute most to the model's predictions.

**Educational Significance:** An accuracy of ~65% using only background features demonstrates that while socio-demographic factors carry some predictive signal, they are insufficient for reliable early warning systems without incorporating intermediate academic performance data.

### 8.6 TensorFlow Playground Insights

TensorFlow Playground demonstrates neural network fundamentals through interactive visualisation:

1. **Circle dataset** (simpler): A 2-layer, 4-neuron network with ReLU activation can learn a circular decision boundary within ~200 epochs, illustrating how hidden layers enable non-linear classification that a single perceptron cannot achieve.

2. **Spiral dataset** (harder): Requires more capacity (3+ layers, more neurons, additional engineered features like $X_1^2$, $\sin(X_1)$) and more training epochs. This demonstrates why deeper networks and feature engineering are essential for complex decision boundaries.

> **Important distinction:** The TensorFlow Playground datasets are **synthetic 2D patterns** (circles, spirals) used for pedagogical demonstration of neural network concepts. They are **not related to** the UCI Student Performance data, which is a 33-attribute real-world dataset analysed separately using Python.

### 8.7 Limitations

1. **Small dataset:** 395 records is relatively small for ML, limiting model generalisation.
2. **Class imbalance:** 67/33 pass/fail split affects classifier performance, particularly recall for the minority (Fail) class.
3. **Single school system:** The data comes from two Portuguese schools and may not generalise to other educational contexts.
4. **Synthetic Nature of Simulation:** TensorFlow Playground operates exclusively on 2D synthetic datasets (Circle, Spiral), which serve an illustrative role for neural dynamics rather than modeling multi-dimensional tabular student records.
5. **Feature encoding:** Simple label encoding was used for categorical variables; more sophisticated encoding (one-hot) might improve MLP performance.
6. **No temporal analysis:** The dataset represents a single academic year and does not capture longitudinal trends.

### 8.8 Conclusion

This practical successfully demonstrated comprehensive Exploratory Data Analysis on the UCI Student Performance dataset. Key findings include:

- Student final grades (G3) are most strongly predicted by prior period grades (G2, G1) and negatively associated with past failures.
- The dataset is clean but exhibits significant outliers in absences and G2 (dropout indicators).
- Socio-demographic features alone provide moderate (64.6%) predictive power for pass/fail classification.
- TensorFlow Playground effectively demonstrates how neural networks learn non-linear decision boundaries, complementing the theoretical understanding applied in the MLP classifier.

These insights provide actionable value for educational institutions: intermediate assessment scores are the most reliable early-warning indicators, and students with past failures and high absenteeism require targeted support interventions.

---

## 9. REFERENCES

1. Cortez, P., & Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance. In *Proceedings of the 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008)*, pp. 5–12, Porto, Portugal. EUROSIS.

2. UCI Machine Learning Repository – Student Performance Dataset:  
   https://archive.ics.uci.edu/dataset/320/student+performance

3. TensorFlow Playground:  
   https://playground.tensorflow.org/

4. pandas Documentation:  
   https://pandas.pydata.org/docs/

5. scikit-learn Documentation – MLPClassifier:  
   https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html

6. Seaborn Documentation:  
   https://seaborn.pydata.org/

7. Matplotlib Documentation:  
   https://matplotlib.org/stable/contents.html

8. SciPy Documentation – scipy.stats:  
   https://docs.scipy.org/doc/scipy/reference/stats.html

9. Tukey, J. W. (1977). *Exploratory Data Analysis*. Addison-Wesley.

---

*Report prepared by SHRIYASH SAHU (24BET10001) for CET3001 – Educational Data Mining and Learning Analytics, November 2026.*
