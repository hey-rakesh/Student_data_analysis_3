# 📊 Student Data Analysis

A Python and Pandas based project for analyzing student academic performance, placement statistics, department-wise performance, city-wise performance, student rankings, and performance-based insights.

---

## 🎯 Project Objective

The project analyzes a cleaned student dataset to extract meaningful insights using **Pandas and NumPy**.

The analysis focuses on department performance, placement outcomes, student scoring, city-wise performance, rankings, and group-level comparisons.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* CSV
* Git & GitHub

---

## 📁 Project Structure

```text
git_project/
│
├── data/
│   ├── clean.csv
│   └── messy.csv
│
├── handling/
│   ├── analysis.py
│   └── cleaning.py
│
└── README.md
```

---

# 🔍 Analysis Questions Solved

## 🏢 1. Department Performance Analysis

**How do different departments compare in terms of placement rate, average CGPA, average marks, and average package?**

The analysis calculates:

* Placement Percentage
* Average CGPA
* Average Marks
* Average Package of Placed Students

Departments are also **ranked according to placement percentage**.

---

## 🏆 2. Qualified Student Identification

**Which placed students meet the academic and attendance criteria for being considered high-performing students?**

Criteria:

* CGPA ≥ 8
* Attendance ≥ 75%
* Backlogs = 0
* Placement = `Placed`

---

## ⭐ 3. Overall Student Performance Score

**How can qualified students be ranked using a weighted performance score?**

The overall score considers:

* CGPA → 50%
* Marks → 30%
* Attendance → 20%

The qualified students are then sorted according to their score.

---

## 🥇 4. Top Performing Students

**Who are the top 3 qualified students and who is the best-performing student from each department?**

The analysis uses the calculated `overall_score` to identify:

* Overall Top 3 students
* Best student from each department

---

# 🌆 City-wise Analysis

## 📈 5. City Performance Analysis

**How do cities compare in terms of placement rate, average CGPA, average marks, and package statistics?**

The analysis calculates:

* Placement Percentage
* Average CGPA
* Average Marks
* Highest Package
* Average Package of Placed Students
* Median Package of Placed Students

Cities are also **ranked according to placement percentage**.

---

## 💰 6. Highest Package Analysis

**What are the highest placement packages achieved in each city among placed students?**

The analysis specifically considers **only placed students** to avoid including package values from unplaced students.

---

## 🏅 7. City-wise Student Ranking

**Who are the top-performing students within each city based on marks?**

Students are ranked separately within their respective cities using `groupby()`, `transform()`, and `rank()`.

The analysis identifies:

* City topper
* Top 2 students from each city
* Individual city rank

---

## 📊 8. Performance Compared with City Average

**Which students perform above, below, or exactly at their city's average marks?**

A city-level average is calculated using `transform("mean")`, and each student's marks are compared against that average.

The analysis creates:

* `above_average`
* `below_average`
* `equal_average`

---

# 🚀 Advanced Pandas Topics Used

* **GroupBy Aggregation**
* **Conditional GroupBy Analysis**
* **Multi-condition Boolean Filtering**
* **Group-wise Ranking**
* **`transform()` for Group-level Calculations**
* **`idxmax()` for Group-wise Maximum Selection**
* **Feature Engineering**
* **Weighted Score Calculation**
* **Group-wise Percentage Calculation**
* **Group-wise Statistical Analysis**
* **Group-wise Sorting & Ranking**
* **Conditional Feature Creation**
* **Top-N Selection**
* **Index-based Row Selection using `loc[]`**
* **DataFrame Construction from Multiple Series**
* **Mean, Median, Maximum & Minimum Aggregation**

---

# 🔮 Future Improvements

* Add Matplotlib visualizations
* Add Seaborn visualizations
* Create an interactive Streamlit dashboard
* Add Scikit-Learn placement prediction
* Add correlation and statistical analysis

---

## 👨‍💻 Author
Rakesh

**Rakesh**

Engineering Student | AI/ML Learner

**Built with Python + Pandas + NumPy**
