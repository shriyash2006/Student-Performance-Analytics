# Module 01: Dataset Architecture & Feature Dictionary

## 1. Overview of the Benchmark Dataset

The dataset utilized for this practical file originates from the **UCI Machine Learning Repository** (Dataset ID: 320) titled **Student Performance Data Set**. Collected by Paulo Cortez and Alice Silva (University of Minho, Portugal) in 2008, it monitors student achievement in secondary education across two Portuguese public institutions:
1. **Gabriel Pereira (GP)**: Urban public school located in Évora.
2. **Mousinho da Silveira (MS)**: Rural/semi-urban secondary school in Portalegre.

Data was gathered using school administrative records (attendance registers, official end-of-period test scores) and structured self-administered questionnaires (evaluating lifestyle, socio-economic factors, parental education, and study habits).

---

## 2. Technical Parsing Details

* **File Format:** Semicolon-delimited ASCII text (`sep=';'`).
* **Record Count:** Exactly **395 rows** (representing individual students enrolled in the core Mathematics curriculum).
* **Attribute Count:** Exactly **33 columns** (30 input features + 3 performance periods: $G1, G2, G3$).
* **Completeness:** Exactly **0 missing/null values** across all columns.
* **Integrity:** Exactly **0 duplicate rows**.

```python
import pandas as pd
df = pd.read_csv('../data/student-mat.csv', sep=';')
assert df.shape == (395, 33)
assert df.isnull().sum().sum() == 0
assert df.duplicated().sum() == 0
```

---

## 3. The 33 Attributes & Categorical Encoding Schema

The attributes are partitioned into four distinct semantic domains:

### Domain A: Target Variable & Prior Academic Performance
The Portuguese secondary education system evaluates students on a **0 to 20 integer continuous grading scale**:
* **`G1` (Numeric: 0 to 20):** First period evaluation (first-term examination grade).
* **`G2` (Numeric: 0 to 20):** Second period evaluation (second-term examination grade).
* **`G3` (Numeric: 0 to 20):** **Final academic grade (Output Target)**. 
  * A grade of **$\ge 10$** represents a passing outcome.
  * A grade of **$< 10$** represents academic failure.

### Domain B: Student Demographics & Institutional Attributes
1. **`school` (Binary):** Student's attending school:
   * `'GP'`: Gabriel Pereira (Count: 349)
   * `'MS'`: Mousinho da Silveira (Count: 46)
2. **`sex` (Binary):** Student's biological sex:
   * `'F'`: Female (Count: 208, 52.7%)
   * `'M'`: Male (Count: 187, 47.3%)
3. **`age` (Numeric: 15 to 22):** Chronological age of the student.
4. **`address` (Binary):** Residential location zone:
   * `'U'`: Urban (Count: 307, 77.7%)
   * `'R'`: Rural (Count: 88, 22.3%)
5. **`famsize` (Binary):** Family household size:
   * `'LE3'`: Less than or equal to 3 members (Count: 114)
   * `'GT3'`: Greater than 3 members (Count: 281)
6. **`Pstatus` (Binary):** Cohabitation status of parents:
   * `'T'`: Living together (Count: 354, 89.6%)
   * `'A'`: Living apart (Count: 41, 10.4%)

### Domain C: Socio-Economic & Family Background
7. **`Medu` (Numeric: 0 to 4):** Mother's educational attainment level:
   * `0`: None (Illiterate)
   * `1`: Primary education (4th grade)
   * `2`: 5th to 9th grade
   * `3`: Secondary education (10th to 12th grade)
   * `4`: Higher education (Undergraduate/Postgraduate)
8. **`Fedu` (Numeric: 0 to 4):** Father's educational attainment level (same 0–4 scale).
9. **`Mjob` (Nominal):** Mother's employment category:
   * `'teacher'`, `'health'` care related, civil `'services'` (police/admin), `'at_home'`, or `'other'`.
10. **`Fjob` (Nominal):** Father's employment category (same 5 categories).
11. **`reason` (Nominal):** Primary reason for selecting the school:
    * Close to `'home'`, school `'reputation'`, `'course'` preference, or `'other'`.
12. **`guardian` (Nominal):** Primary legal guardian:
    * `'mother'`, `'father'`, or `'other'`.
13. **`traveltime` (Numeric: 1 to 4):** Commuting duration from home to school:
    * `1`: $< 15$ min | `2`: $15$ to $30$ min | `3`: $30$ min to $1$ hr | `4`: $> 1$ hr.
14. **`famrel` (Numeric: 1 to 5):** Perceived quality of family relationships:
    * `1`: Very bad $\to$ `5`: Excellent.

### Domain D: Behavioral, Lifestyle & Support Factors
15. **`studytime` (Numeric: 1 to 4):** Weekly dedicated study time:
    * `1`: $< 2$ hours | `2`: $2$ to $5$ hours | `3`: $5$ to $10$ hours | `4`: $> 10$ hours.
16. **`failures` (Numeric: 0 to 3):** Number of previous class failures ($n$ if $1 \le n < 3$, else $3$).
17. **`schoolsup` (Binary: yes/no):** Institutional extra educational support.
18. **`famsup` (Binary: yes/no):** Family educational support or private tutoring provided by family.
19. **`paid` (Binary: yes/no):** Extra paid tutoring classes within the course subject.
20. **`activities` (Binary: yes/no):** Extracurricular athletic or club activities.
21. **`nursery` (Binary: yes/no):** Attended pre-school or nursery school as a child.
22. **`higher` (Binary: yes/no):** Desires to take higher education (Yes: 375, No: 20).
23. **`internet` (Binary: yes/no):** Internet access at home (Yes: 329, No: 66).
24. **`romantic` (Binary: yes/no):** Involved in a romantic relationship (No: 263, Yes: 132).
25. **`freetime` (Numeric: 1 to 5):** Amount of free time available after school (1: Very low $\to$ 5: Very high).
26. **`goout` (Numeric: 1 to 5):** Frequency of going out with social peers (1: Very low $\to$ 5: Very high).
27. **`Dalc` (Numeric: 1 to 5):** Workday alcohol consumption (1: Very low $\to$ 5: Very high).
28. **`Walc` (Numeric: 1 to 5):** Weekend alcohol consumption (1: Very low $\to$ 5: Very high).
29. **`health` (Numeric: 1 to 5):** Current self-reported health status (1: Very bad $\to$ 5: Very good).
30. **`absences` (Numeric: 0 to 75):** Cumulative count of school session absences.

---

## 4. Significance in Educational Data Mining

In educational research, datasets typically suffer from **class imbalance** and **zero-inflated distributions**:
* The pass rate in this cohort is **67.1%** (265 Passed vs 130 Failed), producing a 2:1 ratio.
* Several lifestyle features (`failures`, `absences`, `Dalc`) are heavily clustered near zero or one, demanding robust non-parametric statistical methods rather than simple Gaussian assumptions.
