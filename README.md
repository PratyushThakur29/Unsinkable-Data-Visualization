**Unsinkable Data Visualization** is a lightweight, introductory Exploratory Data Analysis (EDA) script built using Python. This project loads the historical Titanic dataset directly from a live remote repository, cleans missing values, computes key summary statistics, and generates analytical visualizations using `matplotlib` and `seaborn` to examine survival variables.

---

## 📊 Overview of the Analysis

The script walks through a standard data science workflow:
1. **Data Ingestion:** Loads the Titanic CSV dataset dynamically from a remote URL.
2. **Inspection:** Displays the first few records and outputs comprehensive statistical data summaries (count, mean, standard deviation, percentiles).
3. **Data Cleaning:** Detects missing value distributions and handles the `Age` column's missing elements by imputing them with the **median age** of the dataset.
4. **Data Visualization:** Generates four distinct visual plots to reveal underlying survival patterns.

---

## 📈 Visualizations Included

The project creates the following four visual insights:
* **Plot 1: Survival Count** – A baseline chart visualizing the total breakdown of survivors vs. non-survivors.
* **Plot 2: Survival by Gender** – A grouped breakdown revealing the massive impact gender had on structural survival rates ("Women and children first").
* **Plot 3: Age Distribution** – A detailed histogram with a Kernel Density Estimate (KDE) curve mapping out passenger age frequency.
* **Plot 4: Passenger Class vs Survival** – A categorical comparison highlighting how lower socio-economic status (Ticket Class 3) correlated to a higher mortality rate.

---

## 🛠️ Tech Stack & Requirements

This script is built using core Python data science libraries:
* **Pandas** - For dataframe handling and data ingestion.
* **NumPy** - For statistical and numerical computation backup.
* **Matplotlib** - For window frame generation and plot structures.
* **Seaborn** - For stylized, high-level categorical graphs.
