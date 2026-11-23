# Module 06: Target Leakage & Real-Data MLP Classifier

## 1. The Critical Concept of Target Leakage

In predictive modeling and machine learning, **Target Leakage** occurs when information from outside the training data split—or variables that would not be available at the actual moment of prediction—is introduced into the feature set.

### How Target Leakage Manifests in Student Performance Data
* In `student-mat.csv`, three grading evaluations are recorded: $G1$ (term 1), $G2$ (term 2), and $G3$ (final).
* The correlation between $G2$ and $G3$ is **$r = 0.905$**, and between $G1$ and $G3$ is **$r = 0.801$**.
* If a model includes $G1$ and $G2$ as features to predict whether a student passes $G3$, it will easily achieve **$\ge 92\%$ classification accuracy**.

### Why This is an Operational Failure in Practice:
1. **Zero Lead Time for Intervention:** The second-term grade ($G2$) is finalized only weeks before final examinations. By then, it is too late to design and deploy academic recovery programs.
2. **Trivial Prediction:** Predicting that a student who scored 18 in $G2$ will pass $G3$ requires no machine learning; it is self-evident.
3. **True Purpose of Early Warning Systems:** Educators need to identify at-risk students **at matriculation (Day 1)** using demographic, parental, socio-economic, and historical lifestyle features.

> **Our Implementation:** We **strictly dropped $G1$ and $G2$** from the feature matrix $X$. The classifier is forced to predict academic success using pre-course background features alone!

---

## 2. Model Architecture & Pipeline Design

### 2.1 Preprocessing Pipeline
1. **Target Formulation:**
   $$\text{pass\_fail} = \begin{cases} 1 & \text{if } G3 \ge 10 \quad (\text{Pass, 265 students, 67.1\%}) \\ 0 & \text{if } G3 < 10 \quad (\text{Fail, 130 students, 32.9\%}) \end{cases}$$
2. **Feature Matrix ($X$):** 30 attributes (13 numerical continuous/discrete + 17 label-encoded categorical).
3. **Stratified Partitioning:** 80% Training ($n = 316$), 20% Testing ($n = 79$). Stratification guarantees that the 67:33 pass/fail proportion is preserved identically in both splits.
4. **Leakage-Free Feature Scaling:**
   ```python
   scaler = StandardScaler()
   X_train_scaled = scaler.fit_transform(X_train)  # Calculate mean and std ONLY on training set
   X_test_scaled  = scaler.transform(X_test)       # Transform test set using training parameters
   ```
   *Fitting `StandardScaler` on the entire dataset prior to splitting is a form of data snooping that falsely inflates performance. Our code avoids this.*

---

### 2.2 Neural Architecture: Multi-Layer Perceptron (MLP)
Implemented using `sklearn.neural_network.MLPClassifier`:
* **Input Layer:** 30 features.
* **Hidden Layer 1:** 64 units, **ReLU** non-linearity: $h_1 = \max(0, W_1 x + b_1)$.
* **Hidden Layer 2:** 32 units, **ReLU** non-linearity: $h_2 = \max(0, W_2 h_1 + b_2)$.
* **Output Layer:** 1 unit with Logistic Sigmoid activation:
  $$P(\text{Pass}|x) = \sigma(W_3 h_2 + b_3) = \frac{1}{1 + e^{-(W_3 h_2 + b_3)}}$$
* **Loss Function:** Binary Cross-Entropy (Log Loss).
* **Optimizer:** Adam (Adaptive Moment Estimation) with initial learning rate $\eta = 0.001$.
* **Overfitting Control:** Early stopping enabled (`validation_fraction = 0.15`, `n_iter_no_change = 20`).

---

## 3. Empirical Evaluation & Confusion Matrix

### Test Set Performance ($n = 79$)
* **Overall Accuracy:** **64.56%** (51 correct out of 79 test students).

#### Detailed Classification Report:
| Class | Precision | Recall | F1-Score | Support ($n$) |
|:---|:---:|:---:|:---:|:---:|
| **Fail ($0$)** | 0.3800 | **0.1154 (12%)** | 0.1765 | 26 |
| **Pass ($1$)** | 0.6761 | **0.9057 (91%)** | 0.7742 | 53 |
| **Macro Average** | 0.5280 | 0.5105 | 0.4753 | 79 |
| **Weighted Average** | 0.5788 | 0.6456 | 0.5772 | 79 |

#### Confusion Matrix:
$$\begin{pmatrix} 
\text{True Negative (TN)} = 3 & \text{False Positive (FP)} = 23 \\ 
\text{False Negative (FN)} = 5 & \text{True Positive (TP)} = 48 
\end{pmatrix}$$

* **True Positives (TP = 48):** Students who passed and were correctly identified as passing.
* **True Negatives (TN = 3):** At-risk students who failed and were correctly identified.
* **False Positives (FP = 23):** Students who failed, but the model incorrectly predicted they would pass.
* **False Negatives (FN = 5):** Students who passed, but the model predicted failure.

---

## 4. Educational & Scientific Insights

1. **Why is Accuracy ~65%?**  
   Without $G1$ and $G2$, the neural network has to rely on noisy, indirect socio-demographic features (parent's education, study time, alcohol consumption, address). An accuracy of ~65% proves that socio-economic background has a measurable influence, but does not strictly determine student outcomes.

2. **The Asymmetry of Recall:**  
   The model achieves **90.57% recall on passing students**, but only **11.54% recall on failing students**. 
   * **Cause:** The 67:33 class imbalance drives the optimization gradient toward predicting the majority class (Pass).
   * **Practical Policy Implication:** A pre-course demographic screening system will successfully confirm which students have solid safety nets, but it will miss most at-risk students who need intervention.
   * **Solution for Production:** Educational institutions cannot rely solely on pre-course demographic surveys. They must integrate **formative Learning Management System (LMS) data** (login frequency, homework submissions, quiz scores) during the first 3 weeks of the semester.
