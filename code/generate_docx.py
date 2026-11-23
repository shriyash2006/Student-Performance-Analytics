#!/usr/bin/env python3
"""Generate DOCX report for Practical 01."""
import os
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT

REPORT_DIR = os.path.join(os.path.dirname(__file__), '..', 'report')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
os.makedirs(REPORT_DIR, exist_ok=True)

doc = Document()

# ── Page setup ──
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)

# ── Helper functions ──
def add_heading_styled(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0, 51, 102)
    return h

def add_figure(filename, caption, width=Inches(5.5)):
    path = os.path.join(OUTPUT_DIR, filename)
    if not os.path.exists(path):
        path = os.path.join(SCREENSHOT_DIR, filename)
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture(path, width=width)
        cap = doc.add_paragraph(caption)
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.style = doc.styles['Normal']
        for run in cap.runs:
            run.font.size = Pt(10)
            run.font.italic = True
    else:
        doc.add_paragraph(f"[Image not found: {filename}]")

def add_table(headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Light Grid Accent 1'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = str(h)
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.bold = True
                run.font.size = Pt(10)
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            cell = table.rows[r_idx + 1].cells[c_idx]
            cell.text = str(val)
            for p in cell.paragraphs:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in p.runs:
                    run.font.size = Pt(10)
    return table


# ══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ══════════════════════════════════════════════════════════════════════════════
for _ in range(4):
    doc.add_paragraph()

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('CET3001 – Educational Data Mining\nand Learning Analytics')
run.font.size = Pt(26)
run.font.bold = True
run.font.color.rgb = RGBColor(0, 51, 102)

doc.add_paragraph()

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run('PRACTICAL FILE')
run.font.size = Pt(20)
run.font.bold = True

doc.add_paragraph()
doc.add_paragraph()

details = [
    ('Practical No.', '01'),
    ('Title', 'Exploratory Data Analysis of Student Performance'),
    ('Name', 'SHRIYASH SAHU'),
    ('Reg. Number', '24BET10001'),
    ('Course Code', 'CET3001'),
    ('Date', 'November 2026'),
]

table = doc.add_table(rows=len(details), cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, (key, val) in enumerate(details):
    table.rows[i].cells[0].text = key
    table.rows[i].cells[1].text = val
    for p in table.rows[i].cells[0].paragraphs:
        for run in p.runs:
            run.font.bold = True
            run.font.size = Pt(13)
    for p in table.rows[i].cells[1].paragraphs:
        for run in p.runs:
            run.font.size = Pt(13)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 1. AIM
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('1. AIM', level=1)
doc.add_paragraph(
    'To perform a comprehensive Exploratory Data Analysis (EDA) on the UCI Student '
    'Performance dataset (student-mat.csv) to understand data distributions, calculate '
    'descriptive statistics, visualize grade patterns, explore variable correlations, '
    'identify outliers, demonstrate neural network simulation using TensorFlow Playground, '
    'and optionally train an MLP classifier for pass/fail prediction.'
)

# ══════════════════════════════════════════════════════════════════════════════
# 2. APPARATUS / TOOLS REQUIRED
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('2. Apparatus / Tools Required', level=1)
add_table(
    ['Category', 'Details'],
    [
        ['Operating System', 'macOS'],
        ['Programming Language', 'Python 3.x'],
        ['IDE / Environment', 'Google Colab / Jupyter Notebook / Terminal'],
        ['Primary Platform', 'TensorFlow Playground (https://playground.tensorflow.org/)'],
        ['Dataset', 'UCI Student Performance – Mathematics (student-mat.csv)'],
        ['Dataset Source', 'https://archive.ics.uci.edu/dataset/320/student+performance'],
        ['Libraries', 'pandas, numpy, matplotlib, seaborn, scipy, scikit-learn'],
        ['ML Framework', 'scikit-learn 1.9 (MLPClassifier)'],
    ]
)

# ══════════════════════════════════════════════════════════════════════════════
# 3. THEORY
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('3. Theory', level=1)

doc.add_heading('3.1 Exploratory Data Analysis (EDA)', level=2)
doc.add_paragraph(
    'Exploratory Data Analysis is a systematic approach to analyzing datasets using '
    'statistical summaries and graphical representations. In Educational Data Mining, '
    'EDA reveals academic performance distributions, relationships between factors and '
    'grades, anomalies, and data quality issues.'
)

doc.add_heading('3.2 Descriptive Statistics', level=2)
doc.add_paragraph(
    'Measures of Central Tendency:\n'
    '• Mean: x̄ = (1/n) Σxᵢ\n'
    '• Median: Middle value when data is sorted\n'
    '• Mode: Most frequent value\n\n'
    'Measures of Dispersion:\n'
    '• Variance: σ² = (1/(n-1)) Σ(xᵢ - x̄)²\n'
    '• Standard Deviation: σ = √(variance)\n'
    '• IQR = Q3 - Q1\n\n'
    'Measures of Shape:\n'
    '• Skewness: Measures asymmetry of the distribution\n'
    '• Kurtosis: Measures tailedness of the distribution'
)

doc.add_heading('3.3 Pearson Correlation Coefficient', level=2)
doc.add_paragraph(
    'r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)² · Σ(yᵢ - ȳ)²]\n\n'
    '• |r| > 0.7: Strong correlation\n'
    '• 0.3 < |r| < 0.7: Moderate correlation\n'
    '• |r| < 0.3: Weak correlation'
)

doc.add_heading('3.4 IQR Outlier Detection', level=2)
doc.add_paragraph(
    'The Interquartile Range method:\n'
    '1. Compute Q1 (25th percentile) and Q3 (75th percentile)\n'
    '2. IQR = Q3 - Q1\n'
    '3. Lower Bound = Q1 - 1.5 × IQR\n'
    '4. Upper Bound = Q3 + 1.5 × IQR\n'
    '5. Values outside [Lower, Upper] are outliers'
)

doc.add_heading('3.5 Multi-Layer Perceptron (MLP)', level=2)
doc.add_paragraph(
    'The MLP is a feedforward neural network used in the optional extension:\n'
    '• Input layer: 30 features\n'
    '• Hidden layer 1: 64 neurons, ReLU activation\n'
    '• Hidden layer 2: 32 neurons, ReLU activation\n'
    '• Output: Binary classification (Pass/Fail)\n'
    '• Optimizer: Adam\n'
    '• Loss: Binary Cross-Entropy\n\n'
    'ReLU(x) = max(0, x)\n\n'
    'Classification Metrics:\n'
    '• Accuracy = (TP + TN) / (TP + TN + FP + FN)\n'
    '• Precision = TP / (TP + FP)\n'
    '• Recall = TP / (TP + FN)\n'
    '• F1-Score = 2 × Precision × Recall / (Precision + Recall)'
)

doc.add_heading('3.6 TensorFlow Playground', level=2)
doc.add_paragraph(
    'An interactive web-based neural network visualizer providing:\n'
    '• Built-in datasets: Circle, XOR, Gaussian, Spiral\n'
    '• Configurable hidden layers (1-6), neurons (1-8), activation functions\n'
    '• Real-time visualization of decision boundaries, weights, and loss\n\n'
    'Note: TensorFlow Playground uses synthetic 2D datasets for demonstration. '
    'These are NOT related to the UCI Student Performance dataset.'
)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 4. METHODOLOGY
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('4. Methodology / Procedure', level=1)

steps = [
    'Install Python libraries: pandas, numpy, matplotlib, seaborn, scipy, scikit-learn.',
    'Download the UCI Student Performance dataset from https://archive.ics.uci.edu/dataset/320/student+performance.',
    'Extract student-mat.csv (Mathematics, 395 records, 33 attributes, semicolon-separated).',
    'Load dataset using pd.read_csv(path, sep=";").',
    'Inspect: Display head/tail, shape, dtypes, missing values, duplicates.',
    'Identify numerical (16) and categorical (17) columns.',
    'Compute descriptive statistics: mean, median, mode, variance, std, quartiles, IQR, skewness, kurtosis.',
    'Generate histogram of G3 with mean and median lines.',
    'Generate box plot of G3 and box plots for all key variables.',
    'Generate bar chart and violin plot for studytime vs G3.',
    'Generate scatter plots: G1 vs G3 (with trend line), G2 vs G3.',
    'Compute correlation matrix and generate heatmap.',
    'Apply IQR outlier detection on key variables.',
    'Visualize outliers with scatter plots showing IQR bounds.',
    'Open TensorFlow Playground, configure Circle and Spiral experiments, train, capture screenshots.',
    'Create binary target (Pass: G3≥10, Fail: G3<10), excluding G1/G2 to prevent target leakage.',
    'Train MLP classifier (64,32) with ReLU, Adam, early stopping.',
    'Evaluate using accuracy, precision, recall, F1-score, confusion matrix.',
    'Save all outputs and prepare report.',
]
for i, step in enumerate(steps, 1):
    doc.add_paragraph(f'{i}. {step}')

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 5. ALGORITHM / WORKFLOW
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('5. Algorithm / Architecture / Workflow', level=1)

doc.add_heading('5.1 EDA Workflow', level=2)
doc.add_paragraph(
    'Dataset Acquisition → Data Loading → Data Inspection → '
    'Descriptive Statistics → Visualization → Outlier Detection → '
    'Interpretation & Reporting'
)

doc.add_heading('5.2 EDA Pseudocode', level=2)
doc.add_paragraph(
    'ALGORITHM: EDA of Student Performance\n'
    'INPUT: student-mat.csv (395 × 33)\n'
    'OUTPUT: Statistics, visualizations, outlier analysis\n\n'
    '1. LOAD dataset with sep=";" \n'
    '2. DISPLAY shape, head(5), tail(5)\n'
    '3. IDENTIFY numerical_cols, categorical_cols\n'
    '4. CHECK missing_values, duplicates\n'
    '5. FOR EACH col IN focus_variables:\n'
    '     COMPUTE mean, median, mode, var, std, Q1, Q3, IQR, skewness, kurtosis\n'
    '6. PLOT histogram(G3), boxplot(G3)\n'
    '7. PLOT scatter(G1, G3) with trend line\n'
    '8. COMPUTE correlation_matrix; PLOT heatmap\n'
    '9. FOR EACH col IN outlier_variables:\n'
    '     lower = Q1 - 1.5*IQR; upper = Q3 + 1.5*IQR\n'
    '     outliers = values outside [lower, upper]\n'
    '10. SAVE all figures and statistics'
)

doc.add_heading('5.3 MLP Architecture', level=2)
doc.add_paragraph(
    'Input Layer (30 features) → Hidden Layer 1 (64 neurons, ReLU) → '
    'Hidden Layer 2 (32 neurons, ReLU) → Output (1 neuron, Sigmoid)\n\n'
    'Optimizer: Adam | Loss: Binary Cross-Entropy | Early Stopping: Yes'
)

doc.add_heading('5.4 TensorFlow Playground Configuration', level=2)
add_table(
    ['Parameter', 'Experiment 1 (Circle)', 'Experiment 2 (Spiral)'],
    [
        ['Dataset', 'Circle', 'Spiral'],
        ['Input Features', 'X₁, X₂', 'All 7 features'],
        ['Hidden Layers', '2 (4, 4)', '3 (6, 4, 2)'],
        ['Activation', 'ReLU', 'Tanh'],
        ['Learning Rate', '0.03', '0.03'],
        ['Noise', '~15', '~0'],
        ['Target Epochs', '200+', '400+'],
    ]
)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 6. PROGRAM / IMPLEMENTATION
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('6. Program / Implementation', level=1)
doc.add_paragraph(
    'The complete implementation is available in two forms:\n'
    '• Python script: code/practical01_eda.py\n'
    '• Jupyter notebook: code/Practical01_EDA_StudentPerformance.ipynb\n\n'
    'Key code sections are shown below with explanations.'
)

code_blocks = [
    ('Data Loading', '''df = pd.read_csv('../data/student-mat.csv', sep=';')
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(df.head())'''),
    ('Descriptive Statistics', '''focus_cols = ['studytime', 'failures', 'absences', 'G1', 'G2', 'G3']
desc = df[num_cols].describe().T
desc['median'] = df[num_cols].median()
desc['mode'] = df[num_cols].mode().iloc[0]
desc['variance'] = df[num_cols].var()
desc['skewness'] = df[num_cols].skew()
desc['kurtosis'] = df[num_cols].kurtosis()'''),
    ('Histogram of G3', '''fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['G3'], bins=21, range=(-0.5, 20.5), edgecolor='black')
ax.axvline(df['G3'].mean(), color='red', linestyle='--', label='Mean')
ax.axvline(df['G3'].median(), color='green', linestyle='-.', label='Median')
ax.legend()
plt.savefig('fig01_histogram_G3.png')'''),
    ('Scatter Plot with Correlation', '''scatter = ax.scatter(df['G1'], df['G3'], c=df['G2'], cmap='viridis')
z = np.polyfit(df['G1'], df['G3'], 1)
r, pval = stats.pearsonr(df['G1'], df['G3'])
ax.set_title(f'G1 vs G3 (r = {r:.3f})')'''),
    ('Correlation Heatmap', '''corr_matrix = df[num_cols].corr()
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdBu_r', center=0)'''),
    ('IQR Outlier Detection', '''for col in outlier_cols:
    Q1, Q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]'''),
    ('MLP Classifier', '''df['pass_fail'] = (df['G3'] >= 10).astype(int)
# Exclude G1, G2 (target leakage prevention)
mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu',
                    solver='adam', max_iter=500, early_stopping=True)
mlp.fit(X_train_scaled, y_train)
print(f"Accuracy: {accuracy_score(y_test, mlp.predict(X_test_scaled)):.4f}")'''),
]

for title, code in code_blocks:
    doc.add_heading(title, level=3)
    p = doc.add_paragraph()
    run = p.add_run(code)
    run.font.name = 'Courier New'
    run.font.size = Pt(9)
    doc.add_paragraph()

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 7. OUTPUT / SIMULATION
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('7. Output / Simulation', level=1)

doc.add_heading('7.1 Dataset Inspection', level=2)
doc.add_paragraph('Dataset: 395 rows × 33 columns | Missing: 0 | Duplicates: 0')
doc.add_paragraph('Students with G3 = 0 (possible dropouts): 38')

doc.add_heading('7.2 Descriptive Statistics', level=2)
add_table(
    ['Statistic', 'studytime', 'failures', 'absences', 'G1', 'G2', 'G3'],
    [
        ['Mean', '2.0354', '0.3342', '5.7089', '10.9089', '10.7139', '10.4152'],
        ['Median', '2.0', '0.0', '4.0', '11.0', '11.0', '11.0'],
        ['Mode', '2', '0', '0', '10', '9', '10'],
        ['Std Dev', '0.8392', '0.7437', '8.0031', '3.3192', '3.7615', '4.5814'],
        ['Variance', '0.7043', '0.5530', '64.0495', '11.0171', '14.1489', '20.9896'],
        ['Min', '1', '0', '0', '3', '0', '0'],
        ['Max', '4', '3', '75', '19', '19', '20'],
        ['Q1', '1.0', '0.0', '0.0', '8.0', '9.0', '8.0'],
        ['Q3', '2.0', '0.0', '8.0', '13.0', '13.0', '14.0'],
        ['IQR', '1.0', '0.0', '8.0', '5.0', '4.0', '6.0'],
        ['Skewness', '0.6321', '2.3870', '3.6716', '0.2406', '−0.4316', '−0.7327'],
        ['Kurtosis', '−0.0144', '5.0047', '21.7191', '−0.6938', '0.6277', '0.4034'],
    ]
)

doc.add_paragraph()

doc.add_heading('7.3 Visualizations', level=2)
add_figure('fig01_histogram_G3.png', 'Figure 1: Distribution of Final Grades (G3)')
add_figure('fig02_boxplot_G3.png', 'Figure 2: Box Plot of Final Grades (G3)')
add_figure('fig03_boxplots_key_vars.png', 'Figure 3: Box Plots of Key Variables')
add_figure('fig04_studytime_vs_G3.png', 'Figure 4: Study Time vs Final Grade')
add_figure('fig05_scatter_G1_vs_G3.png', 'Figure 5: G1 vs G3 Scatter Plot (r = 0.801)')
add_figure('fig06_scatter_G2_vs_G3.png', 'Figure 6: G2 vs G3 Scatter Plot (r = 0.905)')
add_figure('fig07_correlation_heatmap.png', 'Figure 7: Correlation Heatmap', width=Inches(6))
add_figure('fig09_grade_comparison.png', 'Figure 9: Grade Distribution Comparison (G1, G2, G3)')
add_figure('fig10_pairplot.png', 'Figure 10: Pair Plot of Key Variables', width=Inches(5))
add_figure('fig11_gender_grades.png', 'Figure 11: Grade Distribution by Gender')

doc.add_heading('7.4 Correlations with G3', level=2)
add_table(
    ['Variable', 'Correlation', 'Strength'],
    [
        ['G2', '+0.905', 'Very Strong Positive'],
        ['G1', '+0.801', 'Strong Positive'],
        ['Medu', '+0.217', 'Weak Positive'],
        ['Fedu', '+0.152', 'Weak Positive'],
        ['studytime', '+0.098', 'Very Weak'],
        ['failures', '−0.360', 'Moderate Negative'],
        ['age', '−0.162', 'Weak Negative'],
        ['goout', '−0.133', 'Weak Negative'],
    ]
)

doc.add_heading('7.5 Outlier Detection Results', level=2)
add_table(
    ['Variable', 'Q1', 'Q3', 'IQR', 'Lower', 'Upper', 'Count', '%'],
    [
        ['absences', '0.0', '8.0', '8.0', '−12.0', '20.0', '15', '3.8%'],
        ['G1', '8.0', '13.0', '5.0', '0.5', '20.5', '0', '0.0%'],
        ['G2', '9.0', '13.0', '4.0', '3.0', '19.0', '13', '3.3%'],
        ['G3', '8.0', '14.0', '6.0', '−1.0', '23.0', '0', '0.0%'],
        ['failures', '0.0', '0.0', '0.0', '0.0', '0.0', '83', '21.0%'],
        ['age', '16.0', '18.0', '2.0', '13.0', '21.0', '1', '0.3%'],
        ['studytime', '1.0', '2.0', '1.0', '−0.5', '3.5', '27', '6.8%'],
    ]
)
doc.add_paragraph()
add_figure('fig08_outlier_detection.png', 'Figure 8: Outlier Detection using IQR Method', width=Inches(6))

doc.add_heading('7.6 TensorFlow Playground Simulation', level=2)
doc.add_paragraph(
    'The live simulation was executed and captured from https://playground.tensorflow.org/. '
    'Below are the actual platform configurations, training metrics, and resulting decision boundaries.'
)

doc.add_heading('7.6.1 Platform Overview & Built-in Capabilities', level=3)
doc.add_paragraph(
    '• Datasets: Circle, Exclusive OR (XOR), Gaussian clusters, Spiral (Classification); Plane, Multi-Gaussian (Regression)\n'
    '• Features: X₁, X₂, X₁², X₂², X₁X₂, sin(X₁), sin(X₂)\n'
    '• Activation Functions: ReLU, Tanh, Sigmoid, Linear\n'
    '• Regularization: None, L1, L2\n'
    '• Hidden Layers: Up to 6 layers, 1–8 neurons per layer'
)
add_figure('tf_playground_default.png', 'Figure 15: TensorFlow Playground – Default Interface', width=Inches(6.0))

doc.add_heading('7.6.2 Experiment 1: Circle Dataset (Non-linear Classification with ReLU)', level=3)
add_table(
    ['Parameter', 'Configured Value'],
    [
        ['Dataset', 'Circle (concentric rings)'],
        ['Features', 'X₁, X₂ (raw 2D coordinates)'],
        ['Hidden Layers', '2 layers (4 neurons, 4 neurons)'],
        ['Activation', 'ReLU'],
        ['Learning Rate', '0.03'],
        ['Noise', '15'],
        ['Train / Test Ratio', '50%'],
        ['Epochs Reached', '302'],
        ['Final Training Loss', '0.001'],
        ['Final Test Loss', '0.002'],
    ]
)
doc.add_paragraph(
    'Observation: At epoch 302, the network formed a closed circular decision boundary around the inner class. '
    'The combination of piecewise linear ReLU units in two hidden layers successfully partitioned the non-linearly separable 2D space.'
)
add_figure('tf_playground_circle_trained.png', 'Figure 16: Circle Dataset – Trained Model & Decision Boundary (Epoch 302)', width=Inches(6.0))

doc.add_heading('7.6.3 Experiment 2: Spiral Dataset (Complex Manifold with Tanh)', level=3)
add_table(
    ['Parameter', 'Configured Value'],
    [
        ['Dataset', 'Spiral (interleaved spiral arms)'],
        ['Features', 'All 7 features (X₁, X₂, X₁², X₂², X₁X₂, sin(X₁), sin(X₂))'],
        ['Hidden Layers', '3 layers (6, 4, 2 neurons)'],
        ['Activation', 'Tanh'],
        ['Learning Rate', '0.03'],
        ['Noise', '0'],
        ['Train / Test Ratio', '50%'],
        ['Epochs Reached', '484'],
        ['Final Training Loss', '0.001'],
        ['Final Test Loss', '0.002'],
    ]
)
doc.add_paragraph(
    'Observation: The spiral manifold presents severe non-linear curvature. By combining higher-order sinusoidal '
    'and polynomial input features with smooth Tanh activations, the 3-layer network successfully mapped the interlocking arms '
    'with a test loss of 0.002.'
)
add_figure('tf_playground_spiral_trained.png', 'Figure 17: Spiral Dataset – Trained Model & Decision Boundary (Epoch 484)', width=Inches(6.0))

doc.add_heading('7.7 MLP Classifier Results', level=2)
doc.add_paragraph('Pass/Fail Distribution: Pass = 265 (67.1%), Fail = 130 (32.9%)')
doc.add_paragraph('Train: 316 samples | Test: 79 samples | Accuracy: 0.6456 (64.56%)')
doc.add_paragraph()

add_table(
    ['Metric', 'Fail', 'Pass', 'Weighted Avg'],
    [
        ['Precision', '0.38', '0.68', '0.58'],
        ['Recall', '0.12', '0.91', '0.65'],
        ['F1-Score', '0.18', '0.77', '0.58'],
        ['Support', '26', '53', '79'],
    ]
)

doc.add_paragraph()
doc.add_paragraph('Confusion Matrix: TP=48, TN=3, FP=23, FN=5')
add_figure('fig12_confusion_matrix.png', 'Figure 12: Confusion Matrix – MLP Classifier')
add_figure('fig13_training_loss.png', 'Figure 13: MLP Training Loss Curve')
add_figure('fig14_feature_importance.png', 'Figure 14: Feature Importance (Permutation)')

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 8. RESULTS AND INTERPRETATION
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('8. Results and Interpretation', level=1)

doc.add_heading('8.1 Dataset Characteristics', level=2)
doc.add_paragraph(
    'The dataset contains 395 student records with 33 attributes. It is clean with zero '
    'missing values and zero duplicates. 38 students scored G3 = 0, likely indicating dropouts.'
)

doc.add_heading('8.2 Statistical Findings', level=2)
doc.add_paragraph(
    '• G3 mean = 10.42, std = 4.58, negative skewness (−0.73) due to dropout spike at zero.\n'
    '• Absences is the most dispersed (variance=64.05, range=75, skewness=3.67, kurtosis=21.72).\n'
    '• Failures has IQR=0 (highly concentrated at zero); IQR method artifacts flag 21% as outliers.\n'
    '• Study time has weak correlation with G3 (r=0.098); prior grades are far stronger predictors.'
)

doc.add_heading('8.3 Correlation Insights', level=2)
doc.add_paragraph(
    '• G2→G3 (r=0.905) and G1→G3 (r=0.801): Strongest predictors.\n'
    '• Failures→G3 (r=−0.360): Strongest negative non-grade correlation.\n'
    '• Mother\'s education (r=0.217) has stronger influence than father\'s (r=0.152).\n'
    '• Social/lifestyle factors show weak negative correlations with grades.'
)

doc.add_heading('8.4 Outlier Analysis', level=2)
doc.add_paragraph(
    '• Absences: 15 outliers (up to 75) — Retain; represent high-risk students.\n'
    '• G2: 13 outliers (all G2=0) — Dropout indicators; flag but retain.\n'
    '• Failures: 83 "outliers" — Statistical artifact (IQR=0); do not treat as outliers.\n'
    '• Age: 1 outlier (age=22) — Valid data point; retain.'
)

doc.add_heading('8.5 MLP Classifier', level=2)
doc.add_paragraph(
    'Accuracy: 64.6% (without G1/G2 to prevent leakage). The model has high Pass recall (91%) '
    'but very low Fail recall (12%), biased by class imbalance. This demonstrates that socio-demographic '
    'features alone provide moderate predictive power; intermediate grades are essential for reliable '
    'early-warning systems.'
)

doc.add_heading('8.6 Limitations', level=2)
doc.add_paragraph(
    '1. Small dataset (395 records) limits ML generalisation.\n'
    '2. Class imbalance (67/33%) affects Fail class recall.\n'
    '3. Data from two Portuguese schools; may not generalise globally.\n'
    '4. Synthetic Nature of Simulation: TensorFlow Playground demonstrates 2D synthetic datasets rather than tabular student records.\n'
    '5. Simple label encoding; one-hot encoding may improve results.'
)

doc.add_heading('8.7 Conclusion', level=2)
doc.add_paragraph(
    'This practical demonstrated comprehensive EDA on the UCI Student Performance dataset. '
    'Key findings: G3 is most strongly predicted by prior grades (G2: r=0.905, G1: r=0.801) and '
    'negatively by failures (r=−0.360). Absences show significant outliers requiring attention. '
    'The MLP classifier achieves 64.6% accuracy using background features alone, confirming that '
    'intermediate assessments are essential for reliable student performance prediction. '
    'TensorFlow Playground effectively demonstrates neural network decision boundary learning.'
)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════════════════
# 9. REFERENCES
# ══════════════════════════════════════════════════════════════════════════════
add_heading_styled('9. References', level=1)

refs = [
    'Cortez, P., & Silva, A. (2008). Using Data Mining to Predict Secondary School Student '
    'Performance. Proceedings of EPIA 2008, pp. 5-12, Porto, Portugal.',
    'UCI ML Repository – Student Performance: https://archive.ics.uci.edu/dataset/320/student+performance',
    'TensorFlow Playground: https://playground.tensorflow.org/',
    'pandas Documentation: https://pandas.pydata.org/docs/',
    'scikit-learn MLPClassifier: https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html',
    'Seaborn: https://seaborn.pydata.org/',
    'Matplotlib: https://matplotlib.org/stable/',
    'SciPy stats: https://docs.scipy.org/doc/scipy/reference/stats.html',
    'Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley.',
]

for i, ref in enumerate(refs, 1):
    doc.add_paragraph(f'[{i}] {ref}')

# ── Save ──
docx_path = os.path.join(REPORT_DIR, 'Practical01_Report.docx')
doc.save(docx_path)
print(f'DOCX saved: {docx_path}')
