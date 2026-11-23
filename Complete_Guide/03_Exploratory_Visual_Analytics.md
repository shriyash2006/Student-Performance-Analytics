# Module 03: Exploratory Visual Analytics

## 1. Role of Visualization in Educational Mining

While summary tables condense numbers, graphical visualization reveals non-linear trends, cluster separations, multi-modal densities, and heteroscedasticity that summary statistics often mask.

In this practical, 14 high-resolution figures were generated in `outputs/` using `matplotlib` and `seaborn`.

---

## 2. In-Depth Breakdown of Key Visualizations

### Figure 1: Distribution of Final Grades (`G3`) — Histogram
* **File:** `outputs/fig01_histogram_G3.png`
* **Plot Type:** Frequency Histogram with 21 unit-width bins (range $-0.5$ to $20.5$) with overlaid vertical markers for Mean ($\bar{x} = 10.42$) and Median ($Q_2 = 11.00$).
* **Visual Insight:**
  * Rather than forming a pure Gaussian distribution, the histogram reveals **two distinct components**:
    1. A relatively normal distribution centered between grades 8 and 15 (representing active test-takers).
    2. An isolated, high-frequency spike at **$G3 = 0$ containing exactly 38 students (9.6% of the cohort)**.
  * **Educational Meaning:** Students scoring 0 did not simply fail marginally; they suffered from severe administrative absence, dropped out before the exam, or were disqualified.

---

### Figure 2: Box Plot of Final Grades (`G3`)
* **File:** `outputs/fig02_boxplot_G3.png`
* **Plot Type:** Horizontal Tukey Box Plot displaying $Q_1$, Median, $Q_3$, and Whiskers.
* **Visual Insight:**
  * $Q_1 = 8.0$, $\text{Median} = 11.0$, $Q_3 = 14.0$, yielding $IQR = 6.0$.
  * Whiskers extend to the minimum ($0$) and maximum ($20$).
  * Notice that **no individual points are plotted beyond the whiskers**. Because $1.5 \times IQR = 9.0$, the lower fence is $8 - 9 = -1$ and upper fence is $14 + 9 = 23$. Since all valid grades lie within $[0, 20]$, the IQR method identifies zero formal outliers in $G3$.

---

### Figure 3: Comparative Box Plots of Key Variables
* **File:** `outputs/fig03_boxplots_key_vars.png`
* **Plot Type:** $2 \times 3$ subplot grid comparing `studytime`, `failures`, `absences`, `G1`, `G2`, and `G3`.
* **Visual Insight:**
  * Clearly contrasts variables with healthy spreads (`G1`, `G2`, `G3`) against heavily compressed, zero-inflated variables (`failures` and `absences`).
  * In `absences`, multiple points stretch out between 20 and 75, visually highlighting the long right tail.

---

### Figure 4: Study Time vs. Final Grade (`G3`) — Bar Chart & Violin Plot
* **File:** `outputs/fig04_studytime_vs_G3.png`
* **Plot Type:** Side-by-side comparative analysis:
  * **Left:** Mean $G3$ by Study Time category ($<2$ hrs: 10.05; $2–5$ hrs: 10.17; $5–10$ hrs: 12.05; $>10$ hrs: 11.26).
  * **Right:** Violin plot demonstrating kernel density distributions per study-time tier.
* **Visual Insight:**
  * While studying 5–10 hours yields higher average performance (12.05), studying $>10$ hours exhibits diminishing returns (11.26) and contains students with wide variance.
  * **Educational Meaning:** Study time alone has a weak linear correlation ($r = 0.098$). Quality of study, baseline prerequisite knowledge, and cognitive ability matter far more than raw hours spent.

---

### Figure 5 & 6: Scatter Plots of Period Grades ($G1 \to G3$ and $G2 \to G3$)
* **Files:** `outputs/fig05_scatter_G1_vs_G3.png`, `outputs/fig06_scatter_G2_vs_G3.png`
* **Plot Type:** Bivariate scatter plots with fitted Ordinary Least Squares (OLS) linear trendlines and Pearson correlation coefficients.
* **Visual Insight:**
  * **$G1 \to G3$:** Trendline $G3 = 1.11 \cdot G1 - 1.65$ with $r = 0.801$ ($p < 0.001$).
  * **$G2 \to G3$:** Trendline $G3 = 1.10 \cdot G2 - 1.39$ with $r = 0.905$ ($p < 0.001$).
  * Points cluster tightly along the regression diagonal. A distinct horizontal line of points at $G3 = 0$ highlights students who performed adequately in $G1$ or $G2$ but dropped out before $G3$.

---

### Figure 7: Correlation Heatmap (All 16 Continuous Attributes)
* **File:** `outputs/fig07_correlation_heatmap.png`
* **Plot Type:** Lower-triangular correlation matrix heatmap with diverging RdBu color scale and annotated Pearson coefficients.

#### Key Pearson Correlation Findings with Final Grade ($G3$):
| Correlated Attribute | Correlation $r$ | Magnitude & Interpretation |
|:---|:---:|:---|
| **`G2` (Period 2 Grade)** | **+0.905** | Very strong positive linear relationship |
| **`G1` (Period 1 Grade)** | **+0.801** | Strong positive linear relationship |
| **`Medu` (Mother's Education)** | **+0.217** | Weak positive protective factor |
| **`Fedu` (Father's Education)** | **+0.152** | Weak positive protective factor |
| **`studytime`** | **+0.098** | Very weak positive association |
| **`absences`** | **+0.034** | Negligible linear correlation |
| **`Walc` (Weekend Alcohol)** | **-0.052** | Negligible negative correlation |
| **`Dalc` (Workday Alcohol)** | **-0.055** | Negligible negative correlation |
| **`traveltime`** | **-0.117** | Weak negative friction factor |
| **`goout`** | **-0.133** | Weak negative relationship |
| **`age`** | **-0.162** | Weak negative relationship (older students in class often repeated years) |
| **`failures`** | **-0.360** | **Moderate negative correlation (Top non-grade impediment)** |

---

### Figures 8–11: Additional Exploratory Visualizations
* **`fig08_outlier_detection.png`:** Multi-panel scatter plots mapping every student observation against upper and lower Tukey fences.
* **`fig09_grade_comparison.png`:** Overlaid histograms of $G1, G2, G3$ demonstrating how grade distributions evolve over time.
* **`fig10_pairplot.png`:** High-dimensional pairwise relationship matrix showing joint distributions between grades, failures, and study time.
* **`fig11_gender_grades.png`:** Boxplot split by student gender showing comparable medians ($11$ for females vs $11$ for males).
