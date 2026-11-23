# Module 04: Outlier Detection via Tukey's IQR Fences

## 1. What is an Outlier in Educational Data Mining?

An outlier is an empirical observation that deviates significantly from the remaining members of the sample in which it occurs. In traditional statistics, outliers are often viewed as measurement noise or transcription errors to be eliminated. 

However, in **Educational Data Mining**, an outlier often represents the **most policy-relevant student**:
* A student with 75 absences who still passes.
* An otherwise capable student who drops out suddenly ($G1=14 \to G3=0$).
* A chronically failing student needing immediate psychological or academic counseling.

Blindly deleting outliers would introduce **survivorship bias** into your dataset!

---

## 2. Mathematical Definition of Tukey's Fences

John Tukey (1977) formulated non-parametric inner and outer fences based on the sample quartiles ($Q_1$ and $Q_3$):

1. **Calculate the First Quartile ($Q_1$):** 25th percentile.
2. **Calculate the Third Quartile ($Q_3$):** 75th percentile.
3. **Compute the Interquartile Range ($IQR$):**
   $$IQR = Q_3 - Q_1$$
4. **Establish Tukey's Fences:**
   $$\text{Lower Bound} = Q_1 - 1.5 \times IQR$$
   $$\text{Upper Bound} = Q_3 + 1.5 \times IQR$$
5. **Classification Rule:** Any observation $x_i$ satisfying $x_i < \text{Lower Bound}$ or $x_i > \text{Upper Bound}$ is flagged as a potential outlier.

---

## 3. Outlier Summary Table

The following results were computed by `practical01_eda.py` across the cohort of 395 students:

| Variable | $Q_1$ | $Q_3$ | $IQR$ | Lower Bound | Upper Bound | Outlier Count | Percentage |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`absences`** | 0.0 | 8.0 | 8.0 | -12.00 | 20.00 | **15** | **3.8%** |
| **`G1` (Period 1)** | 8.0 | 13.0 | 5.0 | 0.50 | 20.50 | **0** | **0.0%** |
| **`G2` (Period 2)** | 9.0 | 13.0 | 4.0 | 3.00 | 19.00 | **13** | **3.3%** |
| **`G3` (Final)** | 8.0 | 14.0 | 6.0 | -1.00 | 23.00 | **0** | **0.0%** |
| **`failures`** | 0.0 | 0.0 | 0.0 | 0.00 | 0.00 | **83** | **21.0%** |
| **`age`** | 16.0 | 18.0 | 2.0 | 13.00 | 21.00 | **1** | **0.3%** |
| **`studytime`** | 1.0 | 2.0 | 1.0 | -0.50 | 3.50 | **27** | **6.8%** |

---

## 4. Substantive Analysis of Outlier Categories

### 4.1 The Chronic Absenteeism Group (`absences`)
* **Calculated Fences:** Lower = -12.0, Upper = 20.0.
* **Outliers Found:** Exactly 15 students exceeded 20 absences.
* **Exact Outlier Values:** $[21, 22, 22, 22, 23, 24, 25, 26, 28, 30, 38, 40, 54, 56, 75]$.
* **Assessment:** These numbers reflect real-world medical issues, chronic disengagement, or familial obligations.
* **Retention Recommendation:** **RETAIN.** Removing these records would artificially inflate attendance statistics and prevent early-warning models from recognizing patterns associated with severe truancy.

---

### 4.2 The Zero-Inflation Artifact (`failures`)
* **Calculated Fences:** Because over 66% of students have 0 past class failures, $Q_1 = 0$ and $Q_3 = 0$.
  $$IQR = 0.0 - 0.0 = 0.0$$
  $$\text{Upper Bound} = 0.0 + 1.5(0.0) = 0.0$$
* **Algorithmic Outcome:** Any student with failures $> 0$ (i.e., 1, 2, or 3 past failures) is mathematically classified as an outlier (83 students, 21.0%).
* **Assessment:** This is a classic **statistical artifact** caused by applying continuous boxplot algorithms to a discrete, zero-inflated integer count.
* **Retention Recommendation:** **DO NOT TREAT AS OUTLIERS.** Having 1 to 3 past failures is a natural and highly predictive characteristic of at-risk students ($r = -0.360$ with final grades). Deleting 21% of the cohort would destroy the model's ability to identify students in need of academic remediation.

---

### 4.3 The Dropout Phenotype (`G2 = 0`)
* **Calculated Fences:** Lower = 3.0, Upper = 19.0.
* **Outliers Found:** Exactly 13 students.
* **Outlier Values:** Every single outlier has $G2 = 0$.
* **Assessment:** In Portuguese secondary schools, grades are integers between 0 and 20. Scoring 0 almost always corresponds to non-attendance or course withdrawal before the second evaluation period.
* **Retention Recommendation:** **FLAG BUT RETAIN.** These records provide vital training signal for dropout forecasting.
