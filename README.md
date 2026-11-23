# CET3001 – Practical 01: Exploratory Data Analysis of Student Performance

**Student:** SHRIYASH SAHU  
**Registration Number:** 24BET10001  
**Course Code:** CET3001 – Educational Data Mining and Learning Analytics  

---

## 📁 Project Structure

```
Practical01/
├── README.md                                  ← Project documentation and reproduction guide
├── Complete_Guide/                            ← Comprehensive 8-part in-depth academic & viva guide
│   ├── README.md                              ← Master guide navigation & index
│   ├── 01_Dataset_and_Feature_Dictionary.md   ← Full attribute breakdown & data dictionary
│   ├── 02_Descriptive_Statistics_and_Math.md  ← Mathematical formulas & verified stats tables
│   ├── 03_Exploratory_Visual_Analytics.md     ← Detailed analysis of all 14 figures
│   ├── 04_Outlier_Detection_and_Tukey_Fences.md ← Outlier mechanics, zero-inflation & dropouts
│   ├── 05_TensorFlow_Playground_Simulation.md ← Live neural network simulation & boundary dynamics
│   ├── 06_Target_Leakage_and_MLP_Classifier.md ← Leakage-free ML pipeline & evaluation analysis
│   └── 07_Viva_Voce_and_Exam_Defense_QnA.md    ← Top 15 viva defense questions & model answers
├── code/
│   ├── practical01_eda.py                     ← Main Python script (complete EDA + MLP extension)
│   ├── Practical01_EDA_StudentPerformance.ipynb ← Interactive Jupyter Notebook version
│   ├── capture_playground.js                 ← Headless Chrome script for live TF Playground simulation
│   ├── generate_docx.py                       ← DOCX generation script with all embedded figures
│   └── generate_pdf.py                        ← Publication-quality 15-page PDF compiler
├── data/
│   ├── student-mat.csv                        ← UCI Student Performance (Mathematics, 395 × 33)
│   ├── student-por.csv                        ← UCI Student Performance (Portuguese language)
│   └── student.txt                            ← Dataset attribute documentation
├── outputs/                                   ← All 14 high-resolution EDA figures & summary tables
│   ├── fig01_histogram_G3.png                 ← Final grade distribution histogram
│   ├── fig02_boxplot_G3.png                   ← Box plot of G3 with quartiles
│   ├── fig03_boxplots_key_vars.png            ← Box plots of key numerical variables
│   ├── fig04_studytime_vs_G3.png              ← Study time vs final grade (mean bar & violin plot)
│   ├── fig05_scatter_G1_vs_G3.png             ← Scatter plot G1 vs G3 (r = 0.801)
│   ├── fig06_scatter_G2_vs_G3.png             ← Scatter plot G2 vs G3 (r = 0.905)
│   ├── fig07_correlation_heatmap.png          ← Complete correlation heatmap (16 numerical columns)
│   ├── fig08_outlier_detection.png            ← Tukey IQR outlier bounds visualization
│   ├── fig09_grade_comparison.png             ← Comparative distribution across G1, G2, G3
│   ├── fig10_pairplot.png                     ← Multi-variable pair plot
│   ├── fig11_gender_grades.png                ← Final grade distribution by gender
│   ├── fig12_confusion_matrix.png             ← Confusion matrix of non-leaking MLP classifier
│   ├── fig13_training_loss.png                ← MLP training loss curve & validation trajectory
│   ├── fig14_feature_importance.png           ← Permutation feature importance ranking
│   ├── descriptive_statistics.csv             ← Full statistical metrics export
│   └── outlier_summary.csv                    ← Outlier counts, boundaries, and percentages
├── screenshots/                               ← Live TensorFlow Playground captured simulations
│   ├── playground_results.json                ← Captured training metrics & DOM element inspection
│   ├── tf_playground_default.png              ← Initial default platform interface
│   ├── tf_playground_circle_trained.png       ← Circle dataset trained model (Epoch 302, Test Loss 0.002)
│   └── tf_playground_spiral_trained.png       ← Spiral dataset trained model (Epoch 484, Test Loss 0.002)
└── report/                                    ← Formal practical reports
    ├── Practical01_Report.md                  ← Markdown practical report
    ├── Practical01_Report.docx                ← Microsoft Word report (2.1 MB, fully formatted)
    └── Practical01_Report.pdf                 ← Publication-quality PDF report (15 pages, 2.3 MB)
```

---

## 🚀 How to Reproduce

### Prerequisites
- Python 3.9+ with `pip`
- Google Chrome browser (for headless simulation)
- Node.js & npm (for browser automation)

### Step 1: Install Python Dependencies
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy reportlab pypdf python-docx nbformat
```

### Step 2: Run the Complete EDA Pipeline
```bash
cd Practical01/code
python3 practical01_eda.py
```
This loads `student-mat.csv`, computes all descriptive statistics, executes Tukey IQR outlier detection, trains the non-leaking MLP classifier, and saves all 14 figures in `outputs/`.

### Step 3: Run Interactive Jupyter Notebook
```bash
cd Practical01/code
jupyter notebook Practical01_EDA_StudentPerformance.ipynb
```

### Step 4: Run TensorFlow Playground Live Simulation
```bash
cd Practical01
npm install puppeteer-core
cd code
node capture_playground.js
```
This programmatically controls Google Chrome, loads the exact network topologies onto `playground.tensorflow.org`, runs real backpropagation until convergence, logs loss curves, and captures genuine full-canvas screenshots into `screenshots/`.

### Step 5: Regenerate Reports (DOCX & PDF)
```bash
cd Practical01/code
python3 generate_docx.py
python3 generate_pdf.py
```

---

## 📊 Dataset Information
- **Source:** [UCI Machine Learning Repository – Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance)
- **File Used:** `student-mat.csv` (Mathematics course)
- **Records:** 395 students
- **Attributes:** 33 (16 numerical, 17 categorical)
- **Target Variable:** G3 (Final Grade, 0–20 continuous scale; Pass ≥ 10)
- **Missing Values:** 0 | **Duplicate Records:** 0

---

## 📝 Key Findings & Empirical Results

1. **Grade Dynamics:** Mean final grade is **10.42 / 20** (std = 4.58). The distribution is left-skewed (-0.73) due to a spike of **38 students scoring 0** (administrative dropouts / exam absence).
2. **Predictive Strength:** Prior academic performance is by far the strongest predictor:
   - G2 → G3: $r = 0.905$ ($p < 0.001$, extremely strong)
   - G1 → G3: $r = 0.801$ ($p < 0.001$, strong)
3. **Risk Factors:** Past class failures is the single strongest non-grade negative correlate ($r = -0.360$).
4. **Outliers:** 
   - Absences has 15 extreme outliers (up to 75 absences); retained as high-risk intervention targets.
   - Failures has 83 records flagged by IQR fences due to $IQR = 0$; identified as a statistical artifact of zero-inflated data.
5. **TensorFlow Playground Simulations:**
   - **Circle:** 2 layers × 4 neurons, ReLU activation reached **Test Loss 0.002, Train Loss 0.001 at Epoch 302**, forming a distinct circular decision boundary.
   - **Spiral:** 3 layers (6, 4, 2 neurons), Tanh activation with 7 engineered features reached **Test Loss 0.002, Train Loss 0.001 at Epoch 484**, successfully resolving the non-linear interlocking spiral arms.
6. **MLP Classification (No Target Leakage):**
   - Excluding G1/G2 to model true pre-course early intervention achieved **64.56% test accuracy**.
   - High recall on passing students (90.57%), but low recall on failing students (11.5%) due to class imbalance (67% Pass vs 33% Fail), confirming that demographic features alone cannot replace continuous formative assessments.

---

## 📄 References
- Cortez, P., & Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance. *Proceedings of EPIA 2008*.
- UCI ML Repository: https://archive.ics.uci.edu/dataset/320/student+performance
- TensorFlow Playground: https://playground.tensorflow.org/
