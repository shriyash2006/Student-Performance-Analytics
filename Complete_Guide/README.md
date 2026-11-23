# 📖 CET3001: Educational Data Mining — Complete Practical Guide

> **Student:** SHRIYASH SAHU (24BET10001)  
> **Course:** CET3001 – Educational Data Mining and Learning Analytics  
> **Practical 01:** Exploratory Data Analysis of Student Performance  
> **Repository:** [Student-Performance-Analytics](https://github.com/shriyash2006/Student-Performance-Analytics)

---

## 📌 Guide Overview

This directory provides an exhaustive, step-by-step academic and technical breakdown of the entire practical. Whether you are reviewing for a laboratory viva, presenting your project in an academic seminar, or implementing educational data mining pipelines, each module in this guide explains the underlying mathematics, implementation choices, and educational significance.

```
Complete_Guide/
├── README.md                                 ← Master Guide Navigation & Index (This File)
├── 01_Dataset_and_Feature_Dictionary.md      ← Detailed dataset attributes & schema definitions
├── 02_Descriptive_Statistics_and_Math.md     ← Mathematical formulas, dispersion & shape calculations
├── 03_Exploratory_Visual_Analytics.md        ← Breakdown of all 14 figures & educational takeaways
├── 04_Outlier_Detection_and_Tukey_Fences.md  ← Outlier analysis, zero-inflation artifacts & dropouts
├── 05_TensorFlow_Playground_Simulation.md    ← Live neural network simulation & boundary mechanics
├── 06_Target_Leakage_and_MLP_Classifier.md   ← Leakage-free ML extension, architecture & evaluations
└── 07_Viva_Voce_and_Exam_Defense_QnA.md       ← Top 15 viva defense questions & model answers
```

---

## 📑 Module Directory

### [Module 01: Dataset & Feature Dictionary](01_Dataset_and_Feature_Dictionary.md)
* Origin and structure of the **UCI Student Performance Benchmark** (`student-mat.csv`).
* The 33 attributes classified into Demographics, Socio-Economics, Lifestyle, and Academic Performance.
* The Portuguese 0–20 grading system and the official passing threshold ($G3 \ge 10$).
* Technical parsing nuances: semicolon (`;`) delimiters and 0 missing values.

### [Module 02: Descriptive Statistics & Mathematical Formulations](02_Descriptive_Statistics_and_Math.md)
* **Central Tendency:** Arithmetic Mean ($\bar{x}$), Median ($Q_2$), Mode.
* **Dispersion & Variability:** Sample Variance ($s^2$), Standard Deviation ($s$), Range, Interquartile Range ($IQR$).
* **Distribution Shape:** Fisher-Pearson Standardized Skewness & Sample Excess Kurtosis.
* Verified empirical tables for `studytime`, `failures`, `absences`, `G1`, `G2`, and `G3`.

### [Module 03: Exploratory Visual Analytics](03_Exploratory_Visual_Analytics.md)
* In-depth commentary on all **14 high-resolution figures**.
* Univariate distributions: Why $G3$ exhibits left-skewed bimodal behavior.
* Bivariate relationships: Study time violin plots and the temporal consistency of academic trajectory.
* Relational dependencies: Linear regression trends between $G1 \to G3$ ($r = 0.801$) and $G2 \to G3$ ($r = 0.905$).
* Heatmap correlation analysis: Identifying positive socio-economic buffers and failure penalties.

### [Module 04: Outlier Detection & Tukey's Fences](04_Outlier_Detection_and_Tukey_Fences.md)
* Mathematical definition of Tukey's IQR inner and outer fences ($[Q_1 - 1.5\cdot IQR, Q_3 + 1.5\cdot IQR]$).
* The **Absences Outlier Group** (15 students up to 75 absences) and why deleting them causes survivorship bias.
* The **Zero-Inflation Artifact in Failures**: Why $IQR = 0$ flags 83 valid records as statistical outliers.
* Administrative dropout analysis: Isolating the 38 students scoring $G3 = 0$.

### [Module 05: TensorFlow Playground Live Simulation](05_TensorFlow_Playground_Simulation.md)
* Purpose of interactive neural simulation and distinguishing synthetic 2D coordinates from multi-dimensional tabular data.
* **Experiment 1 (Circle Dataset):** 2 hidden layers (4, 4 neurons) with ReLU activation converging at **Epoch 302** (Test Loss: 0.002) to form a convex closed boundary.
* **Experiment 2 (Spiral Dataset):** 3 hidden layers (6, 4, 2 neurons) with Tanh activation and 7 engineered features converging at **Epoch 484** (Test Loss: 0.002).
* Automated Headless Chrome extraction via Puppeteer (`capture_playground.js`).

### [Module 06: Target Leakage Prevention & MLP Classification](06_Target_Leakage_and_MLP_Classifier.md)
* The danger of **Target Leakage** in Educational Early Warning Systems.
* Why omitting $G1$ and $G2$ is mandatory for meaningful pre-course risk prediction.
* Multi-Layer Perceptron (64 $\to$ 32 $\to$ 1) design, ReLU non-linearity, and Adam optimization.
* Train-only `StandardScaler` fitting to prevent data snooping.
* Evaluation breakdown: Confusion Matrix (TP=48, TN=3, FP=23, FN=5), 64.56% Accuracy, and Class Imbalance nuances.

### [Module 07: Viva Voce & Oral Defense Q&A](07_Viva_Voce_and_Exam_Defense_QnA.md)
* 15 high-frequency oral examination and viva questions with rigorous, mathematically sound answers.
* How to present the practical narrative effectively in an academic viva.

---

## 🎯 Quick Reference Cheat Sheet

| Metric / Parameter | Value / Finding | Educational Context |
|---|---|---|
| **Total Records** | 395 students | Collected across two Portuguese secondary schools |
| **Total Features** | 33 attributes | 16 numerical, 17 categorical |
| **Missing Values** | 0 entries | Clean dataset, no imputation required |
| **Mean Final Grade ($G3$)** | 10.42 / 20 | Sits directly above the passing threshold (10) |
| **Standard Deviation ($G3$)** | 4.58 | Substantial spread across student performance |
| **Pass Rate ($G3 \ge 10$)** | 67.1% (265 Passed / 130 Failed) | 2:1 class imbalance between passing and failing |
| **Top Positive Predictor** | $G2$ Grade ($r = +0.905$) | Strong temporal correlation in student evaluations |
| **Top Negative Predictor** | Past Failures ($r = -0.360$) | Prior academic failure compound into future difficulty |
| **Study Time Correlation** | $r = +0.098$ | Weak linear correlation; study time alone does not guarantee success |
| **Dropout Count ($G3 = 0$)** | 38 students (9.6%) | Administrative dropouts / unattempted final exams |
| **Absences Outliers** | 15 students (Max: 75 days) | Retained as critical targets for educational counseling |
| **MLP Accuracy (No Leakage)** | 64.56% | Predicts Pass/Fail using strictly pre-course demographics |
