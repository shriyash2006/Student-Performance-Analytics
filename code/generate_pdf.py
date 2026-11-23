#!/usr/bin/env python3
"""
Generate comprehensive PDF report for CET3001 Practical 01 using ReportLab.
Student: SHRIYASH SAHU | Reg No: 24BET10001
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, '..', 'report')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'outputs')
SCREENSHOT_DIR = os.path.join(BASE_DIR, '..', 'screenshots')
PDF_PATH = os.path.join(REPORT_DIR, 'Practical01_Report.pdf')

os.makedirs(REPORT_DIR, exist_ok=True)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.saveState()
                self.setFont("Helvetica", 9)
                self.setFillColor(colors.HexColor('#555555'))
                # Header
                self.drawString(54, 11 * inch - 36, "CET3001 – Educational Data Mining | Practical 01: Student EDA")
                self.setStrokeColor(colors.HexColor('#CCCCCC'))
                self.setLineWidth(0.5)
                self.line(54, 11 * inch - 40, 8.5 * inch - 54, 11 * inch - 40)
                # Footer
                page_text = f"Page {self._pageNumber} of {num_pages}"
                self.drawRightString(8.5 * inch - 54, 30, page_text)
                self.drawString(54, 30, "Shriyash Sahu (24BET10001)")
                self.line(54, 42, 8.5 * inch - 54, 42)
                self.restoreState()
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

def build_pdf():
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    primary_color = colors.HexColor('#003366')
    secondary_color = colors.HexColor('#2E6B9E')

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=primary_color,
        alignment=1,
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=secondary_color,
        alignment=1,
        spaceAfter=30
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=primary_color,
        spaceBefore=16,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=secondary_color,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#222222'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=15,
        spaceAfter=4
    )

    caption_style = ParagraphStyle(
        'Caption_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#555555'),
        alignment=1,
        spaceBefore=4,
        spaceAfter=10
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#111111'),
        backColor=colors.HexColor('#F5F5F5'),
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=8
    )

    story = []

    # ══════════════════════════════════════════════════════════════════════════════
    # COVER PAGE
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Spacer(1, 1.2 * inch))
    story.append(Paragraph("CET3001 – Educational Data Mining<br/>and Learning Analytics", title_style))
    story.append(Paragraph("LABORATORY PRACTICAL REPORT", subtitle_style))
    story.append(HRFlowable(width="80%", thickness=2, color=primary_color, spaceBefore=10, spaceAfter=30))

    meta_data = [
        [Paragraph("<b>Course Code:</b>", body_style), Paragraph("CET3001", body_style)],
        [Paragraph("<b>Subject:</b>", body_style), Paragraph("Educational Data Mining and Learning Analytics", body_style)],
        [Paragraph("<b>Practical Number:</b>", body_style), Paragraph("01", body_style)],
        [Paragraph("<b>Practical Title:</b>", body_style), Paragraph("Exploratory Data Analysis of Student Performance", body_style)],
        [Paragraph("<b>Student Name:</b>", body_style), Paragraph("SHRIYASH SAHU", body_style)],
        [Paragraph("<b>Registration Number:</b>", body_style), Paragraph("24BET10001", body_style)],
        [Paragraph("<b>Primary Platform:</b>", body_style), Paragraph("TensorFlow Playground (Simulation)", body_style)],
        [Paragraph("<b>Dataset Source:</b>", body_style), Paragraph("UCI Machine Learning Repository (student-mat.csv)", body_style)],
        [Paragraph("<b>Academic Term:</b>", body_style), Paragraph("November 2026", body_style)],
    ]

    meta_table = Table(meta_data, colWidths=[2.2 * inch, 4.3 * inch])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, primary_color),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))

    story.append(meta_table)
    story.append(Spacer(1, 1.5 * inch))
    story.append(Paragraph("<b>Department of Computer Science & Engineering</b>", ParagraphStyle('Inst', parent=body_style, alignment=1, fontSize=11, fontName='Helvetica-Bold')))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════════
    # 1. AIM
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("1. AIM", h1_style))
    story.append(Paragraph(
        "To conduct a rigorous Exploratory Data Analysis (EDA) on the UCI Student Performance benchmark dataset "
        "(<code>student-mat.csv</code>), compute descriptive statistics (mean, median, mode, variance, standard deviation, "
        "interquartile ranges, skewness, kurtosis), generate distribution and correlation visualizations, isolate outliers "
        "using Tukey's IQR fences, conduct neural network simulation experiments on the TensorFlow Playground platform, "
        "and implement an additional Multi-Layer Perceptron (MLP) classifier for pass/fail prediction while preventing target leakage.",
        body_style
    ))

    # ══════════════════════════════════════════════════════════════════════════════
    # 2. APPARATUS / TOOLS REQUIRED
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("2. APPARATUS / TOOLS REQUIRED", h1_style))
    tools_data = [
        [Paragraph("<b>Category</b>", body_style), Paragraph("<b>Specification / Tools</b>", body_style)],
        [Paragraph("Operating System", body_style), Paragraph("macOS (Darwin 25.1.0)", body_style)],
        [Paragraph("Programming Language", body_style), Paragraph("Python 3.12+ (Anaconda / Virtual Environment)", body_style)],
        [Paragraph("IDE / Notebook", body_style), Paragraph("Jupyter Notebook / Google Colab / Visual Studio Code", body_style)],
        [Paragraph("Primary Simulation Platform", body_style), Paragraph("TensorFlow Playground (https://playground.tensorflow.org/)", body_style)],
        [Paragraph("Dataset", body_style), Paragraph("UCI Student Performance (student-mat.csv, 395 records × 33 attributes)", body_style)],
        [Paragraph("Dataset Source", body_style), Paragraph("https://archive.ics.uci.edu/dataset/320/student+performance", body_style)],
        [Paragraph("Core Data Libraries", body_style), Paragraph("pandas (v3.1.1), numpy (v2.2.5), scipy (v1.16.1)", body_style)],
        [Paragraph("Visualization Suite", body_style), Paragraph("matplotlib (v3.10.1), seaborn (v0.13.2)", body_style)],
        [Paragraph("Machine Learning Framework", body_style), Paragraph("scikit-learn (v1.6.1) – MLPClassifier, StandardScaler", body_style)],
        [Paragraph("Browser Automation", body_style), Paragraph("Google Chrome (v137), Puppeteer-core (v24)", body_style)],
    ]
    tools_table = Table(tools_data, colWidths=[2.2 * inch, 4.3 * inch])
    tools_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F8FAFC'), colors.white]),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(tools_table)
    story.append(Spacer(1, 10))

    # ══════════════════════════════════════════════════════════════════════════════
    # 3. THEORY
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("3. THEORY", h1_style))
    story.append(Paragraph("3.1 Exploratory Data Analysis (EDA) in Educational Mining", h2_style))
    story.append(Paragraph(
        "Exploratory Data Analysis (EDA), formalised by John Tukey (1977), is an empirical investigation process that uses statistical summaries "
        "and graphical methods to uncover underlying data structures, detect anomalies, test foundational hypotheses, and assess quality without "
        "premature parametric assumptions. In Educational Data Mining (EDM), EDA identifies critical predictors of academic attrition, detects "
        "bimodal achievement distributions, isolates systemic absenteeism patterns, and guides the architecture of early-warning decision models.",
        body_style
    ))

    story.append(Paragraph("3.2 Descriptive Statistics & Formulations", h2_style))
    story.append(Paragraph("<b>Arithmetic Mean:</b> Central balance point of numerical observations:", body_style))
    story.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;<b>x̄ = (1 / n) · ∑<sub>i=1</sub><sup>n</sup> x<sub>i</sub></b>", code_style))
    story.append(Paragraph("<b>Sample Variance & Standard Deviation:</b> Measure of dispersion around the mean:", body_style))
    story.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;<b>s² = [1 / (n - 1)] · ∑<sub>i=1</sub><sup>n</sup> (x<sub>i</sub> - x̄)², &nbsp;&nbsp;&nbsp; s = √(s²)</b>", code_style))
    story.append(Paragraph("<b>Interquartile Range (IQR):</b> Robust spread resistant to extreme outliers, spanning the central 50%:", body_style))
    story.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;<b>IQR = Q₃ - Q₁</b>, &nbsp; where Q₁ = 25th percentile, Q₃ = 75th percentile.", code_style))
    story.append(Paragraph("<b>Sample Skewness & Excess Kurtosis:</b> Characterize distribution asymmetry and tail weight:", body_style))
    story.append(Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;<b>Skewness = [n / ((n-1)(n-2))] · ∑ [(x<sub>i</sub> - x̄) / s]³</b><br/>"
                           "&nbsp;&nbsp;&nbsp;&nbsp;<b>Kurtosis = [n(n+1)/((n-1)(n-2)(n-3))] · ∑ [(x<sub>i</sub> - x̄)/s]⁴ - [3(n-1)²/((n-2)(n-3))]</b>", code_style))

    story.append(Paragraph("3.3 Pearson Product-Moment Correlation", h2_style))
    story.append(Paragraph(
        "Measures linear dependence between pairs of continuous random variables (X, Y) within range [-1, +1]:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>r<sub>XY</sub> = ∑ (x<sub>i</sub> - x̄)(y<sub>i</sub> - ȳ) / [ √(∑(x<sub>i</sub> - x̄)²) · √(∑(y<sub>i</sub> - ȳ)²) ]</b>",
        code_style
    ))

    story.append(Paragraph("3.4 Tukey's IQR Outlier Detection Fence", h2_style))
    story.append(Paragraph(
        "Observations outside the inner fences [Q₁ - 1.5·IQR, Q₃ + 1.5·IQR] are classified as potential outliers. "
        "In educational data, outliers must be substantively evaluated: genuine dropouts (G3 = 0) and high absenteeism "
        "carry critical policy insights and should not be blindly discarded.",
        body_style
    ))

    story.append(Paragraph("3.5 Multi-Layer Perceptron (MLP) Classifier Theory", h2_style))
    story.append(Paragraph(
        "An Artificial Neural Network mapping 30 input features across two hidden layers (64, 32) to a binary output (Pass/Fail). "
        "Activation function is Rectified Linear Unit (ReLU): <b>f(z) = max(0, z)</b>. Optimization utilizes Adam with Binary Cross-Entropy Loss:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>L = - (1/n) · ∑ [ y<sub>i</sub> log(ŷ<sub>i</sub>) + (1 - y<sub>i</sub>) log(1 - ŷ<sub>i</sub>) ]</b>",
        code_style
    ))
    story.append(Paragraph(
        "Evaluation metrics: Accuracy = (TP + TN)/(P + N); Precision = TP/(TP + FP); Recall = TP/(TP + FN); F1 = 2·(P·R)/(P + R).",
        body_style
    ))

    story.append(Paragraph("3.6 TensorFlow Playground Simulation Principles", h2_style))
    story.append(Paragraph(
        "TensorFlow Playground simulates real-time backpropagation on 2D synthetic datasets (Circle, XOR, Gaussian, Spiral). "
        "It visually demonstrates how hidden layers and non-linear activation functions bend linear hyperplanes into complex "
        "decision manifolds. Synthetic 2D data is distinguished from multi-attribute tabular educational datasets.",
        body_style
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════════
    # 4. METHODOLOGY / PROCEDURE
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("4. METHODOLOGY / PROCEDURE", h1_style))
    proc_steps = [
        "<b>Dataset Acquisition:</b> Download official UCI Student Performance archive; extract <code>student-mat.csv</code>.",
        "<b>Data Loading & Structure Verification:</b> Read CSV using semicolon delimiter (<code>sep=';'</code>); verify 395 records and 33 attributes.",
        "<b>Data Quality Audit:</b> Execute <code>isnull().sum()</code> and <code>duplicated().sum()</code> to confirm zero missing entries and zero duplicate rows.",
        "<b>Attribute Typing:</b> Partition columns into 16 numerical features and 17 categorical attributes.",
        "<b>Descriptive Statistical Computation:</b> Calculate central tendency, dispersion, quartiles, IQR, skewness, and kurtosis across studytime, failures, absences, G1, G2, G3.",
        "<b>Exploratory Visualizations:</b> Render G3 histogram with mean/median markers, G3 boxplot, multi-variable boxplots, studytime violin plots, G1/G2 vs G3 scatter plots with regression trendlines, and a complete correlation heatmap.",
        "<b>IQR Outlier Identification:</b> Calculate upper and lower fences; isolate and analyze outliers across seven key attributes.",
        "<b>Platform Simulation (TensorFlow Playground):</b> Access playground.tensorflow.org via headless Chrome; inspect DOM; execute live training for Circle (ReLU, 2 layers) and Spiral (Tanh, 3 layers, 7 features); log loss and epoch progression; capture genuine viewport screenshots.",
        "<b>ML Extension (MLP Classification):</b> Establish binary target (Pass: G3 ≥ 10); exclude G1/G2 to prevent target leakage; encode categoricals; perform 80/20 stratified split; scale features strictly on training fold; fit MLPClassifier; extract confusion matrix, classification report, loss curve, and permutation importances.",
    ]
    for idx, s in enumerate(proc_steps, 1):
        story.append(Paragraph(f"{idx}. {s}", bullet_style))

    story.append(Spacer(1, 15))

    # ══════════════════════════════════════════════════════════════════════════════
    # 5. ALGORITHM & ARCHITECTURE
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("5. ALGORITHM, ARCHITECTURE & WORKFLOW", h1_style))
    story.append(Paragraph("5.1 End-to-End Pipeline Workflow", h2_style))
    story.append(Paragraph(
        "<b>Raw Dataset</b> → <b>Delimiter Parsing</b> → <b>Data Integrity Audit</b> → "
        "<b>Descriptive Statistics Extraction</b> → <b>Multi-variable Visualizations</b> → "
        "<b>IQR Outlier Isolation</b> → <b>Neural Simulation (TF Playground)</b> → "
        "<b>Non-leaking MLP Classifier</b> → <b>Evaluation & Reporting</b>",
        code_style
    ))

    story.append(Paragraph("5.2 MLP Classifier Architecture", h2_style))
    story.append(Paragraph(
        "• <b>Input Layer:</b> 30 features (13 scaled numerical + 17 label-encoded socio-demographic features)<br/>"
        "• <b>Hidden Layer 1:</b> 64 fully connected units, ReLU activation: <i>a₁ = max(0, W₁x + b₁)</i><br/>"
        "• <b>Hidden Layer 2:</b> 32 fully connected units, ReLU activation: <i>a₂ = max(0, W₂a₁ + b₂)</i><br/>"
        "• <b>Output Layer:</b> 1 unit, Logistic Sigmoid activation: <i>ŷ = σ(W₃a₂ + b₃)</i><br/>"
        "• <b>Regularization & Convergence:</b> Early stopping with 15% validation split, patience = 20 iterations.",
        body_style
    ))
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════════
    # 6. PROGRAM IMPLEMENTATION SUMMARY
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("6. PROGRAM / IMPLEMENTATION", h1_style))
    story.append(Paragraph(
        "The complete, verified, standalone Python source code is provided in <code>code/practical01_eda.py</code> "
        "and mirrored as an interactive notebook in <code>code/Practical01_EDA_StudentPerformance.ipynb</code>. "
        "Key operational code segments are highlighted below:",
        body_style
    ))

    story.append(Paragraph("<b>Snippet 1: Data Loading & Verification</b>", body_style))
    story.append(Paragraph(
        "df = pd.read_csv('../data/student-mat.csv', sep=';')<br/>"
        "assert df.isnull().sum().sum() == 0, 'Missing values detected'<br/>"
        "num_cols = df.select_dtypes(include=[np.number]).columns.tolist()",
        code_style
    ))

    story.append(Paragraph("<b>Snippet 2: Target Leakage Prevention & MLP Fitting</b>", body_style))
    story.append(Paragraph(
        "df['pass_fail'] = (df['G3'] >= 10).astype(int)<br/>"
        "# Exclude G1 and G2 to prevent trivial target leakage<br/>"
        "X = df_ml.drop(columns=['G1', 'G2', 'G3', 'pass_fail'])<br/>"
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)<br/>"
        "scaler = StandardScaler()<br/>"
        "X_train_s = scaler.fit_transform(X_train)<br/>"
        "X_test_s = scaler.transform(X_test)<br/>"
        "mlp = MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', solver='adam', max_iter=500, early_stopping=True)",
        code_style
    ))
    story.append(Spacer(1, 10))

    # ══════════════════════════════════════════════════════════════════════════════
    # 7. OUTPUT / SIMULATION RESULTS
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("7. OUTPUT / SIMULATION", h1_style))

    story.append(Paragraph("7.1 Computed Descriptive Statistics Table", h2_style))
    stats_data = [
        ["Statistic", "studytime", "failures", "absences", "G1", "G2", "G3"],
        ["Mean", "2.0354", "0.3342", "5.7089", "10.9089", "10.7139", "10.4152"],
        ["Median", "2.0000", "0.0000", "4.0000", "11.0000", "11.0000", "11.0000"],
        ["Mode", "2", "0", "0", "10", "9", "10"],
        ["Std Dev", "0.8392", "0.7437", "8.0031", "3.3192", "3.7615", "4.5814"],
        ["Variance", "0.7043", "0.5530", "64.0495", "11.0171", "14.1489", "20.9896"],
        ["Min", "1", "0", "0", "3", "0", "0"],
        ["Max", "4", "3", "75", "19", "19", "20"],
        ["Q1 (25%)", "1.0", "0.0", "0.0", "8.0", "9.0", "8.0"],
        ["Q3 (75%)", "2.0", "0.0", "8.0", "13.0", "13.0", "14.0"],
        ["IQR", "1.0", "0.0", "8.0", "5.0", "4.0", "6.0"],
        ["Skewness", "0.6321", "2.3870", "3.6716", "0.2406", "-0.4316", "-0.7327"],
        ["Kurtosis", "-0.0144", "5.0047", "21.7191", "-0.6938", "0.6277", "0.4034"],
    ]
    t_stats = Table(stats_data, colWidths=[1.1 * inch, 0.9 * inch, 0.9 * inch, 0.9 * inch, 0.9 * inch, 0.9 * inch, 0.9 * inch])
    t_stats.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), primary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F8FAFC'), colors.white]),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_stats)
    story.append(Spacer(1, 10))

    story.append(Paragraph("7.2 IQR Outlier Detection Summary", h2_style))
    outlier_table_data = [
        ["Variable", "Q1", "Q3", "IQR", "Lower", "Upper", "Outlier Count", "Outlier %"],
        ["absences", "0.0", "8.0", "8.0", "-12.0", "20.0", "15", "3.8%"],
        ["G1", "8.0", "13.0", "5.0", "0.5", "20.5", "0", "0.0%"],
        ["G2", "9.0", "13.0", "4.0", "3.0", "19.0", "13", "3.3%"],
        ["G3", "8.0", "14.0", "6.0", "-1.0", "23.0", "0", "0.0%"],
        ["failures", "0.0", "0.0", "0.0", "0.0", "0.0", "83", "21.0%"],
        ["age", "16.0", "18.0", "2.0", "13.0", "21.0", "1", "0.3%"],
        ["studytime", "1.0", "2.0", "1.0", "-0.5", "3.5", "27", "6.8%"],
    ]
    t_outlier = Table(outlier_table_data, colWidths=[1.1 * inch, 0.7 * inch, 0.7 * inch, 0.7 * inch, 0.8 * inch, 0.8 * inch, 0.9 * inch, 0.8 * inch])
    t_outlier.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), secondary_color),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_outlier)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════════
    # 7.3 EMBEDDED VISUALIZATIONS
    # ══════════════════════════════════════════════════════════════════════════════
    def add_plot(img_name, caption, w=5.5*inch, h=2.8*inch):
        p = os.path.join(OUTPUT_DIR, img_name)
        if not os.path.exists(p):
            p = os.path.join(SCREENSHOT_DIR, img_name)
        if os.path.exists(p):
            story.append(Image(p, width=w, height=h))
            story.append(Paragraph(caption, caption_style))
            story.append(Spacer(1, 4))

    story.append(Paragraph("7.3 Exploratory Data Visualizations", h2_style))
    add_plot('fig01_histogram_G3.png', "Figure 1: Distribution of Final Grades (G3) showing Mean (10.42) and Median (11.00)")
    add_plot('fig02_boxplot_G3.png', "Figure 2: Box Plot of Final Grades (G3) displaying Quartiles and Whiskers", h=2.0*inch)
    story.append(PageBreak())

    add_plot('fig03_boxplots_key_vars.png', "Figure 3: Comparative Box Plots across Key Numerical Variables", h=3.2*inch)
    add_plot('fig04_studytime_vs_G3.png', "Figure 4: Study Time vs Final Grade (G3) – Mean Bar Chart and Violin Distributions", h=2.5*inch)
    story.append(PageBreak())

    add_plot('fig05_scatter_G1_vs_G3.png', "Figure 5: Scatter Plot of G1 vs G3 with Fitted Linear Regression (r = 0.801, p < 0.001)", h=2.8*inch)
    add_plot('fig06_scatter_G2_vs_G3.png', "Figure 6: Scatter Plot of G2 vs G3 showing Extreme Predictive Linearity (r = 0.905)", h=2.8*inch)
    story.append(PageBreak())

    add_plot('fig07_correlation_heatmap.png', "Figure 7: Full Correlation Heatmap of All 16 Numerical Variables", w=5.8*inch, h=3.8*inch)
    add_plot('fig08_outlier_detection.png', "Figure 8: Outlier Detection Scatter Plots with Upper and Lower Tukey Fences", w=5.8*inch, h=3.0*inch)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════════
    # 7.4 TENSORFLOW PLAYGROUND SIMULATION
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("7.4 TensorFlow Playground Live Simulation Results", h1_style))
    story.append(Paragraph(
        "Direct headless Chrome automation was executed against the official web simulator (playground.tensorflow.org). "
        "Below are the verified screenshots and training metrics captured directly from the live DOM canvas.",
        body_style
    ))

    add_plot('tf_playground_default.png', "Figure 15: TensorFlow Playground – Default Interface and Feature Palette", w=5.8*inch, h=2.9*inch)
    add_plot('tf_playground_circle_trained.png', "Figure 16: Circle Dataset – Trained Model at Epoch 302 (Test Loss: 0.002, Train Loss: 0.001)", w=5.8*inch, h=2.9*inch)
    story.append(PageBreak())

    add_plot('tf_playground_spiral_trained.png', "Figure 17: Spiral Dataset – Trained Model at Epoch 484 (Test Loss: 0.002, Train Loss: 0.001)", w=5.8*inch, h=2.9*inch)

    story.append(Paragraph("7.5 Real-Data MLP Classifier Results (Pass/Fail)", h2_style))
    story.append(Paragraph(
        "<b>Dataset Partition:</b> 316 training instances, 79 test instances (80/20 stratified split).<br/>"
        "<b>Overall Accuracy:</b> <b>64.56%</b> (without intermediate grade leakage).<br/>"
        "<b>Pass Class Metrics:</b> Precision = 0.6761, Recall = 0.9057, F1-Score = 0.7742 (Support: 53).<br/>"
        "<b>Fail Class Metrics:</b> Precision = 0.3800, Recall = 0.1200, F1-Score = 0.1800 (Support: 26).<br/>"
        "<b>Confusion Matrix Counts:</b> TP = 48, TN = 3, FP = 23, FN = 5.",
        body_style
    ))
    add_plot('fig12_confusion_matrix.png', "Figure 12: Confusion Matrix of the Non-leaking MLP Classifier", w=4.5*inch, h=2.6*inch)
    add_plot('fig13_training_loss.png', "Figure 13: MLP Training Loss Curve and Early-Stopping Convergence", w=4.8*inch, h=2.4*inch)
    story.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════════
    # 8. RESULTS AND INTERPRETATION
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("8. RESULTS AND INTERPRETATION", h1_style))
    story.append(Paragraph("8.1 Statistical Distribution Interpretation", h2_style))
    story.append(Paragraph(
        "The distribution of final grades (G3) yields a mean of 10.42 with substantial standard deviation (4.58). "
        "A critical finding is the left-skewness (skewness = -0.7327) caused by 38 students scoring exactly zero. "
        "In educational context, this bimodal drop represents administrative exam non-attendance or dropouts rather "
        "than continuous academic deficiency.",
        body_style
    ))

    story.append(Paragraph("8.2 Correlation & Academic Trajectory", h2_style))
    story.append(Paragraph(
        "The correlation hierarchy demonstrates that prior academic performance overwhelmingly dictates final outcomes: "
        "G2 (r = 0.905) and G1 (r = 0.801). Among non-grade features, previous class failures exhibit the strongest negative "
        "association (r = -0.360). Parental education correlates positively (Medu: r = 0.217; Fedu: r = 0.152), indicating "
        "subtle socio-economic advantages. Alcohol consumption (Dalc/Walc) and absences show negligible direct correlation with final grades, "
        "suggesting their effects are mediated through cumulative failure events.",
        body_style
    ))

    story.append(Paragraph("8.3 Outlier Assessment & Retention Decisions", h2_style))
    story.append(Paragraph(
        "• <b>Absences:</b> 15 outliers (values up to 75) represent chronic absenteeism. Retained because removing them masks high-risk populations.<br/>"
        "• <b>Failures:</b> 83 records flagged by IQR as outliers due to IQR = 0. This is an algorithmic artifact of zero-inflated distributions; all data points are valid.<br/>"
        "• <b>G2 Zeros:</b> 13 students scoring 0 in G2 dropped out or skipped the exam; essential for attrition modeling.",
        body_style
    ))

    story.append(Paragraph("8.4 MLP Classifier Performance & Target Leakage Prevention", h2_style))
    story.append(Paragraph(
        "Excluding G1 and G2 is essential for real-world utility: predicting final grades using period 2 grades achieves artificial ~92% accuracy "
        "but provides zero lead time for intervention. Using socio-demographic features alone, our MLP achieves 64.56% accuracy. "
        "The model achieves 90.57% recall on passing students but suffers from low recall (11.5%) on failing students due to 67:33 class imbalance. "
        "This proves that background features alone are inadequate for early-warning systems and must be complemented with ongoing LMS engagement data.",
        body_style
    ))

    story.append(Paragraph("8.5 Conclusion", h2_style))
    story.append(Paragraph(
        "This experiment successfully executed the entire pipeline of educational exploratory data mining. "
        "Statistical analysis revealed significant predictors and zero-inflation artifacts in student evaluations. "
        "TensorFlow Playground demonstrated neural boundary formation on non-linear manifolds, and our standalone MLP "
        "quantified the realistic predictive limits of pre-course demographic variables.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # ══════════════════════════════════════════════════════════════════════════════
    # 9. REFERENCES
    # ══════════════════════════════════════════════════════════════════════════════
    story.append(Paragraph("9. REFERENCES", h1_style))
    refs = [
        "Cortez, P., & Silva, A. (2008). Using Data Mining to Predict Secondary School Student Performance. <i>Proceedings of the 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008)</i>, pp. 5–12, Porto, Portugal. EUROSIS.",
        "UCI Machine Learning Repository – Student Performance Dataset: https://archive.ics.uci.edu/dataset/320/student+performance",
        "TensorFlow Playground: https://playground.tensorflow.org/",
        "Tukey, J. W. (1977). <i>Exploratory Data Analysis</i>. Addison-Wesley Publishing Company.",
        "Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. <i>Journal of Machine Learning Research</i>, 12, 2825–2830.",
        "Romero, C., & Ventura, S. (2020). Educational Data Mining and Learning Analytics: An updated survey. <i>WIREs Data Mining and Knowledge Discovery</i>, 10(3), e1355.",
        "Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. <i>Computing in Science & Engineering</i>, 9(3), 90–95."
    ]
    for r in refs:
        story.append(Paragraph(r, bullet_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated at: {PDF_PATH}")

if __name__ == '__main__':
    build_pdf()
