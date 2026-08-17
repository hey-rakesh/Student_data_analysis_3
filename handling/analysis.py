import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\git_project\data\clean.csv", encoding="UTF-8")

# print(df.dtypes)
# print(df.shape)
# print(df.isnull().sum())
# print(df.columns)

#-------------------------------------------------------------Department wise Analysis------------------------------------------------

dept_total = df.groupby("department")["name"].size()

dept_plcd = df[df["placement"] == "Placed"].groupby("department")["name"].size()

dept_not_plcd = df[df["placement"]=="Not Placed"].groupby("department")["name"].size()

plcd_percent = ((dept_plcd * 100) / dept_total).round(2).astype(int)


avg_cgpa = df.groupby("department")["cgpa"].mean().round(2)
avg_marks = df.groupby("department")["marks"].mean().round(2)

avg_pkg_plcd_Stds = df[df["placement"] == "Placed"].groupby("department")["package_lpa"].mean().round(2)

dept_analysis = pd.DataFrame({"Total_Student":dept_total,
                              "Placed Students":dept_plcd,
                              "Not Placed Students":dept_not_plcd,
                              "Percetage placed students":plcd_percent,
                              "Average CGPA":avg_cgpa,
                              "Average Marks":avg_marks,
                              "Average Package":avg_pkg_plcd_Stds,
                              
})
# print(dept_analysis)



qualified = df[(df["cgpa"] >= 8) &
               (df["attendance"] >= 75) &
               (df["backlogs"] == 0) &
               (df["placement"] == "Placed")]

qualified["overall_score"] = (
    qualified["cgpa"] * 0.50
    + (qualified["marks"] / 10) * 0.30
    + (qualified["attendance"] / 10) * 0.20
)



# print(qualified[["name", "cgpa", "marks", "attendance", "overall_score"]])

qualified = qualified.sort_values("overall_score", ascending=False)
top_3 = qualified.head(3)

# print(top_3[["name", "cgpa", "marks", "attendance", "package_lpa","overall_score"]])

dept_best_students = qualified.groupby("department")["overall_score"].idxmax()
top_Student = qualified.loc[dept_best_students]

# print(top_Student[["department", "name", "cgpa", "marks", "attendance", "overall_score"]])



dept_high_pkg = df.groupby("department")["package_lpa"].max()
dept_analysis = dept_analysis.sort_values("Percetage placed students", ascending=False)
dept_analysis["Rank"] = dept_analysis["Percetage placed students"].rank(ascending=False, method="dense")
# print(dept_analysis)



# -----------------------------------------------------City Wise Analysis---------------------------------------------------------

city_total = df.groupby("city").size()
city_plcd = df[df["placement"] == "Placed"].groupby("city").size()
city_not_plcd = df[df["placement"] == "Not Placed"].groupby("city").size()
plcd_percent = ((city_plcd * 100 ) / city_total).round(2)
city_avg_cgpa = df.groupby("city")["cgpa"].mean().round(2)
city_avg_marks = df.groupby("city")["marks"].mean().round(2)

city_highest_pkg = df.groupby("city")["package_lpa"].max()





# Highest package of ONLY placed students
placed = df[df["placement"] == "Placed"]
city_high_pkg_idx = (placed.groupby("city")["package_lpa"].idxmax())
city_high_pkg = placed.loc[city_high_pkg_idx]

# print(city_high_pkg)

city_analysis = pd.DataFrame({"Total Students": city_total,
                              "Placed Students": city_plcd,
                              "Not Placed Student":city_not_plcd,
                              "Placement Percent":plcd_percent,
                              "Average Marks":city_avg_marks,
                              "Average CGPA":city_avg_cgpa,
                              "Highest Package":city_highest_pkg
})

placed = df[df["placement"] == "Placed"]

min_package = placed.groupby("city")["package_lpa"].min()
# print(min_package)

# ---------------------------------------or---------------------------------------------

min_pkg = df[df["placement"]=="Placed"].groupby("city")["package_lpa"].min()
# print(min_pkg)

max_cgpa = df.groupby("city")["cgpa"].max()
# print(max_cgpa)


cgpa_8 = df[df["cgpa"] >= 8].groupby("city").size()
# print(cgpa_8)

marks_80 = df[df["marks"] >= 80].groupby("city").size()
# print(marks_80)

topper_city = df.groupby("city")["marks"].idxmax()
# print(topper_city)

# print(df.loc[topper_city][["name", "city"]])

topper_cgpa = df.groupby("city")["cgpa"].idxmax()
# print(df.loc[topper_cgpa])

avg_pkg_plcd = df[df["placement"] == "Placed"].groupby("city")["package_lpa"].mean()
# print(avg_pkg_plcd)

med_pkg_plcd = df[df["placement"] == "Placed"].groupby("city")["package_lpa"].median().round(2)
# print(med_pkg_plcd)

# print(city_analysis)

city_analysis = city_analysis.sort_values("Placement Percent",ascending=False)
city_analysis["City Rank"] = city_analysis["Placement Percent"].rank(ascending=False, method="dense").astype(int)
# print(city_analysis)


condition = (
    (city_analysis["Placement Percent"] > 40) &
    (city_analysis["Average CGPA"] > 5.5) & 
    (city_analysis["Total Students"] >= 10)
)
# print(city_analysis[condition].index)


df["City Rank"] = df.groupby("city")["marks"].transform(
    lambda x: x.rank(ascending=False, method="dense").astype(int)
)

sort_rank = df.sort_values("City Rank", ascending=True)
# print(sort_rank[["name", "marks", "city", "City Rank"]].head(50))

df["city_avg_marks"] = df.groupby("city")["marks"].transform("mean")

df["above_average"] = df["marks"] > df["city_avg_marks"]
df["below_average"] = df["marks"] < df["city_avg_marks"]
df["equal_average"] = df["marks"] == df["city_avg_marks"]

# print(df[["name", "city", "above_average", "below_average", "equal_average"]])

df["City Rank"] = df.groupby("city")["marks"].transform(
    lambda x: x.rank(ascending=False, method="dense")
)

top_2 = df[df["City Rank"] <= 2]

print(top_2[["name", "city", "marks", "City Rank"]])