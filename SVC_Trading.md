# 📈 Support Vector Classifier (SVC) Trading Strategy

This project implements a basic **machine learning-based trading strategy** using a Support Vector Classifier (SVC) to predict the next day's price movement of a stock. The strategy is **systematic, long-only**, and retrains monthly while rebalancing daily.

## 🔍 Overview

* **Strategy Type**: Systematic, Machine Learning
* **Algorithm**: Support Vector Classifier (SVC)
* **Asset Class**: US Equities
* **Security**: Amazon (AMZN)
* **Data Frequency**: Daily OHLCV (Open, High, Low, Close, Volume)
* **Model Retraining**: Monthly (on the first trading day)
* **Portfolio Rebalancing**: Daily (just before market close)


## 📂 Features

* Uses daily stock price data for feature engineering
* Creates technical features:

  * `Open - Close`
  * `High - Low`
* Predicts the next day's price direction (`Up` = 1, `Down` = 0)
* Executes buy/sell orders based on the prediction if model accuracy > 50%

  ### 🧑‍💻 [Code](https://github.com/varmakollu/MLTrade/blob/main/Blueshift.py)


## 🛠️ Requirements

This strategy is built for use on the **Blueshift platform** or other algorithmic backtesting environments that support:

* `numpy`
* `sklearn`
* `blueshift.api` for scheduling and order execution

## 🧠 Model Logic

1. **Feature Engineering**:

   * Calculates two features: intraday range and price direction.
2. **Target Variable**:

   * Predicts whether the next day’s closing price will be higher than today’s.
3. **Training**:

   * Data is split into training (80%) and testing (20%) sets.
   * SVC is trained on the training set monthly.
4. **Prediction**:

   * Daily prediction at close.
   * Trades are only executed if model confidence (accuracy) exceeds 50%.

## ⏱️ Scheduled Functions

* `retrain_model`: Runs at the start of every month to retrain the classifier.
* `rebalance`: Runs daily at market close to evaluate and act on predictions.

## 📈 Strategy Behavior

| Condition                    | Action                          |
| ---------------------------- | ------------------------------- |
| Accuracy > 50% & Signal == 1 | Buy (100% portfolio allocation) |
| Accuracy > 50% & Signal == 0 | Sell (0% allocation)            |
| Accuracy ≤ 50%               | Hold (0% allocation)            |

## ⚠️ Disclaimer

> This code is provided as a **template for educational purposes**.
> It is **not suitable for live trading** without thorough **backtesting**,
> parameter tuning, and **risk management**.
