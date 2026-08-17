import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\git_project\data\messy.csv", encoding="UTF-8")
# print(df.shape)
# print(df.duplicated().sum())
# print(df.drop_duplicates(["student_id"],inplace=True))
# print(df.duplicated().sum())


df["name"] = df["name"].str.strip()
df["name"] = df["name"].str.title()
# print(df["name"])

# print(df["age"].head(20))
# print(df["age"].isnull().sum())
# print(df["age"].nunique())
# print(df["age"].unique())
df["age"] = df["age"].replace({"unknown":np.nan, 
                               "?":np.nan,
                               "-":""})
# print(df["age"].nunique())
# print(df["age"].unique())
df["age"] = df["age"].str.strip()
df["age"] = pd.to_numeric(df["age"])
# print(df[df["age"]<0].sum())
df.loc[df["age"] < 0, "age"] = np.nan
df["age"] = df["age"].fillna(df["age"].median()).astype(int).round()
# print(df["age"].isnull().sum())
# print(df["age"].nunique())


#-----------------------------------------------Gender------------------------------------------------------

# print(df["gender"].nunique())
# print(df["gender"].unique())
df["gender"] = df["gender"].replace({"female":"Female",
                                     "f":"Female",
                                     "FEMALE":"Female",
                                     "MALE":"Male",
                                     "M":"Male",
                                     "F":"Female",
                                     "male":"Male"
                                     })
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])

# print(df["gender"].nunique())
# print(df["gender"].unique())


#----------------------------------------------------------City-------------------------------------------------------

# print(df["city"].unique())
# print(df["city"].nunique())
df["city"] = df["city"].str.strip()

df["city"] = df["city"].replace({"pune":"Pune",                        # other method use lower case then title key word
                                "indore":"Indore",                    
                                "jaipur":"Jaipur",                  # bangaluru, calcutta delhi wale case ke liye ye sahi rahta
                                "Bengaluru":"Bangalore",
                                "CALCUTTA":"Kolkata",
                                "delhi":"New Delhi",
                                "bhopal":"Bhopal",
                                "BHOPAL":"Bhopal",
                                "gwalior":"Gwalior",
                                "DEWAS":"Dewas",
                                "UJJAIN":"Ujjain",
                                "JAIPUR":"Jaipur",
                                "bengaluru":"Bangalore",
                                "New Delhi":"New Delhi",
                                "MUMBAI":"Mumbai",
                                "dewas":"Dewas",
                                "kolkata":"Kolkata",
                                "mumbai":"Mumbai",
                                "nagpur":"Nagpur",
                                "PUNE":"Pune",
                                "INDORE":"Indore",
                                "DELHI":"New Delhi",
                                "ujjain":"Ujjain",
                                "Delhi":"New Delhi"
                                })

df["city"] = df["city"].fillna(df["city"].mode()[0])
# print(df["city"].unique())
# print(df["city"].nunique())


#----------------------------------------------------State-------------------------------------------------


# print(df["state"].unique())
# print(df["state"].nunique())
df["state"] = df["state"].fillna(df["state"].mode()[0])
# print(df["state"].unique())
# print(df["state"].nunique())

#----------------------------------------------Department---------------------------------------------------------

# print(df["department"].unique())
# print(df["department"].nunique())
df["department"] = df["department"].str.strip()
df["department"] = df["department"].replace({"civil":"Civil",
                                             "CIVIL":"Civil",
                                             "me":"ME",
                                             "data science":"DS",
                                             "Data Science":"DS",
                                             "I.T.":"IT",
                                             "cse":"CSE",
                                             "Computer Science":"CSE",
                                             "ece":"ECE",
                                             "E.C.E":"ECE",
                                             "aiml":"AIML",
                                             "Mechanical":"ME",
                                             "it":"IT",
                                             "AI ML":"AIML",
                                             "AI-ML":"AIML",
                                             "C.S.E":"CSE"
                                             })
df["department"] = df["department"].fillna(df["department"].mode()[0])
# print(df["department"].unique())
# print(df["department"].nunique())


#---------------------------------------------------Marks----------------------------------------------------

# print(df["marks"].isnull().sum())

df["marks"] = df["marks"].str.strip()
df["marks"] = df["marks"].replace({"?":np.nan,
                                   "unknown":np.nan
                                   })
temp = pd.to_numeric(df["marks"], errors="coerce")                   
# print(df.loc[temp.isna(), "marks"].value_counts(dropna=False))           # how to find all varity of nuknown values
df["marks"] = pd.to_numeric(df["marks"])

df["marks"] = df["marks"].fillna(df["marks"].mean()).round()
# print(df["marks"].isnull().sum())



#----------------------------------------------------attendance-----------------------------------------------

# print(df["attendance"].isnull().sum())
temp = pd.to_numeric(df["attendance"], errors="coerce")
# print(df.loc[temp.isna(), "attendance"].value_counts(dropna=False))
df["attendance"] = df["attendance"].str.strip()
df["attendance"] = df["attendance"].replace({"unknown":np.nan,
                                             "?":np.nan
                                             })
df["attendance"] = pd.to_numeric(df["attendance"])
df["attendance"] = df["attendance"].fillna(df["attendance"].mean()).round()
# print(df["attendance"].isnull().sum())


#------------------------------------------------------CGPA-------------------------------------------------------------

df["cgpa"] = pd.to_numeric(df["cgpa"], errors="coerce")

df["cgpa"] = df["cgpa"].replace([np.inf, -np.inf], np.nan)               # how to handle infinite values

df.loc[(df["cgpa"]<0) | (df["cgpa"]>=10), "cgpa"] = np.nan

df["cgpa"] = df["cgpa"].fillna(df["cgpa"].median())

# print(df["cgpa"].isna().sum())
# print(np.isinf(df["cgpa"]).sum())


# -----------------------------------------------------internship------------------------------------------------

# print(df["internship"].nunique())
# print(df["internship"].unique())
df["internship"] = df["internship"].replace({"YES":"Yes",
                                             "no":"No",
                                             "NO":"No",
                                             "N":"No",
                                             "Y":"Yes",
                                             "yes":"Yes",
                                             })


df["internship"] = df["internship"].fillna(df["internship"].mode()[0])
# print(df["internship"].nunique())
# print(df["internship"].unique())



# -------------------------------------------------placement-----------------------------------------------------

# print(df["placement"].nunique())
# print(df["placement"].unique())
df["placement"] = df["placement"].str.strip()
df["placement"] = df["placement"].replace({"not placed":"Not Placed",
                                           "Not placed":"Not Placed",
                                           "PLACED":"Placed",
                                           "Yes":"Placed",
                                           "placed":"Placed",
                                           "No":"Not Placed",
                                           
                                           })

df["placement"] = df["placement"].fillna(df["placement"].mode()[0])
# print(df["placement"].nunique())
# print(df["placement"].unique())


# ------------------------------------------------------package_lpa--------------------------------------------------
import pandas as pd
import numpy as np

# 1. Initial missing values
# print("Initial NaN:", df["package_lpa"].isnull().sum())


# 2. Remove extra spaces
df["package_lpa"] = df["package_lpa"].astype("string").str.strip()


# 3. Remove LPA / lpa / Lpa etc.
df["package_lpa"] = (df["package_lpa"].str.replace(r"(?i)\s*lpa", "", regex=True))


df["package_lpa"] = pd.to_numeric(df["package_lpa"],errors="coerce")


# 5. Check invalid/missing values AFTER cleaning
# print(df.loc[df["package_lpa"].isna(),"package_lpa"].value_counts(dropna=False))



df["package_lpa"] = df["package_lpa"].fillna(df["package_lpa"].mean())

# print(df["package_lpa"].isnull().sum())
# print(df["package_lpa"].value_counts(dropna=False))


# ------------------------------------------------------salary------------------------------------------------------

# print(df["salary"].isnull().sum())
temp_1 = pd.to_numeric(df["salary"], errors="coerce")
# print(df.loc[temp_1.isna(), "salary"].value_counts())

df["salary"] = (df["salary"].astype("string").str.strip())

df["salary"] = df["salary"].str.replace("₹", "", regex=False)
df["salary"] = df["salary"].str.replace(r"(?i)\s*INR","", regex=True)
df["salary"] = df["salary"].str.replace(r"(?i)\s*K", "000", regex=True)

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["salary"] = df["salary"].fillna(df["salary"].median()).round()

# print(df["salary"].value_counts(dropna=False))


#--------------------------------------------------------projects-----------------------------------------------------

# print(df["projects"].isnull().sum())
# print(df["projects"].value_counts(dropna=False))
df["projects"] = df["projects"].str.strip()
df["projects"] = df["projects"].replace({"?":np.nan,
                                         "unknown":np.nan
                                         })
df["projects"] = pd.to_numeric(df["projects"], errors="coerce")
df["projects"] = df["projects"].fillna(df["projects"].mean()).round()
# print(df["projects"].isnull().sum())
# print(df["projects"].value_counts(dropna=False))


#------------------------------------------------------backlogs---------------------------------------------------

# print(df["backlogs"].isnull().sum())
# print(df["backlogs"].value_counts(dropna=False))
df["backlogs"] = df["backlogs"].astype("string").str.strip()

df["backlogs"] = pd.to_numeric(df["backlogs"], errors="coerce")              # handle unknown ,? == NaN

df.loc[df["backlogs"]<0, "backlogs"] = np.nan

df["backlogs"] = df["backlogs"].fillna(df["backlogs"].median())
df["backlogs"] = df["backlogs"].astype(int)
# print(df["backlogs"].isnull().sum())
# print(df["backlogs"].value_counts(dropna=False))


#---------------------------------------------------------joining_date---------------------------------------------------------

# print(df["joining_date"].value_counts(dropna=False))

df["joining_date"] = pd.to_datetime(df["joining_date"], errors="coerce")
df["joining_date"] = df["joining_date"].dt.strftime("%d-%m-%Y")
# print(df["joining_date"].isna().sum())
# print(df["joining_date"].dtype)

# print(df["joining_date"].value_counts(dropna=False))


#-------------------------------------------------------payment_mode-------------------------------------------------------


# print(df["payment_mode"].nunique())
# print(df["payment_mode"].unique())

df["payment_mode"] = df["payment_mode"].str.strip().str.lower()
df["payment_mode"] = df["payment_mode"].str.replace({"upi":"UPI",
                                                    "cash":"Cash",
                                                    "card":"Card",
                                                    "net banking": "Net Banking"})

# print(df["payment_mode"].nunique())
# print(df["payment_mode"].unique())

# print(df["payment_mode"].isnull().sum())
# print(df["payment_mode"].value_counts(dropna=False))
df["payment_mode"] = df["payment_mode"].fillna(df["payment_mode"].mode()[0])



#-----------------------------------------------------------------E-Mail--------------------------------------------------------


# print(df["email"].value_counts(dropna=False))
# print(df["email"].isnull().sum())
df["email"] = df["email"].str.strip().str.lower().astype("string")

email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

valid_email = df["email"].str.match(email_pattern, na=False)

df.loc[~valid_email, "email"] = np.nan
# print(df["email"].value_counts(dropna=False))
# print("Missing/Invalid:", df["email"].isna().sum())



# ---------------------------------------------------------------Phone----------------------------------------------------------

# print(df["phone"].isnull().sum())
# print(df["phone"].value_counts(dropna=False))
df["phone"] = df["phone"].astype("string")
df["phone"] = df["phone"].str.strip()
# print(df["phone"].isnull().sum())
# print(df["phone"].value_counts(dropna=False))


valid_phone = df["phone"].str.fullmatch(r"[6-9]\d{9}",na=False)


df.loc[~valid_phone, "phone"] = pd.NA
# print("Missing/Invalid:", df["phone"].isna().sum())

df.to_csv(r"D:\git_project\data\clean.csv",index=False)