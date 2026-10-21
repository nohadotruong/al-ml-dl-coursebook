# 🎨 **1. SCATTER PLOT (biểu đồ phân tán)**

### ✔ Dùng để: xem mối quan hệ giữa 2 biến số.

```python
fig, ax = plt.subplots(figsize=(7,5))

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", ax=ax)

ax.set_title("Scatter Plot: Bill vs Tip")
ax.set_xlabel("Total Bill")
ax.set_ylabel("Tip")

plt.show()
```

---

# 🎨 **2. LINE PLOT (biểu đồ đường)**

### ✔ Dùng cho: dữ liệu thời gian, xu hướng tăng/giảm.

```python
fig, ax = plt.subplots(figsize=(7,5))

sns.lineplot(x=x, y=y, marker="o", ax=ax)
ax.set_title("Line Plot Example")
ax.set_xlabel("Index")
ax.set_ylabel("Value")

plt.show()
```

---

# 🎨 **3. BAR PLOT (biểu đồ cột)**

### ✔ Dùng cho: so sánh theo nhóm (categorical).

```python
fig, ax = plt.subplots(figsize=(7,5))

sns.barplot(data=tips, x="day", y="total_bill", palette="viridis", ax=ax)

ax.set_title("Average Bill per Day")
ax.set_ylabel("Total Bill")

plt.show()
```

---

# 🎨 **4. COUNT PLOT (đếm số lượng mỗi nhóm)**

### ✔ Dùng cho: xem tần suất từng category xuất hiện.

```python
fig, ax = plt.subplots(figsize=(7,5))

sns.countplot(data=tips, x="day", ax=ax)

ax.set_title("Count of Records per Day")

plt.show()
```

---

# 🎨 **5. HISTOGRAM (phân phối)**

```python
fig, ax = plt.subplots(figsize=(7,5))
sns.histplot(tips["total_bill"], kde=True, ax=ax)

ax.set_title("Histogram of Total Bills")

plt.show()
```

---

# 🎨 **6. KDE PLOT (mật độ)**

```python
fig, ax = plt.subplots(figsize=(7,5))
sns.kdeplot(data=tips["total_bill"], fill=True, ax=ax)

ax.set_title("KDE Plot of Total Bills")

plt.show()
```

---

# 🎨 **7. BOX PLOT (hộp)**

### ✔ Dùng để: xem median, IQR, outliers.

```python
fig, ax = plt.subplots(figsize=(7,5))
sns.boxplot(data=tips, x="day", y="total_bill", ax=ax, showfliers=True)

ax.set_title("Boxplot of Bills by Day")

plt.show()
```

---

# 🎨 **8. VIOLIN PLOT (phân phối + boxplot)**

```python
fig, ax = plt.subplots(figsize=(7,5))
sns.violinplot(data=tips, x="day", y="total_bill", ax=ax)

ax.set_title("Violin Plot")

plt.show()
```

---

# 🎨 **9. HEATMAP (ma trận nhiệt)**

### ✔ Dùng cho: ma trận tương quan.

```python
corr = tips.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)

ax.set_title("Correlation Heatmap")

plt.show()
```

---

# 🎨 **10. PAIRPLOT (đa biến)**

### ✔ Dùng cho: khám phá sơ bộ toàn dataset.

```python
sns.pairplot(tips, hue="sex", corner=True)
plt.show()
```

---

# 🎨 **11. JOINT PLOT (2 biến + phân phối)**

```python
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg")
plt.show()
```

---

# 🎨 **12. CATPLOT (vẽ theo nhóm linh hoạt)**

```python
sns.catplot(data=tips, x="day", y="total_bill", kind="violin")
plt.show()
```

---

# 🎨 **13. SWARM PLOT (rải điểm, tránh overlap)**

```python
fig, ax = plt.subplots(figsize=(7,5))
sns.swarmplot(data=tips, x="day", y="total_bill", ax=ax)

ax.set_title("Swarm Plot")

plt.show()
```

---

# 🎨 **14. STRIP PLOT (scatter cho dữ liệu phân loại)**

```python
fig, ax = plt.subplots(figsize=(7,5))
sns.stripplot(data=tips, x="day", y="total_bill", jitter=True, ax=ax)

ax.set_title("Strip Plot")

plt.show()
```

---

# 🎨 **15. RELPLOT (scatter + line nâng cao)**

```python
sns.relplot(data=tips, x="total_bill", y="tip", hue="sex", kind="scatter")
plt.show()
```

---

# ✅ **1. Cách gộp nhiều biểu đồ bằng `plt.subplots` (chuẩn nhất)**

```python
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Biểu đồ 1 (trái)
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=axes[0])
axes[0].set_title("Scatter Plot")

# Biểu đồ 2 (phải)
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[1])
axes[1].set_title("Box Plot")

plt.tight_layout()
plt.show()
```

📌 Kết quả:
Hai biểu đồ nằm cạnh nhau trong **cùng 1 cửa sổ**.

---

# ✅ **2. Subplot dạng lưới: 2×2**

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.histplot(tips["total_bill"], ax=axes[0,0])
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=axes[0,1])
sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[1,0])
sns.barplot(data=tips, x="day", y="tip", ax=axes[1,1])

axes[0,0].set_title("Histogram")
axes[0,1].set_title("Scatter")
axes[1,0].set_title("Boxplot")
axes[1,1].set_title("Barplot")

plt.tight_layout()
plt.show()
```

---

# ✅ **3. Subplot với kích thước khác nhau (GridSpec)**

Dùng khi muốn biểu đồ lớn – nhỏ không đều.

```python
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[2, 1])

ax1 = fig.add_subplot(gs[0, :])   # hàng đầu chiếm full width
ax2 = fig.add_subplot(gs[1, 0])   # bottom-left
ax3 = fig.add_subplot(gs[1, 1])   # bottom-right

sns.lineplot(x=range(10), y=range(10), ax=ax1)
sns.histplot(tips["tip"], ax=ax2)
sns.scatterplot(data=tips, x="total_bill", y="tip", ax=ax3)

ax1.set_title("Large Line Plot")
ax2.set_title("Histogram")
ax3.set_title("Scatter")

plt.tight_layout()
plt.show()
```

---

# ✅ **4. Kết hợp nhiều Seaborn plot với FacetGrid**

(khi biểu đồ giống nhau, chỉ thay dữ liệu nhóm)

```python
g = sns.FacetGrid(tips, col="sex", height=5)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_titles(col_template="{col_name}")
plt.show()
```

---

# ✅ **5. Dùng `plt.subplot()` kiểu nhanh (ít dùng hơn)**

```python
plt.figure(figsize=(10,4))

plt.subplot(1, 2, 1)
sns.histplot(tips["total_bill"])
plt.title("Histogram")

plt.subplot(1, 2, 2)
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Scatter")

plt.tight_layout()
plt.show()
```

---
