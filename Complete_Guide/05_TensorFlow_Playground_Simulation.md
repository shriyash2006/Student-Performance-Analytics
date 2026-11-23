# Module 05: TensorFlow Playground Live Simulation

## 1. Context and Platform Overview

As mandated by the laboratory specification, **TensorFlow Playground** (https://playground.tensorflow.org/) serves as the primary visual platform for demonstrating artificial neural network training dynamics.

Developed by Daniel Smilkov and Shan Carter (Google Brain team), TensorFlow Playground is an open-source, web-based visualization environment that runs a client-side backpropagation simulation in JavaScript.

---

## 2. Crucial Scientific Distinction

> **Fundamental Distinction:**  
> * **TensorFlow Playground** operates strictly on **synthetic 2D spatial coordinate datasets** ($X_1, X_2 \in [-6, +6]$).
> * **UCI Student Performance** is a **33-dimensional tabular, real-world educational dataset**.
> * TensorFlow Playground does **NOT** provide a pre-trained educational model. We use it to demonstrate how multi-layer architectures bend hyperplanes to separate non-linearly separable spatial classes.

---

## 3. Automated Headless Chrome Execution

To guarantee 100% genuine execution outputs, we scripted a headless browser controller using Node.js and `puppeteer-core` (`code/capture_playground.js`). The script initialized Google Chrome, loaded the playground with configured URL parameters, clicked the live play button (`#play-pause-button`), monitored DOM convergence, and extracted canvas screenshots.

### Platform Parameter Inventory (DOM Inspection)
* **Datasets (Classification):** Circle, Exclusive OR (XOR), Gaussian, Spiral.
* **Datasets (Regression):** Plane, Multi-Gaussian.
* **Input Feature Transformations:** $X_1$, $X_2$, $X_1^2$, $X_2^2$, $X_1 X_2$, $\sin(X_1)$, $\sin(X_2)$.
* **Activation Functions:** ReLU, Tanh, Sigmoid, Linear.
* **Regularization Options:** None, L1, L2.
* **Layer Flexibility:** 0 to 6 hidden layers; 1 to 8 neurons per hidden layer.

---

## 4. Experiment 1: Circle Dataset (Concentric Rings with ReLU)

### Configuration
* **Topology:** 2 Hidden Layers (Layer 1: 4 neurons; Layer 2: 4 neurons).
* **Inputs:** Raw coordinates $X_1, X_2$.
* **Activation:** **ReLU** (Rectified Linear Unit: $f(z) = \max(0, z)$).
* **Learning Rate:** 0.03 | **Noise Level:** 15 | **Train/Test Ratio:** 50%.
* **Batch Size:** 10 | **Regularization:** None.

### Empirical Training Progression
```
Starting training for Circle...
Epoch: 62  | Test Loss: 0.033 | Train Loss: 0.035  (Approximate polygonal boundary)
Epoch: 122 | Test Loss: 0.006 | Train Loss: 0.006  (Boundary rounding)
Epoch: 182 | Test Loss: 0.004 | Train Loss: 0.003
Epoch: 242 | Test Loss: 0.003 | Train Loss: 0.002
Epoch: 302 | Test Loss: 0.002 | Train Loss: 0.001  (Fully converged)
```

### Visual & Mathematical Interpretation
* **Screenshot:** `screenshots/tf_playground_circle_trained.png`
* **How ReLU Forms a Circle:** A single neuron with a linear or ReLU activation outputs a single half-plane split by a straight line ($w_1 X_1 + w_2 X_2 + b = 0$). By feeding 4 linear half-planes into a second hidden layer of 4 neurons, the network acts as a **convex polyhedral slicer**. Through backpropagation, the weights adjust so that the intersecting linear facets enclose the inner circular cluster, resulting in a piecewise-linear approximation of a circle with near-zero loss (0.002).

---

## 5. Experiment 2: Spiral Dataset (Complex Manifold with Tanh)

### Configuration
* **Topology:** 3 Hidden Layers (Layer 1: 6 neurons; Layer 2: 4 neurons; Layer 3: 2 neurons).
* **Inputs:** All 7 available feature projections ($X_1, X_2, X_1^2, X_2^2, X_1 X_2, \sin(X_1), \sin(X_2)$).
* **Activation:** **Tanh** (Hyperbolic Tangent: $f(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}}$).
* **Learning Rate:** 0.03 | **Noise Level:** 0 | **Train/Test Ratio:** 50%.

### Empirical Training Progression
* **Target Epoch Reached:** 484 epochs.
* **Final Test Loss:** **0.002** | **Final Training Loss:** **0.001**.
* **Screenshot:** `screenshots/tf_playground_spiral_trained.png`.

### Visual & Mathematical Interpretation
* **The Challenge of the Spiral:** The two classes are tightly wound around the origin in interlocking concentric spirals. A basic 2-layer network with raw coordinates $(X_1, X_2)$ will fail because the manifold possesses infinite direction changes.
* **Why Feature Engineering & Tanh Succeeded:**
  1. The inclusion of sinusoidal basis functions $\sin(X_1)$ and $\sin(X_2)$ introduces periodic spatial undulations.
  2. The quadratic terms $X_1^2, X_2^2$ provide radial symmetry around the origin.
  3. The smooth, continuously differentiable nature of the **Tanh** activation avoids the sharp corners of ReLU, allowing the 3-layer network to weave smooth, interlocking decision ribbons around the spiral arms.
