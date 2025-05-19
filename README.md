
# 🦠 COVID-19 Global Data Tracker

## 📌 Overview

This project is a Python-based data analysis and visualization tool to track global COVID-19 trends. It uses the **Our World in Data COVID-19 dataset** to analyze cases, deaths, and vaccination progress across selected countries.

---

## 🎯 Objectives

- Import and clean real-world COVID-19 data
- Perform exploratory data analysis (EDA)
- Visualize trends and compare across countries
- Provide insights with well-labeled charts

---

## 📁 Files

- `covid19_global_data_tracker.py` – Main script for data analysis and plotting
- `owid-covid-data.csv` – Source dataset (you must download it)
- `README.md` – Project documentation

---

## 📊 Features

- Line plots for total cases, deaths, and new cases
- Death rate analysis
- Vaccination trends
- Customizable for different countries

---

## 🔧 Setup Instructions

1. **Clone the repository or copy files locally.**

2. **Install dependencies:**

```bash
pip install pandas matplotlib seaborn
```

3. **Download dataset:**

Download `owid-covid-data.csv` from:
[https://ourworldindata.org/covid-cases](https://ourworldindata.org/covid-cases)

4. **Run the script:**

```bash
python covid19_global_data_tracker.py
```

---

## 🌍 Default Tracked Countries

- Kenya
- India
- United States

Modify the `countries` list in `main()` to customize.

---

## 📌 Example Insights

- The U.S. consistently has the highest case counts.
- India experienced spikes in mid-2021.
- Kenya had lower case counts but still saw fluctuations.
- Higher vaccination rates correlate with declining death rates.

---

## 🧠 Next Steps

- Add choropleth maps using Plotly or GeoPandas
- Export analysis to PDF or HTML
- Build a dashboard using Streamlit or Dash

---

## 👨‍💻 Author

Iddy Chesire
