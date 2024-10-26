# uni-machine-learning
This repository showcases a research project focused on leveraging **Long Short-Term Memory (LSTM)** networks and **Gated Recurrent Units (GRU)** for predicting cryptocurrency trends. The study bridges the gap between machine learning and finance, evaluating time series models on historical **Bitcoin price data** over the last four years, influenced by significant market events such as COVID-19 and the 2024 halving.

## Group Project - Cryptocurrency
With **Machine Learning (ML)** and **Finance** intersecting in recent years, this study aims to bridge the gap between the subjects using ML models as the vehicle for accurately **predicting Time Series data on Cryptocurrencies.** The project evaluates **Time Series Models** such as **Long Short-Term Memory (LSTM)** and **Gated Recurrent Unit (GRU)** to investigate their performance on historical price data without bias. The dataset covers the last four years due to market conditions, making it ideal for model analysis. The research measures model performance through metrics like **Mean Squared Error**, utilizing data sourced from public interfaces such as **Yahoo Finance**.

### Installation
- Open VSCode terminal and type "git clone https://github.com/xLightless/uni-machine-learning.git"
- After type "py -m venv .venv"
- Next, change directory (cd) to .venv and then activate it.
- pip install -r requirements.txt
- Go to the main.ipynb and run the install requirements cell.

### Data Collection
Data can publically be acquired via Yahoo Finance. This project uses an unofficial API to accommodate for the collection of such data.
It also comes with a large community therefore it is a good choice for potential Machine Learning configurations such as SVMs with Particle Swarm Optimisation (PSO).

## Individual Project - Using Machine Learning to Classify Diabetes
### Support Vector Machines (SVM)
Support Vector Machines (SVM) are supervised learning algorithms used for classification and regression tasks. They group inputs, or features, into classified support vectors. SVM employs kernel functions—such as Radial Basis Function (RBF) and linear—to classify features in higher-dimensional spaces. The study investigates the performance of linear models, which define decision boundaries (hyperplanes) for input features. Hyperparameter optimization is conducted using Grid Search Cross Validation to enhance accuracy and precision.

### Ensemble Methods
Ensemble methods combine multiple base learning models, particularly decision trees, to improve predictive performance. Techniques such as Random Forest and boosting methods like XGBoost and AdaBoost are utilized to enhance accuracy while managing time complexity. For this project, a Random Forest classifier is employed as the base model, augmented by Adaptive Boosting to achieve high predictive accuracy without requiring feature scaling.

For additional reading, refer to the following resources:

- [Does Random Forest Need Feature Scaling or Normalization?](https://forecastegy.com/posts/does-random-forest-need-feature-scaling-or-normalization/#:~:text=Random%20Forest%20is%20a%20tree,can%20be%20skipped%20during%20preproc) (2023)
- [Lecture 3: The Perceptron](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote03.html) (2024)
- [Lecture 9: SVM](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote09.html) (2024)
- [YouTube Video on SVM](https://www.youtube.com/watch?v=NnmKeYUYMPY)

### Methodology
Additionally, the project explores **Support Vector Machines (SVM)** and **Ensemble** methods. Key aspects include:

- **Domain Knowledge**: Understanding the underlying data.
- **Data Cleaning**: Managing missing values for accuracy.
- **Feature Engineering**: Transforming features to enhance model performance.
- **Normalization/Standardization**: Adjusting data to similar ranges for improved analysis.
