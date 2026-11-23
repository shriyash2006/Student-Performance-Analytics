# Module 07: Viva Voce & Oral Defense Q&A

This document compiles the top 15 technical and conceptual questions asked by professors and examiners during practical viva evaluations in Educational Data Mining.

---

### Q1: What is the fundamental difference between Educational Data Mining (EDM) and standard Data Mining?
**Answer:**  
Standard data mining focuses primarily on extracting generalized statistical patterns from arbitrary data (e.g., market basket analysis or financial fraud detection). Educational Data Mining specifically models educational environments—such as student learning trajectories, cognitive skill acquisition, pedagogical intervention efficacy, and institutional attrition risks. In EDM, anomalies (like dropouts or chronically absent students) are not noise to be discarded; they represent the exact sub-populations requiring administrative intervention.

---

### Q2: Why did you load `student-mat.csv` using `sep=';'`?
**Answer:**  
The dataset was collected in Portugal, where commas (`,`) are conventionally used as decimal separators in numerical writing. Consequently, the authors formatted the CSV with semicolons (`;`) to prevent formatting conflicts with numerical floating-point numbers.

---

### Q3: What is the scale of the target variable $G3$, and what does a score of 10 signify?
**Answer:**  
In the Portuguese secondary education grading system, academic performance is evaluated on a continuous integer scale from **0 to 20**. A grade of **10 is the statutory passing threshold**. Any score $< 10$ represents academic course failure.

---

### Q4: Why is the correlation between $G2$ and $G3$ so high ($r = 0.905$)?
**Answer:**  
Academic performance displays strong temporal autocorrelation. The second-period grade ($G2$) is evaluated just a few weeks prior to final exams ($G3$) by the same instructors on cumulative curriculum material. Therefore, student exam preparation and subject mastery remain largely consistent between periods 2 and 3.

---

### Q5: What is "Target Leakage," and how did you prevent it in your machine learning model?
**Answer:**  
Target leakage occurs when predictor variables that contain direct knowledge of the target variable—or variables that would not be available at the true time of operational prediction—are introduced into model training. Including $G1$ and $G2$ allows an artificial neural network to achieve over 92% accuracy, but renders the model practically useless as an early-warning tool at the beginning of the semester. We prevented target leakage by strictly excluding both $G1$ and $G2$ from the feature matrix, forcing the MLP classifier to predict pass/fail outcomes using pre-course demographic, family, and lifestyle features alone.

---

### Q6: Why did you fit `StandardScaler` only on the training set?
**Answer:**  
Fitting a scaler (computing mean $\mu$ and standard deviation $\sigma$) on the entire dataset before train-test splitting leaks test set distribution statistics into the training pipeline (known as *data snooping*). To maintain strict statistical independence, the scaler must compute $\mu_{\text{train}}$ and $\sigma_{\text{train}}$ solely from the training fold, and then apply those identical parameters to transform the unseen test fold.

---

### Q7: In the descriptive statistics, why is $G3$ Skewness negative (-0.7327)?
**Answer:**  
In a typical grading distribution, scores cluster symmetrically around 10–12. However, in our dataset, **38 students scored exactly 0** (representing administrative exam non-attendance, cheating disqualifications, or course withdrawals). This substantial cluster of zero-scores pulls the lower tail far to the left, creating a negative (left-tailed) skewness where the Mean (10.42) is lower than the Median (11.00).

---

### Q8: Why does `failures` have an Interquartile Range ($IQR$) of 0.0?
**Answer:**  
Over 66% of the 395 students in the dataset have never failed a prior grade ($0$ failures). Consequently, the 25th percentile ($Q_1$) is $0.0$ and the 75th percentile ($Q_3$) is also $0.0$. Thus:
$$IQR = Q_3 - Q_1 = 0.0 - 0.0 = 0.0$$

---

### Q9: If Tukey's IQR method flagged 83 students (21%) as outliers in `failures`, why did you NOT remove them?
**Answer:**  
Because an $IQR$ of $0.0$ results in an upper fence of $Q_3 + 1.5(IQR) = 0.0 + 0.0 = 0.0$. Mathematically, any non-zero value ($1, 2, \text{ or } 3$ past failures) is automatically flagged as an outlier. This is an algorithmic artifact of zero-inflated integer data. We retained them because past academic failure is the single strongest non-grade negative predictor of future performance ($r = -0.360$). Removing 21% of the student cohort would destroy the model's ability to recognize at-risk students.

---

### Q10: Why did you retain the 15 outliers in the `absences` column?
**Answer:**  
The upper fence for absences is $20.0$. The 15 students with 21 to 75 absences represent chronic truancy, prolonged illnesses, or severe disengagement. In educational data mining, these extreme cases are valid, real-world data points that represent prime targets for administrative counseling and intervention.

---

### Q11: Does weekly study time correlate strongly with final grades?
**Answer:**  
No. The Pearson correlation between `studytime` and `G3` is only **$r = +0.098$** (very weak). The bar and violin visualizations show that while studying 5–10 hours yields higher average marks than $<2$ hours, studying $>10$ hours exhibits diminishing returns. This proves that raw study duration is insufficient without accounting for study quality, baseline aptitude, and effective learning strategies.

---

### Q12: How does TensorFlow Playground differ from the Python analysis conducted in this practical?
**Answer:**  
TensorFlow Playground is a web-based educational simulator operating strictly on synthetic 2D spatial coordinate datasets ($X_1, X_2$) designed to visualize neural network decision boundaries. It does not host pre-trained student performance models. Our Python implementation, by contrast, processes the real 33-attribute tabular UCI dataset using data auditing, descriptive statistics, visualization, and a 30-feature Scikit-Learn MLPClassifier.

---

### Q13: In TensorFlow Playground, how did 2 layers of ReLU neurons learn a circular decision boundary?
**Answer:**  
A single neuron with a ReLU activation function computes $f(z) = \max(0, w^T x + b)$, producing a flat half-plane bounded by a linear threshold. When 4 ReLU neurons in Hidden Layer 1 project their linear boundaries into Hidden Layer 2 (4 neurons), the network combines these piecewise linear hyperplanes like facets of a polygon. Through backpropagation, the weights adjust so that the intersecting facets enclose the inner class, creating a smooth piecewise-linear circular boundary with a test loss of 0.002.

---

### Q14: Why did the Spiral dataset in TensorFlow Playground require engineered features and Tanh activation?
**Answer:**  
The spiral manifold features two tightly intertwined, non-linear arms with severe curvature around the origin. A simple network with raw linear coordinates $(X_1, X_2)$ gets trapped in local minima. By injecting non-linear trigonometric inputs ($\sin(X_1), \sin(X_2)$) and polynomial terms ($X_1^2, X_2^2$), the network gains spatial periodicity and radial symmetry. The smooth, continuously differentiable **Tanh** activation allows the 3-layer network (6, 4, 2 neurons) to bend decision ribbons smoothly around the spiral arms, achieving a test loss of 0.002 at Epoch 484.

---

### Q15: Why did the MLP classifier achieve 90.57% recall on passing students, but only 11.54% recall on failing students?
**Answer:**  
This asymmetry is driven by **class imbalance**: 67.1% of the cohort passed ($n=265$), while only 32.9% failed ($n=130$). During gradient descent with cross-entropy loss, the network minimizes overall error by biasing its predictions toward the majority class (Pass). To correct this in future work, techniques like synthetic oversampling (SMOTE), class-weighted loss penalties (`class_weight='balanced'`), or lower probability decision thresholds should be applied.
