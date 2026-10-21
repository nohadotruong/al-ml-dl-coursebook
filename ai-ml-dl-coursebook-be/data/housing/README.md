# California Housing Dataset — Summary

This dataset is a modified version of the California Housing data introduced in **Aurélien Géron’s book _Hands-On Machine Learning with Scikit-Learn and TensorFlow_**. It contains information from the **1990 California Census** and is widely used for introductory machine learning tasks, especially regression.

---

## 📌 Dataset Overview

- **Rows (samples):** 20,640
- **Columns (features):** 10
- **Task type:** Regression
- **Target variable:** `median_house_value`
- **Source:** Originally from _Pace & Barry (1997)_, compiled and popularized by Aurélien Géron.

This dataset is ideal for learning because:

- It requires basic but realistic preprocessing
- Features are easy to understand
- Data size is manageable (not too small, not too large)

---

## 📂 Features Description

| Column               | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `longitude`          | Geographic longitude of the district (negative = West).   |
| `latitude`           | Geographic latitude of the district (positive = North).   |
| `housing_median_age` | Median age of houses in the district.                     |
| `total_rooms`        | Total number of rooms in all houses of the district.      |
| `total_bedrooms`     | Total number of bedrooms in the district.                 |
| `population`         | Total population living in the district.                  |
| `households`         | Number of households (groups living in one housing unit). |
| `median_income`      | Median income of the district (units = ×10,000 USD).      |
| `median_house_value` | Median home value in USD — **target variable**.           |
| `ocean_proximity`    | Categorical indicator of distance to the ocean.           |

---

## 📌 Notes

- The data is **not cleaned**, so preprocessing steps such as handling missing values, feature engineering, and scaling are typically required.
- The dataset offers a good introduction to:

  - Exploratory Data Analysis (EDA)
  - Regression modeling
  - Feature engineering
  - Handling mixed numerical + categorical data

---

## 📘 Citation

Pace, R. Kelley, and Ronald Barry.
_Sparse spatial autoregressions._ Statistics & Probability Letters 33.3 (1997): 291–297.

---

## 📎 Related Resources

- Géron’s original repository:
  [https://github.com/ageron/handson-ml/tree/master/datasets/housing](https://github.com/ageron/handson-ml/tree/master/datasets/housing)
- Kaggle version:
  [https://www.kaggle.com/datasets/camnugent/california-housing-prices](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
