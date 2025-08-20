# Employee Performance Analysis
# Author: Data Analyst
# Verification Email: 22f3000284@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import mpld3
import inspect

# -------------------------
# Step 1: Load the dataset
# -------------------------
data = {
    "employee_id": ["EMP001", "EMP002", "EMP003", "EMP004", "EMP005"],
    "department": ["Sales", "Sales", "Marketing", "Operations", "HR"],
    "region": ["North America", "Latin America", "Middle East", "North America", "Europe"],
    "performance_score": [88.45, 65.73, 94.46, 87.06, 85.55],
    "years_experience": [9, 6, 4, 15, 15],
    "satisfaction_rating": [4.9, 3.8, 3.9, 4.6, 4.1]
}

df = pd.DataFrame(data)

# -------------------------
# Step 2: Frequency count for Operations department
# -------------------------
operations_count = df[df["department"] == "Operations"].shape[0]
print("Frequency count for Operations department:", operations_count)

# -------------------------
# Step 3: Create histogram of department distribution
# -------------------------
plt.figure(figsize=(8, 5))
df["department"].value_counts().plot(kind="bar")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

# Convert the matplotlib figure to HTML
html_chart = mpld3.fig_to_html(plt.gcf())

# -------------------------
# Step 4: Embed email, code, and chart into HTML
# -------------------------
# Get this script's code as a string
code_str = inspect.getsource(inspect.currentframe())

html_content = f"""
<html>
<head>
    <title>Employee Performance Analysis</title>
</head>
<body>
    <h2>Employee Performance Analysis</h2>
    <p><b>Verification Email:</b> 22f3000284@ds.study.iitm.ac.in</p>
    <p><b>Frequency count for Operations department:</b> {operations_count}</p>
    <h3>Python Code Used:</h3>
    <pre>{code_str}</pre>
    <h3>Visualization:</h3>
    {html_chart}
</body>
</html>
"""

with open("employee_performance_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file 'employee_performance_analysis.html' generated successfully with email + code + chart.")
