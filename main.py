import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(
    page_title="Global Climate EDA",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Title and Introduction ---
st.title('Global Climate EDA: An Interactive Dashboard')
st.write(
    "This dashboard provides an exploratory data analysis of global climate change indicators. "
    "Use the sidebar to select countries to analyze."
)
st.info("Note: This dashboard is currently running on a synthetically generated dataset due to a file-access issue. The structure and code are ready for the real dataset.")


# --- Data Loading ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('climate_change_dataset.csv')
    except FileNotFoundError:
        st.error("Error: The dataset file was not found. Please make sure the CSV file is in the same folder as this app.")
        return None
    return df

df = load_data()

# --- Sidebar for User Inputs ---
st.sidebar.header('Filter Options')

if df is not None:
    all_countries = df['Country'].unique()
    selected_countries = st.sidebar.multiselect(
        'Select Countries',
        options=all_countries,
        default=list(all_countries[:5])  # Default to the first 5 countries
    )

    if selected_countries:
        filtered_df = df[df['Country'].isin(selected_countries)]
    else:
        filtered_df = df.copy()

    # --- Main Panel for Visualizations ---

    st.header('Country-wise Analysis')

    # --- Bar Chart: Average Temperature by Country ---
    st.subheader('Average Temperature Comparison')
    if not filtered_df.empty and selected_countries:
        avg_temp_by_country = filtered_df.groupby('Country')['Avg Temperature (°C)'].mean().sort_values()
        fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
        sns.barplot(x=avg_temp_by_country.values, y=avg_temp_by_country.index, ax=ax_bar, palette="coolwarm")
        ax_bar.set_xlabel('Average Temperature (°C)')
        ax_bar.set_ylabel('Country')
        ax_bar.set_title('Average Temperature for Selected Countries')
        st.pyplot(fig_bar)
    else:
        st.warning("Please select at least one country to see the temperature comparison.")

    st.markdown("---")

    # --- Time Series and Relationship Plots ---
    st.header("Trends and Relationships")
    col1, col2 = st.columns(2)

    # --- Line Chart: Sea Level Rise Over Time ---
    with col1:
        st.subheader('Average Sea Level Rise Over Time')
        if not filtered_df.empty and selected_countries:
            avg_slr_by_year = filtered_df.groupby('Year')['Sea Level Rise (mm)'].mean()
            fig_line, ax_line = plt.subplots(figsize=(10, 6))
            sns.lineplot(data=avg_slr_by_year, marker='o', ax=ax_line, color='teal')
            ax_line.set_ylabel('Avg Sea Level Rise (mm)')
            ax_line.set_xlabel('Year')
            ax_line.set_title('Average Sea Level Rise (for selected countries)')
            ax_line.grid(True)
            st.pyplot(fig_line)

    # --- Scatter Plot: CO2 vs. Temperature ---
    with col2:
        st.subheader('CO2 Emissions vs. Temperature')
        if not filtered_df.empty and selected_countries:
            fig_scatter, ax_scatter = plt.subplots(figsize=(10, 6))
            sns.scatterplot(
                data=filtered_df,
                x='CO2 Emissions (Tons/Capita)',
                y='Avg Temperature (°C)',
                hue='Country',
                alpha=0.8,
                s=100,  # marker size
                ax=ax_scatter
            )
            ax_scatter.set_title('CO2 Emissions vs. Temperature')
            ax_scatter.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()
            st.pyplot(fig_scatter)

    # --- Displaying the Filtered Data ---
    st.header('Filtered Data Explorer')
    if selected_countries:
        st.dataframe(filtered_df)
    else:
        st.write("Select countries from the sidebar to view data.")

else:
    st.warning("Could not load data to run the dashboard.")