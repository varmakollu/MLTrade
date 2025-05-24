# 🧠 Machine Learning Exercises – Python Practice

Welcome to this beginner-friendly repository of interactive machine learning exercises using Python! These short coding tasks are designed to help you practice essential machine learning concepts, data handling techniques, and model building strategies using tools like `pandas`, `sklearn`, and `matplotlib`.

---

## 📁 Exercise List

### 1. **Basic Python Expression**

* **Objective:** Print the value of a simple arithmetic expression.
* **Task:**

  ```python
  d = 6 / 3
  print(d)  # Output: 2.0
  ```

### 2. **Importing Machine Learning Libraries**

* **Objective:** Get started with the Support Vector Classifier (SVC).
* **Task:**

  ```python
  from sklearn.svm import SVC
  ```

### 3. **Reading Data from CSV**

* **Objective:** Load and view S\&P 500 historical price data from a CSV file.
* **Instructions:**

  * CSV File: `../data/SPY.csv`
  * Set the first column as index.
* **Task:**

  ```python
  Df = pd.read_csv('../data/SPY.csv', index_col=0)
  print(Df.head())
  ```

---

## 🛠 Requirements

To run the scripts, make sure you have the following libraries installed:

```bash
pip install pandas numpy matplotlib scikit-learn
```

---

## 📚 Concepts Covered

* Basic Python syntax and arithmetic
* Support Vector Classifier (SVC) usage from `sklearn`
* CSV file handling with `pandas`
* DataFrame inspection with `.head()`
* Preparing data for machine learning tasks

---

## 💡 Hints & Tips

* Use the Python console for quick practice.
* Refer to the official documentation for detailed explanations:

  * [pandas documentation](https://pandas.pydata.org/)
  * [scikit-learn documentation](https://scikit-learn.org/stable/)

---

## 📬 Feedback

If you have questions or suggestions, feel free to open an issue or reach out!

Happy Learning! 🚀
