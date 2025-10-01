import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(
    page_title="Global Climate Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Title and Introduction ---
st.title('🌍 Global Climate Insights Dashboard')
st.markdown("An interactive tool to explore climate change indicators and inform policy decisions.")

# --- Data Loading and Cleaning ---
@st.cache_data
def load_and_clean_data():
    """
    Loads the dataset, handles potential errors, and performs basic cleaning.
    To use your real data, ensure the filename is 'climate_change_dataset.csv'.
    """
    try:
        df = pd.read_csv('climate_change_dataset.csv')
        df.dropna(inplace=True)
        return df
    except FileNotFoundError:
        st.error("FATAL: The file 'climate_change_dataset.csv' was not found.")
        st.info("Please make sure your dataset is in the same folder as the app and is named correctly.")
        return None

df = load_and_clean_data()

# Stop the app if the data fails to load
if df is None:
    st.stop()

# --- Sidebar for User Inputs ---
st.sidebar.header('Dashboard Filters')

min_year, max_year = int(df['Year'].min()), int(df['Year'].max())
selected_year_range = st.sidebar.slider(
    'Select Year Range',
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

all_countries = sorted(df['Country'].unique())
selected_countries = st.sidebar.multiselect(
    'Select Countries',
    options=all_countries,
    default=all_countries[:5] 
)

# --- Filtering Logic ---

if selected_countries:
    filtered_df = df[
        (df['Country'].isin(selected_countries)) &
        (df['Year'] >= selected_year_range[0]) &
        (df['Year'] <= selected_year_range[1])
    ]
else:
    filtered_df = df[
        (df['Year'] >= selected_year_range[0]) &
        (df['Year'] <= selected_year_range[1])
    ]

# --- Main Panel ---

if filtered_df.empty:
    st.warning("No data available for the selected filters. Please adjust your selections.")
else:
    # --- KPI Metrics Section ---
    st.header("High-Level KPIs")
    avg_temp = filtered_df['Avg Temperature (°C)'].mean()
    avg_co2 = filtered_df['CO2 Emissions (Tons/Capita)'].mean()
    total_events = filtered_df['Extreme Weather Events'].sum()
    avg_renewable = filtered_df['Renewable Energy (%)'].mean()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Avg. Temperature", f"{avg_temp:.2f} °C")
    col2.metric("Avg. CO2 Emissions", f"{avg_co2:.2f} T/Capita")
    col3.metric("Total Extreme Events", f"{total_events:,.0f}")
    col4.metric("Avg. Renewable Energy", f"{avg_renewable:.2f} %")

    st.markdown("---")

    # --- Interactive World Map ---
    st.header("Geographical View of Climate Indicators")
    st.info(f"Choose an indicator to visualize on the world map.")
    map_indicator = st.selectbox(
        'Select Indicator for Map',
        options=['Avg Temperature (°C)', 'CO2 Emissions (Tons/Capita)', 'Renewable Energy (%)', 'Forest Area (%)']
    )

    map_df = filtered_df.groupby('Country')[map_indicator].mean().reset_index()

    fig_map = px.choropleth(
        map_df,
        locations="Country",
        locationmode="country names",
        color=map_indicator,
        hover_name="Country",
        color_continuous_scale=px.colors.sequential.Plasma,
        title=f"{map_indicator} Across Selected Countries"
    )
    fig_map.update_layout(margin={"r":0,"t":30,"l":0,"b":0})
    st.plotly_chart(fig_map, use_container_width=True)


    # --- Tabs for Detailed Charts ---
    st.header("Detailed Analysis")
    tab1, tab2 = st.tabs(["📈 Trend Analysis", "📊 Relationship Analysis"])

    with tab1:
        st.subheader("Trends of Climate Indicators Over Time")
        st.info(f"Choose an indicator to analyze its trend over time.")
        trend_indicator = st.selectbox(
            'Select Indicator to Analyze',
            options=df.columns.drop(['Year', 'Country']),
            key='trend_indicator'
        )
        trend_df = filtered_df.groupby('Year')[trend_indicator].mean().reset_index()
        
        fig_trend = px.line(
            trend_df,
            x='Year',
            y=trend_indicator,
            title=f'Average {trend_indicator} Over Time',
            markers=True
        )
        fig_trend.update_layout(xaxis_title='Year', yaxis_title=trend_indicator)
        st.plotly_chart(fig_trend, use_container_width=True)

    with tab2:
        col_rel_1, col_rel_2 = st.columns(2)
        with col_rel_1:
            st.subheader("Correlation Heatmap")
            corr = filtered_df.drop('Year', axis=1).corr(numeric_only=True)
            fig_heatmap, ax = plt.subplots(figsize=(8, 6))
            sns.heatmap(corr, annot=True, cmap='viridis', fmt=".2f", ax=ax, annot_kws={"size": 8})
            st.pyplot(fig_heatmap)

        with col_rel_2:
            st.subheader("CO2 Emissions vs. Temperature")
            fig_scatter = px.scatter(
                filtered_df,
                x='CO2 Emissions (Tons/Capita)',
                y='Avg Temperature (°C)',
                color='Country',
                hover_name='Country',
                title='CO2 Emissions vs. Average Temperature'
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

    st.header('Filtered Data Explorer')
    st.dataframe(filtered_df)

st.markdown("---")
st.markdown("Made By Team Tech Square | Data Source: Kaggle | Deployed on Streamlit Cloud")
