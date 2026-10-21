# **1️⃣ Hiểu dữ liệu (EDA – Exploratory Data Analysis)**

- Xem **dtypes**, **count**, **missing values**, **summary statistics**
- Vẽ **boxplot / histogram / countplot / heatmap missing values**
- Mục đích: biết dữ liệu có vấn đề gì cần xử lý

---

# **2️⃣ Xử lý missing values**

- **Numeric columns**:

  - Điền trung bình (mean), trung vị (median) hoặc sử dụng **model-based imputation**

- **Categorical columns**:

  - Điền giá trị phổ biến (mode) hoặc "Unknown"

- **Hoặc loại bỏ rows/columns nếu missing quá nhiều**

---

# **3️⃣ Xử lý outliers**

- Xác định bằng **IQR** hoặc **Z-score**
- Cách xử lý:

  - Remove (loại bỏ)
  - Capping / Winsorization
  - Transform (log, sqrt) để giảm skew

---

# **4️⃣ Encode categorical variables**

- **Label Encoding**: với nhãn thứ tự (`pclass`)
- **One-Hot Encoding**: với nhãn không thứ tự (`sex`, `embarked`)
- **Target Encoding / Ordinal Encoding**: nếu cần

---

# **5️⃣ Feature engineering (tạo đặc trưng mới)**

- Ví dụ Titanic:

  - `family_size = sibsp + parch`
  - `is_alone = 1 if family_size == 0 else 0`
  - Nhóm cabin, nhóm tuổi, phân loại giá vé

---

# **6️⃣ Scaling / Normalization numeric features**

- Dùng khi mô hình **nhạy với scale**: SVM, KNN, Neural Network, Logistic Regression

- Scaler phổ biến:

  - `StandardScaler` (Z-score)
  - `MinMaxScaler` (0–1)
  - `RobustScaler` (dữ liệu có outlier)

- Không cần scale nếu dùng **tree-based models** (RandomForest, XGBoost)

---

# **7️⃣ Split dữ liệu train/validation/test**

- Tách dữ liệu trước khi **train** để tránh data leakage
- Ví dụ:

```python
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

# **8️⃣ Optional: Dimensionality Reduction**

- PCA, Feature selection nếu dữ liệu nhiều chiều
- Giúp giảm **overfitting** và tăng tốc tính toán

---

# **9️⃣ Check final dataset**

- Xem lại:

  - Missing values còn không
  - Outliers đã xử lý
  - Scale / Encoding đã chuẩn
  - Dữ liệu train/test đúng format

---

💡 **Tóm tắt thứ tự:**

```
EDA → Missing values → Outliers → Encode categorical → Feature engineering → Scaling → Train/Test split → Optional Dimensionality reduction → Check final dataset
```

---
