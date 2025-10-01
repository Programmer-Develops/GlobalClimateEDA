<div align="center">

![GlobalClimateEDA](https://img.shields.io/badge/GlobalClimateEDA-blue) ![Python](https://img.shields.io/badge/Python-3.11+-green) ![Streamlit](https://img.shields.io/badge/Streamlit-1.50.0-red)
</div>

# 🌍 Global Climate Insights Dashboard

**Team:** Tech Square

## 1. Project Overview

This project serves as a response to the "Analyzing Global Climate Change Data for Policy Insights" problem statement. Our team, Tech Square, has taken on the role of data consultants for an international environmental agency to analyze a comprehensive climate change dataset.

The primary goal is to perform a detailed Exploratory Data Analysis (EDA) to uncover significant patterns, trends, and correlations. The insights derived from this analysis are presented through an interactive Streamlit dashboard, designed to help policymakers make data-driven decisions to combat climate change and promote sustainability.

## 2. Dataset

The analysis is based on a global climate change dataset sourced from Kaggle. It contains various climate-related indicators across multiple countries and years.

**Key features in the dataset include:**
- **Year:** The year of the recorded data (2000-2024).
- **Country:** The country or region.
- **Avg Temperature (°C):** The average annual temperature.
- **CO2 Emissions (Tons/Capita):** Per-person carbon dioxide emissions.
- **Sea Level Rise (mm):** Annual increase in sea level.
- **Rainfall (mm):** Total annual rainfall.
- **Population:** The country's population for the given year.
- **Renewable Energy (%):** The percentage of energy from renewable sources.
- **Extreme Weather Events:** The count of major weather events.
- **Forest Area (%):** The percentage of land covered by forests.

## 3. The Interactive Dashboard

The core of this project is an interactive web application built with Streamlit. It allows users to dynamically filter and visualize the data to discover insights on their own.

### Key Features:
- **High-Level KPIs:** At-a-glance metrics (KPIs) that summarize the data based on the user's selections.
- **Dynamic Filtering:** Users can filter the entire dashboard by a specific **range of years** and by selecting one or more **countries**.
- **Interactive World Map:** A choropleth map that provides a geographical overview of a selected climate indicator, such as average temperature or CO2 emissions.
- **Customizable Trend Analysis:** A dynamic line chart that allows users to select any indicator and visualize its trend over the selected time period.
- **Relationship Analysis:**
    - A **Correlation Heatmap** to instantly show the statistical relationships between all variables.
    - An interactive **Scatter Plot** to explore the specific relationship between CO2 emissions and average temperature.
- **Data Explorer:** A table that displays the filtered raw data for detailed inspection.

## 4. Technologies Used

- **Language:** Python
- **Libraries:**
    - **Streamlit:** For building the interactive web dashboard.
    - **Pandas:** For data manipulation and cleaning.
    - **Plotly Express:** For creating interactive charts and maps.
    - **Matplotlib & Seaborn:** For generating the correlation heatmap.

## 5. How to Run the Project Locally

To run the dashboard on your own machine, please follow these steps:

**Prerequisites:**
- Python 3.8 or higher installed.
- `pip` (Python package installer).

**Step 1: Clone the Repository**
Clone this project from GitHub to your local machine.
```bash
git clone <your-repository-url>
cd <repository-folder-name>
```
**Step 2: Install Required Libraries**
Install all the necessary packages using the requirements.txt file. It's recommended to do this in a virtual environment.
```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

Step 3: Run the Streamlit App
Make sure the `main.py` script and the `climate_change_dataset.csv` file are in the same directory. Run the following command in your terminal:
```Bash
streamlit run app.py
```

<div align="center">
Made with ❤️ and 😊 by the Tech Square Team

"Data is a precious thing and will last longer than the systems themselves." - Tim Berners-Lee

</div>