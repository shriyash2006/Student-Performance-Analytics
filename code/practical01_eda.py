#!/usr/bin/env python3
"""
CET3001 – Educational Data Mining and Learning Analytics
Practical 01: Exploratory Data Analysis of Student Performance
Student: SHRIYASH SAHU | Reg No: 24BET10001

This script performs complete EDA on the UCI Student Performance dataset (student-mat.csv).
"""

import os
import sys
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for saving figures
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ── Configuration ──────────────────────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'student-mat.csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style='whitegrid', palette='Set2', font_scale=1.1)
plt.rcParams['figure.dpi'] = 150
plt.rcParams['savefig.bbox'] = 'tight'

# ══════════════════════════════════════════════════════════════════════════════
# SECTION A: DATASET LOADING AND INSPECTION
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 80)
print("SECTION A: DATASET LOADING AND INSPECTION")
print("=" * 80)

df = pd.read_csv(DATA_PATH, sep=';')
print(f"\nDataset loaded successfully from: {os.path.abspath(DATA_PATH)}")
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# ── A1: First 5 records ──
print("\n── First 5 Records ──")
print(df.head().to_string())

# ── A2: Last 5 records ──
print("\n── Last 5 Records ──")
print(df.tail().to_string())

# ── A3: Dataset dimensions ──
print(f"\n── Dataset Dimensions ──")
print(f"Number of records (rows): {df.shape[0]}")
print(f"Number of attributes (columns): {df.shape[1]}")

# ── A4: Column names and data types ──
print("\n── Column Names and Data Types ──")
print(df.dtypes.to_string())

# ── A5: Numerical and categorical columns ──
num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df.select_dtypes(include=['object']).columns.tolist()
print(f"\nNumerical columns ({len(num_cols)}): {num_cols}")
print(f"Categorical columns ({len(cat_cols)}): {cat_cols}")

# ── A6: Missing values ──
print("\n── Missing Values ──")
missing = df.isnull().sum()
print(f"Total missing values: {missing.sum()}")
if missing.sum() > 0:
    print(missing[missing > 0])
else:
    print("No missing values found in any column.")

# ── A7: Duplicate records ──
dup_count = df.duplicated().sum()
print(f"\n── Duplicate Records ──")
print(f"Number of duplicate rows: {dup_count}")

# ── A8: Basic info ──
print("\n── Dataset Info ──")
df.info()

# ══════════════════════════════════════════════════════════════════════════════
# SECTION B: DATA INSPECTION – DETAILED VIEW
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("SECTION B: DATA INSPECTION – DETAILED VIEW")
print("=" * 80)

# Value counts for key categorical columns
for col in ['school', 'sex', 'address', 'famsize', 'Pstatus', 'higher', 'internet', 'romantic']:
    print(f"\n── Value Counts: {col} ──")
    print(df[col].value_counts().to_string())

# Target variable G3 distribution summary
print("\n── Target Variable G3 Summary ──")
print(df['G3'].describe())
print(f"Students with G3 = 0 (possible dropouts): {(df['G3'] == 0).sum()}")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION C: DESCRIPTIVE STATISTICS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("SECTION C: DESCRIPTIVE STATISTICS")
print("=" * 80)

# Focus columns
focus_cols = ['studytime', 'failures', 'absences', 'G1', 'G2', 'G3']

# Full descriptive statistics for all numerical columns
print("\n── Descriptive Statistics (All Numerical Columns) ──")
desc_all = df[num_cols].describe().T
desc_all['median'] = df[num_cols].median()
desc_all['mode'] = df[num_cols].mode().iloc[0]
desc_all['variance'] = df[num_cols].var()
desc_all['skewness'] = df[num_cols].skew()
desc_all['kurtosis'] = df[num_cols].kurtosis()
desc_all['IQR'] = desc_all['75%'] - desc_all['25%']
print(desc_all.to_string())

# Detailed stats for focus columns
print("\n── Detailed Statistics for Key Variables ──")
for col in focus_cols:
    data = df[col]
    print(f"\n  {col}:")
    print(f"    Mean             = {data.mean():.4f}")
    print(f"    Median           = {data.median():.4f}")
    print(f"    Mode             = {data.mode().iloc[0]}")
    print(f"    Variance         = {data.var():.4f}")
    print(f"    Std Deviation    = {data.std():.4f}")
    print(f"    Minimum          = {data.min()}")
    print(f"    Maximum          = {data.max()}")
    print(f"    Range            = {data.max() - data.min()}")
    print(f"    Q1 (25th pctile) = {data.quantile(0.25):.4f}")
    print(f"    Q2 (50th pctile) = {data.quantile(0.50):.4f}")
    print(f"    Q3 (75th pctile) = {data.quantile(0.75):.4f}")
    print(f"    IQR              = {data.quantile(0.75) - data.quantile(0.25):.4f}")
    print(f"    Skewness         = {data.skew():.4f}")
    print(f"    Kurtosis         = {data.kurtosis():.4f}")

# Save descriptive stats to CSV
desc_focus = df[focus_cols].describe().T
desc_focus['median'] = df[focus_cols].median()
desc_focus['mode'] = df[focus_cols].mode().iloc[0]
desc_focus['variance'] = df[focus_cols].var()
desc_focus.to_csv(os.path.join(OUTPUT_DIR, 'descriptive_statistics.csv'))
print(f"\nDescriptive statistics saved to: descriptive_statistics.csv")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION D: VISUALIZATIONS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("SECTION D: VISUALIZATIONS")
print("=" * 80)

# ── D1: Histogram of G3 (Final Grade) ──
fig, ax = plt.subplots(figsize=(10, 6))
counts, bins, patches = ax.hist(df['G3'], bins=21, range=(-0.5, 20.5), 
                                 edgecolor='black', color='#4C72B0', alpha=0.85)
ax.set_xlabel('Final Grade (G3)', fontsize=13)
ax.set_ylabel('Number of Students', fontsize=13)
ax.set_title('Figure 1: Distribution of Final Grades (G3) – Mathematics', fontsize=14, fontweight='bold')
ax.set_xticks(range(0, 21))
ax.axvline(df['G3'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean = {df['G3'].mean():.2f}")
ax.axvline(df['G3'].median(), color='green', linestyle='-.', linewidth=2, label=f"Median = {df['G3'].median():.2f}")
ax.legend(fontsize=11)
plt.savefig(os.path.join(OUTPUT_DIR, 'fig01_histogram_G3.png'))
plt.close()
print("Saved: fig01_histogram_G3.png")

# ── D2: Box Plot of G3 ──
fig, ax = plt.subplots(figsize=(10, 5))
bp = ax.boxplot(df['G3'], vert=False, patch_artist=True,
                boxprops=dict(facecolor='#4C72B0', alpha=0.7),
                medianprops=dict(color='red', linewidth=2),
                whiskerprops=dict(linewidth=1.5),
                flierprops=dict(marker='o', markerfacecolor='red', markersize=8, alpha=0.6))
ax.set_xlabel('Final Grade (G3)', fontsize=13)
ax.set_title('Figure 2: Box Plot of Final Grades (G3) – Mathematics', fontsize=14, fontweight='bold')
ax.set_yticks([])
# Annotate Q1, Q2, Q3
q1, q2, q3 = df['G3'].quantile([0.25, 0.50, 0.75])
for val, label in [(q1, f'Q1={q1:.0f}'), (q2, f'Median={q2:.0f}'), (q3, f'Q3={q3:.0f}')]:
    ax.annotate(label, xy=(val, 1), xytext=(val, 1.15),
                fontsize=10, ha='center', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='black'))
plt.savefig(os.path.join(OUTPUT_DIR, 'fig02_boxplot_G3.png'))
plt.close()
print("Saved: fig02_boxplot_G3.png")

# ── D3: Box Plots for Multiple Key Variables ──
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
for idx, col in enumerate(focus_cols):
    ax = axes[idx // 3][idx % 3]
    bp = ax.boxplot(df[col], patch_artist=True,
                    boxprops=dict(facecolor=sns.color_palette('Set2')[idx], alpha=0.7),
                    medianprops=dict(color='red', linewidth=2),
                    flierprops=dict(marker='D', markerfacecolor='red', markersize=6))
    ax.set_title(col, fontsize=13, fontweight='bold')
    ax.set_ylabel('Value')
fig.suptitle('Figure 3: Box Plots of Key Variables', fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig03_boxplots_key_vars.png'))
plt.close()
print("Saved: fig03_boxplots_key_vars.png")

# ── D4: Studytime vs G3 (Bar/Violin) ──
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
# Bar plot of mean G3 by studytime
st_means = df.groupby('studytime')['G3'].mean()
axes[0].bar(st_means.index, st_means.values, color=sns.color_palette('Set2', 4), edgecolor='black')
axes[0].set_xlabel('Study Time Category', fontsize=12)
axes[0].set_ylabel('Mean Final Grade (G3)', fontsize=12)
axes[0].set_title('Mean G3 by Study Time', fontsize=13, fontweight='bold')
axes[0].set_xticks([1, 2, 3, 4])
axes[0].set_xticklabels(['<2 hrs', '2-5 hrs', '5-10 hrs', '>10 hrs'])
for i, v in enumerate(st_means.values):
    axes[0].text(st_means.index[i], v + 0.2, f'{v:.2f}', ha='center', fontweight='bold')

# Violin plot
parts = axes[1].violinplot([df[df['studytime'] == t]['G3'].values for t in sorted(df['studytime'].unique())],
                            positions=sorted(df['studytime'].unique()), showmeans=True, showmedians=True)
axes[1].set_xlabel('Study Time Category', fontsize=12)
axes[1].set_ylabel('Final Grade (G3)', fontsize=12)
axes[1].set_title('G3 Distribution by Study Time', fontsize=13, fontweight='bold')
axes[1].set_xticks([1, 2, 3, 4])
axes[1].set_xticklabels(['<2 hrs', '2-5 hrs', '5-10 hrs', '>10 hrs'])

fig.suptitle('Figure 4: Study Time vs Final Grade (G3)', fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig04_studytime_vs_G3.png'))
plt.close()
print("Saved: fig04_studytime_vs_G3.png")

# ── D5: Scatter Plot G1 vs G3 ──
fig, ax = plt.subplots(figsize=(10, 7))
scatter = ax.scatter(df['G1'], df['G3'], c=df['G2'], cmap='viridis', alpha=0.7, 
                     edgecolors='gray', s=60)
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Second Period Grade (G2)', fontsize=12)
# Fit line
z = np.polyfit(df['G1'], df['G3'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['G1'].min(), df['G1'].max(), 100)
ax.plot(x_line, p(x_line), 'r--', linewidth=2, 
        label=f'Trend: G3 = {z[0]:.2f}·G1 + {z[1]:.2f}')
r, pval = stats.pearsonr(df['G1'], df['G3'])
ax.set_xlabel('First Period Grade (G1)', fontsize=13)
ax.set_ylabel('Final Grade (G3)', fontsize=13)
ax.set_title(f'Figure 5: G1 vs G3 Scatter Plot (r = {r:.3f}, p < 0.001)', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
plt.savefig(os.path.join(OUTPUT_DIR, 'fig05_scatter_G1_vs_G3.png'))
plt.close()
print("Saved: fig05_scatter_G1_vs_G3.png")

# ── D6: Scatter Plot G2 vs G3 ──
fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(df['G2'], df['G3'], c='#4C72B0', alpha=0.6, edgecolors='gray', s=60)
z2 = np.polyfit(df['G2'], df['G3'], 1)
p2 = np.poly1d(z2)
x_line2 = np.linspace(df['G2'].min(), df['G2'].max(), 100)
ax.plot(x_line2, p2(x_line2), 'r--', linewidth=2, 
        label=f'Trend: G3 = {z2[0]:.2f}·G2 + {z2[1]:.2f}')
r2, pval2 = stats.pearsonr(df['G2'], df['G3'])
ax.set_xlabel('Second Period Grade (G2)', fontsize=13)
ax.set_ylabel('Final Grade (G3)', fontsize=13)
ax.set_title(f'Figure 6: G2 vs G3 Scatter Plot (r = {r2:.3f}, p < 0.001)', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
plt.savefig(os.path.join(OUTPUT_DIR, 'fig06_scatter_G2_vs_G3.png'))
plt.close()
print("Saved: fig06_scatter_G2_vs_G3.png")

# ── D7: Correlation Matrix and Heatmap ──
print("\n── Correlation Matrix (Numerical Columns) ──")
corr_matrix = df[num_cols].corr()
print(corr_matrix.to_string())

# Heatmap
fig, ax = plt.subplots(figsize=(16, 13))
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
            center=0, square=True, linewidths=0.5, ax=ax,
            annot_kws={'size': 8}, vmin=-1, vmax=1)
ax.set_title('Figure 7: Correlation Heatmap – Numerical Variables', fontsize=15, fontweight='bold')
plt.savefig(os.path.join(OUTPUT_DIR, 'fig07_correlation_heatmap.png'))
plt.close()
print("Saved: fig07_correlation_heatmap.png")

# Key correlations with G3
print("\n── Correlations with Final Grade (G3) ──")
corr_g3 = corr_matrix['G3'].drop('G3').sort_values(ascending=False)
print(corr_g3.to_string())

# ══════════════════════════════════════════════════════════════════════════════
# SECTION E: OUTLIER DETECTION (IQR METHOD)
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("SECTION E: OUTLIER DETECTION (IQR METHOD)")
print("=" * 80)

outlier_cols = ['absences', 'G1', 'G2', 'G3', 'failures', 'age', 'studytime']
outlier_summary = []

for col in outlier_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    n_outliers = len(outliers)
    pct = n_outliers / len(df) * 100
    
    outlier_summary.append({
        'Variable': col,
        'Q1': Q1,
        'Q3': Q3,
        'IQR': IQR,
        'Lower Bound': lower,
        'Upper Bound': upper,
        'Outlier Count': n_outliers,
        'Outlier %': f'{pct:.1f}%'
    })
    
    print(f"\n  {col}:")
    print(f"    Q1 = {Q1}, Q3 = {Q3}, IQR = {IQR}")
    print(f"    Lower Bound = {lower:.2f}, Upper Bound = {upper:.2f}")
    print(f"    Outliers found: {n_outliers} ({pct:.1f}%)")
    if n_outliers > 0 and n_outliers <= 20:
        print(f"    Outlier values: {sorted(outliers[col].values)}")

outlier_df = pd.DataFrame(outlier_summary)
print("\n── Outlier Summary Table ──")
print(outlier_df.to_string(index=False))
outlier_df.to_csv(os.path.join(OUTPUT_DIR, 'outlier_summary.csv'), index=False)

# Outlier visualization
fig, axes = plt.subplots(2, 4, figsize=(18, 10))
axes = axes.flatten()
for idx, col in enumerate(outlier_cols):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    
    is_outlier = (df[col] < lower) | (df[col] > upper)
    
    axes[idx].scatter(range(len(df)), df[col], c=['red' if o else '#4C72B0' for o in is_outlier],
                      alpha=0.5, s=20)
    axes[idx].axhline(upper, color='orange', linestyle='--', label=f'Upper={upper:.1f}')
    axes[idx].axhline(lower, color='orange', linestyle='--', label=f'Lower={lower:.1f}')
    axes[idx].set_title(f'{col} (outliers: {is_outlier.sum()})', fontweight='bold')
    axes[idx].legend(fontsize=8)
    axes[idx].set_xlabel('Student Index')
    axes[idx].set_ylabel(col)

# Remove extra subplot
axes[-1].set_visible(False)
fig.suptitle('Figure 8: Outlier Detection using IQR Method', fontsize=15, fontweight='bold', y=1.01)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'fig08_outlier_detection.png'))
plt.close()
print("Saved: fig08_outlier_detection.png")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION F: ADDITIONAL VISUALIZATIONS
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("SECTION F: ADDITIONAL VISUALIZATIONS")
print("=" * 80)

# ── F1: Grade Distribution Comparison (G1, G2, G3) ──
fig, ax = plt.subplots(figsize=(10, 6))
for grade_col, color, label in [('G1', '#4C72B0', 'G1 (Period 1)'), 
                                 ('G2', '#55A868', 'G2 (Period 2)'), 
                                 ('G3', '#C44E52', 'G3 (Final)')]:
    ax.hist(df[grade_col], bins=21, range=(-0.5, 20.5), alpha=0.5, 
            edgecolor='black', color=color, label=label)
ax.set_xlabel('Grade', fontsize=13)
ax.set_ylabel('Frequency', fontsize=13)
ax.set_title('Figure 9: Comparison of Grade Distributions (G1, G2, G3)', fontsize=14, fontweight='bold')
ax.legend(fontsize=11)
plt.savefig(os.path.join(OUTPUT_DIR, 'fig09_grade_comparison.png'))
plt.close()
print("Saved: fig09_grade_comparison.png")

# ── F2: Pair Plot of Grade Variables ──
fig = sns.pairplot(df[['G1', 'G2', 'G3', 'studytime', 'failures']], 
                   diag_kind='kde', corner=True,
                   plot_kws={'alpha': 0.5, 's': 30})
fig.fig.suptitle('Figure 10: Pair Plot of Key Variables', fontsize=15, fontweight='bold', y=1.02)
plt.savefig(os.path.join(OUTPUT_DIR, 'fig10_pairplot.png'))
plt.close()
print("Saved: fig10_pairplot.png")

# ── F3: Gender-based Grade Distribution ──
fig, ax = plt.subplots(figsize=(10, 6))
df.boxplot(column='G3', by='sex', ax=ax, patch_artist=True,
           boxprops=dict(facecolor='#4C72B0', alpha=0.7),
           medianprops=dict(color='red', linewidth=2))
ax.set_xlabel('Sex', fontsize=12)
ax.set_ylabel('Final Grade (G3)', fontsize=12)
ax.set_title('Figure 11: Final Grade Distribution by Gender', fontsize=14, fontweight='bold')
plt.suptitle('')
plt.savefig(os.path.join(OUTPUT_DIR, 'fig11_gender_grades.png'))
plt.close()
print("Saved: fig11_gender_grades.png")

# ══════════════════════════════════════════════════════════════════════════════
# SECTION G: OPTIONAL – MLP CLASSIFIER (Pass/Fail Prediction)
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("SECTION G: OPTIONAL – MLP CLASSIFIER (Pass/Fail Prediction)")
print("=" * 80)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (classification_report, confusion_matrix, 
                              accuracy_score, ConfusionMatrixDisplay)

# Create binary target: Pass (G3 >= 10) or Fail (G3 < 10)
# Note: Portuguese grading scale uses 10 as pass threshold (0-20 scale)
df['pass_fail'] = (df['G3'] >= 10).astype(int)
print(f"\nPass/Fail distribution (threshold G3 >= 10):")
print(df['pass_fail'].value_counts().rename({1: 'Pass', 0: 'Fail'}).to_string())
print(f"Pass rate: {df['pass_fail'].mean()*100:.1f}%")

# IMPORTANT: Exclude G1 and G2 to prevent target leakage
# (G1 and G2 are intermediate grades highly correlated with G3)
feature_cols = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures',
                'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']

# Encode categorical features
df_ml = df.copy()
le_dict = {}
for col in cat_cols:
    le = LabelEncoder()
    df_ml[col] = le.fit_transform(df_ml[col])
    le_dict[col] = le

# Add encoded categoricals
cat_feature_cols = ['school', 'sex', 'address', 'famsize', 'Pstatus', 
                    'Mjob', 'Fjob', 'reason', 'guardian',
                    'schoolsup', 'famsup', 'paid', 'activities', 
                    'nursery', 'higher', 'internet', 'romantic']
all_feature_cols = feature_cols + cat_feature_cols

X = df_ml[all_feature_cols]
y = df_ml['pass_fail']

# Split data: 80% train, 20% test (stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\nTrain set: {X_train.shape[0]} samples")
print(f"Test set:  {X_test.shape[0]} samples")

# Scale features using TRAINING data only (prevent data leakage)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train MLP Classifier
mlp = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation='relu',
    solver='adam',
    max_iter=500,
    random_state=42,
    early_stopping=True,
    validation_fraction=0.15,
    n_iter_no_change=20,
    learning_rate_init=0.001,
    verbose=False
)

mlp.fit(X_train_scaled, y_train)
y_pred = mlp.predict(X_test_scaled)

# Evaluation
print(f"\n── MLP Classifier Results ──")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Fail', 'Pass']))

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()
print(f"Confusion Matrix:")
print(f"  TP={tp}, TN={tn}, FP={fp}, FN={fn}")
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
print(f"  Precision = {precision:.4f}")
print(f"  Recall    = {recall:.4f}")
print(f"  F1-Score  = {f1:.4f}")

# Confusion Matrix Plot
fig, ax = plt.subplots(figsize=(8, 6))
disp = ConfusionMatrixDisplay(cm, display_labels=['Fail', 'Pass'])
disp.plot(ax=ax, cmap='Blues', values_format='d')
ax.set_title('Figure 12: Confusion Matrix – MLP Classifier (Pass/Fail)', 
             fontsize=14, fontweight='bold')
plt.savefig(os.path.join(OUTPUT_DIR, 'fig12_confusion_matrix.png'))
plt.close()
print("Saved: fig12_confusion_matrix.png")

# Training Loss Curve
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(mlp.loss_curve_, color='#4C72B0', linewidth=2, label='Training Loss')
if hasattr(mlp, 'validation_scores_'):
    ax2 = ax.twinx()
    ax2.plot(mlp.validation_scores_, color='#C44E52', linewidth=2, label='Validation Accuracy')
    ax2.set_ylabel('Validation Accuracy', fontsize=12, color='#C44E52')
    ax2.legend(loc='center right', fontsize=11)
ax.set_xlabel('Iteration', fontsize=12)
ax.set_ylabel('Training Loss', fontsize=12, color='#4C72B0')
ax.set_title('Figure 13: MLP Training Loss Curve', fontsize=14, fontweight='bold')
ax.legend(loc='upper right', fontsize=11)
plt.savefig(os.path.join(OUTPUT_DIR, 'fig13_training_loss.png'))
plt.close()
print("Saved: fig13_training_loss.png")

# Feature Importance (approximation using permutation importance)
from sklearn.inspection import permutation_importance
perm_imp = permutation_importance(mlp, X_test_scaled, y_test, n_repeats=10, random_state=42)
feat_imp = pd.Series(perm_imp.importances_mean, index=all_feature_cols).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 10))
feat_imp.plot(kind='barh', ax=ax, color='#4C72B0', edgecolor='black')
ax.set_xlabel('Mean Importance (Permutation)', fontsize=12)
ax.set_title('Figure 14: Feature Importance – MLP Classifier', fontsize=14, fontweight='bold')
plt.savefig(os.path.join(OUTPUT_DIR, 'fig14_feature_importance.png'))
plt.close()
print("Saved: fig14_feature_importance.png")

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 80)
print("EXECUTION COMPLETE")
print("=" * 80)
print(f"\nAll outputs saved to: {os.path.abspath(OUTPUT_DIR)}")
print("Generated files:")
for f in sorted(os.listdir(OUTPUT_DIR)):
    fpath = os.path.join(OUTPUT_DIR, f)
    size = os.path.getsize(fpath)
    print(f"  {f} ({size:,} bytes)")
