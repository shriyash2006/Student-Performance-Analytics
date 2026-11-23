# Module 02: Descriptive Statistics & Mathematical Formulations

## 1. Overview of Statistical Metrics

Descriptive statistics summarize and characterize the fundamental features of a dataset without fitting a predictive model. In Educational Data Mining, this step reveals:
1. **Central Tendency:** The typical performance level of the student cohort.
2. **Dispersion & Variability:** The inequality or spread in academic achievements and absenteeism.
3. **Distribution Shape:** Asymmetries (skewness) and outlier tail weights (kurtosis).

---

## 2. Mathematical Formulations

### 2.1 Central Tendency

#### Arithmetic Mean ($\bar{x}$)
The primary measure of central location, computed as the sum of all observations divided by the sample size $n$:
$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$
* **Pros:** Leverages every data point; mathematically tractable.
* **Cons:** Highly sensitive to extreme outliers (e.g., students with grade $0$ pull the mean downward).

#### Median ($Q_2$)
The middle value when data is arranged in non-decreasing order:
$$\text{Median} = \begin{cases} 
x_{\left(\frac{n+1}{2}\right)} & \text{if } n \text{ is odd} \\
\frac{1}{2} \left( x_{\left(\frac{n}{2}\right)} + x_{\left(\frac{n}{2}+1\right)} \right) & \text{if } n \text{ is even}
\end{cases}$$
* **Pros:** Robust against extreme outliers and skewed distributions.

#### Mode
The value that appears with the highest empirical frequency in the sample:
$$\text{Mode} = \arg\max_{v} \sum_{i=1}^{n} \mathbb{I}(x_i = v)$$

---

### 2.2 Measures of Dispersion & Spread

#### Sample Variance ($s^2$)
Measures the average squared deviation of observations around their mean, with Bessel's correction ($n-1$) for sample unbiasedness:
$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

#### Sample Standard Deviation ($s$)
The square root of sample variance, returning the dispersion back to the original measurement units:
$$s = \sqrt{s^2} = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$

#### Range ($R$)
$$R = x_{\max} - x_{\min}$$

#### Interquartile Range ($IQR$)
The difference between the 75th percentile ($Q_3$) and the 25th percentile ($Q_1$):
$$IQR = Q_3 - Q_1$$
* Measures the spread of the central 50% of the observations. Unlike variance, $IQR$ is completely immune to extreme boundary outliers.

---

### 2.3 Measures of Distribution Shape

#### Sample Skewness ($g_1$)
Quantifies the degree of distribution asymmetry around the sample mean:
$$\text{Skewness} = \frac{n}{(n-1)(n-2)} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{s}\right)^3$$
* $\text{Skewness} > 0$: **Right-skewed (positive tail)** — Mass of data is on the left; long tail stretches to the right.
* $\text{Skewness} < 0$: **Left-skewed (negative tail)** — Mass of data is on the right; long tail stretches to the left.
* $\text{Skewness} \approx 0$: Symmetric distribution.

#### Sample Excess Kurtosis ($g_2$)
Measures tail heaviness and peakedness relative to a standard normal distribution (which has kurtosis of $0$):
$$\text{Kurtosis} = \left[ \frac{n(n+1)}{(n-1)(n-2)(n-3)} \sum_{i=1}^{n} \left(\frac{x_i - \bar{x}}{s}\right)^4 \right] - \frac{3(n-1)^2}{(n-2)(n-3)}$$
* $\text{Kurtosis} > 0$: **Leptokurtic** (sharp central peak, heavy outlier tails).
* $\text{Kurtosis} < 0$: **Platykurtic** (broad, flat distribution, lighter tails).
* $\text{Kurtosis} \approx 0$: **Mesokurtic** (normal tail thickness).

---

## 3. Verified Empirical Results Table

The script executed `pandas`, `scipy.stats`, and `numpy` across all 395 records. Below are the verified metrics for the key educational variables:

| Variable | Mean | Median | Mode | Variance | Std Dev | Min | Max | Q1 | Q3 | IQR | Skewness | Kurtosis |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`studytime`** | 2.0354 | 2.0000 | 2 | 0.7043 | 0.8392 | 1 | 4 | 1.0 | 2.0 | 1.0 | +0.6321 | -0.0144 |
| **`failures`** | 0.3342 | 0.0000 | 0 | 0.5530 | 0.7437 | 0 | 3 | 0.0 | 0.0 | 0.0 | +2.3870 | +5.0047 |
| **`absences`** | 5.7089 | 4.0000 | 0 | 64.0495 | 8.0031 | 0 | 75 | 0.0 | 8.0 | 8.0 | +3.6716 | +21.7191 |
| **`G1` (Period 1)** | 10.9089 | 11.0000 | 10 | 11.0171 | 3.3192 | 3 | 19 | 8.0 | 13.0 | 5.0 | +0.2406 | -0.6938 |
| **`G2` (Period 2)** | 10.7139 | 11.0000 | 9 | 14.1489 | 3.7615 | 0 | 19 | 9.0 | 13.0 | 4.0 | -0.4316 | +0.6277 |
| **`G3` (Final)** | 10.4152 | 11.0000 | 10 | 20.9896 | 4.5814 | 0 | 20 | 8.0 | 14.0 | 6.0 | -0.7327 | +0.4034 |

---

## 4. In-Depth Interpretation of the Computed Values

### 1. Final Grade (`G3`) Dynamics
* The **Mean is 10.42** while the **Median is 11.00**.
* Notice that the **Skewness is negative (-0.7327)**. In a typical academic bell curve, skewness is close to zero. The negative skew is caused by a discrete cohort of **38 students who scored exactly zero**. These zero-scorers drag the arithmetic mean below the median.
* The variance is high ($s^2 = 20.99, s = 4.58$), spanning grades from $0$ to $20$.

### 2. The Attendance Asymmetry (`absences`)
* `absences` exhibits extreme right-skewness (**+3.67**) and astronomical excess kurtosis (**+21.72**).
* Most students have very low absenteeism (Mode = 0, Median = 4), but the extreme variance ($s^2 = 64.05$) and maximum of $75$ indicate a heavy right tail of chronic absentees.

### 3. The Zero-Inflation Phenomenon (`failures`)
* `failures` has a Median of $0$ and a Mode of $0$.
* Both $Q_1$ and $Q_3$ equal $0.0$, resulting in an **$IQR = 0.0$**.
* This zero-inflation heavily impacts outlier detection algorithms (explained in Module 04).
