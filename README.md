# Medical Insurance Cost Prediction

## 📌 Project Overview

This project uses Machine Learning to predict medical insurance charges based on an individual's demographic and health-related attributes, including age, sex, BMI, smoking status, number of children, and residential region.

The objective is to understand the factors influencing insurance costs, compare regression models, and deploy a web application that allows users to obtain predictions based on their input.

## 🚀 Live Demo

**Try the application:** [Medical Insurance Cost Predictor](https://insurance-cost-predictor-xbedoh7ajgtufvhjg5itbf.streamlit.app/)

## 🛠️ Tech Stack

- **Python** — Model development and implementation
- **Pandas & NumPy** — Data manipulation and numerical computations
- **Matplotlib & Seaborn** — Exploratory data analysis and visualization
- **Scikit-learn** — Data preprocessing, model training, and evaluation
- **Joblib** — Saving and loading trained models
- **Streamlit** — Interactive web application
- **Git & GitHub** — Version control and project hosting

## 📊 Dataset

The project uses a medical insurance dataset containing information about individuals and their insurance charges.

| Feature | Description |
|---|---|
| `age` | Age of the individual |
| `sex` | Sex of the individual |
| `bmi` | Body Mass Index |
| `children` | Number of dependent children |
| `smoker` | Smoking status |
| `region` | Residential region |
| `charges` | Medical insurance charges (target variable) |

## 🔄 Project Workflow

### 1. Exploratory Data Analysis (EDA)
- Examined the dataset structure and statistical summaries.
- Analyzed distributions and relationships between features and insurance charges.
- Explored the impact of smoking status, age, and BMI on insurance costs.

### 2. Data Preprocessing
- Prepared categorical and numerical features for machine learning.
- Applied the necessary feature encoding and scaling steps.
- Prepared the input features and target variable for model training.

### 3. Model Training and Comparison

Trained and evaluated multiple regression algorithms to identify the best-performing model.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 4,298.38 | 5,997.91 | 0.80 |
| Random Forest Regressor | 2,801.50 | 4,816.48 | 0.87 |
| Gradient Boosting Regressor | 2,605.72 | 4,398.71 | **0.89** |

**Best-performing model: Gradient Boosting Regressor**

Gradient Boosting achieved the highest R² score and the lowest MAE and RMSE among the evaluated models.

*Note: The error metrics are expressed in the same units as the dataset's insurance charges.*

### 4. Model Evaluation

The models were compared using:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between actual and predicted charges.
- **Root Mean Squared Error (RMSE):** Penalizes larger prediction errors more heavily.
- **R² Score:** Measures how much of the variation in insurance charges is explained by the model.

The selected model achieved an **R² score of 0.89**, indicating that it explains approximately 89% of the variance in the evaluation data.

### 5. Model Deployment

- Saved the trained model and required preprocessing artifacts using Joblib.
- Developed an interactive application using Streamlit.
- Enabled users to enter individual details and receive predicted insurance charges.
- Deployed the application online for easy access.

## 💻 Run Locally

### Prerequisites
- Python installed
- Git installed

### Step 1: Clone the repository

```bash
git clone https://github.com/capturedbykaran/insurance-cost-predictor.git
cd insurance-cost-predictor
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Streamlit application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## 📁 Project Structure

```text
insurance-cost-predictor/
├── app.py
├── Insurance.ipynb
├── best_model.joblib
├── feature_columns.joblib
├── scaler.joblib
├── insurance.csv
├── requirements.txt
└── README.md
```

## 🔑 Key Learnings

- Performing exploratory data analysis on real-world tabular data.
- Preparing categorical and numerical features for regression.
- Comparing machine learning models using appropriate evaluation metrics.
- Understanding the trade-offs between linear and ensemble-based regression models.
- Saving trained models and preprocessing artifacts for inference.
- Deploying a machine learning model through a user-friendly web interface.

## 🔮 Future Improvements

- Add feature importance visualizations to improve model interpretability.
- Improve the application interface and prediction explanations.
- Evaluate additional regression algorithms and hyperparameter tuning strategies.
- Add automated model testing and input validation.

## 👨‍💻 Author

**Karan**

- [GitHub](https://github.com/capturedbykaran)
- [LinkedIn](https://www.linkedin.com/in/captured-by-karan)
