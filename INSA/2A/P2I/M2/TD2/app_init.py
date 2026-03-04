# web app
import streamlit as st

# DataFrame
import pandas as pd

# numerical calculations
import numpy as np

# interactive visualisation
import plotly.express as px
import plotly.graph_objects as go

# standard visualisation
import matplotlib.pyplot as plt

# stats package
from scipy import stats

# dates
from datetime import datetime, timedelta


def main():
    """
    The logic of the app will be written here.
    """
    print("Hello, world!")
    # create a header
    st.header("Mon appli")
    st.markdown(
        """Chaque année, nous estimons qu'en France plusieurs dizaines de milliers de décès sont dûs à une mauvaise qualité de l'air, et plusieurs millions dans le monde. C'est pourquoi de nombreuses villes étudient et publient un **indice de qualité de l'air** ayant pour but : l'évaluation de la qualité de l'air, l'aide à la décision, et la communication au public. En France, pour les agglomérations de plus de 100 000 habitants, l'indice retenu est l'indice ATMO. Il vise à étudier la qualité de l'air en mesurant les concentrations de dioxyde de souffre SO2, dioxyde d'azote, d'ozone NO2, et de particules en suspension (les particules de diamètre aérodynamique inférieur à 10 micromètres, ${PM}_{10}$ et les particules de diamètre aérodynamique inférieur à 2,5 micromètres $PM2,5$) à l'échelle d'une agglomération ou d'une région. Fréquence de mise à jour : quotidienne à 14H locales. Source: [Indice ATMO](https://www.data.gouv.fr/fr/datasets/indice-atmo/#/resources)"""
    )
    data = load_data()
    if st.sidebar.checkbox("Affichez les données brut", False):
        st.write(data)
    all_stats = [
        "count",
        "moyenne",
        "écart-type",
        "variance",
        "min",
        "1er quartile",
        "médiane",
        "3ème quartile",
        "max",
    ]
    def_stats = ["moyenne", "écart-type", "médiane"]
    list_stats_to_show = st.sidebar.multiselect(
        "Statistiques à afficher",
        options=all_stats,
        default=def_stats,
        key="multi-stats",
    )
    st.sidebar.subheader("Visualisation")
    st.sidebar.checkbox("Cacher", True)
    select = st.sidebar.selectbox(
        "Visualisation type",
        ["Histogram", "Box Plot", "Probability Density"],
        key="viz",
    )

    thres = st.sidebar.slider(
        "Seuil à ne pas dépasser", min_value=10, max_value=100, value=40
    )

    min_date = data["date_dif"].min()
    max_date = data["date_dif"].max()

    # Add date picker to sidebar
    start_date = st.sidebar.date_input(
        "Start date",
        value=min_date,  # default value
        min_value=min_date,
        max_value=max_date,
    )

    # Add date picker to sidebar
    end_date = st.sidebar.date_input(
        "End date",
        value=max_date,  # default value
        min_value=min_date,
        max_value=max_date,
    )
    stats_map = {
        "count": "count",
        "moyenne": "mean",
        "écart-type": "std",
        "variance": "std",
        "min": "min",
        "1er quartile": "25%",
        "médiane": "50%",
        "3ème quartile": "75%",
        "max": "max",
    }
    conv = []
    for stat in list_stats_to_show:
        conv.append(stats_map[stat])
    stats_to_show = data.describe()["conc_pm10"].loc[conv]
    st.write(stats_to_show)

    if select == "Box Plot":
        # create a boxplot
        fig = px.box(data["conc_pm10"], title="PM10: boxplot")
        # display it
        st.plotly_chart(fig)
    if select == "Histogram":
        # create a histogram
        fig = px.histogram(
            data["conc_pm10"][(data["conc_pm10"] < thres)],
            title="Histogramme concentration pm10",
            color_discrete_sequence=["darkcyan"],
            opacity=0.75,
        )
        # display it
        st.plotly_chart(fig)
    if select == "Probability Density":
        fig = px.histogram(
            data["conc_pm10"][data["conc_pm10"] < thres],
            title="Histogramme concentration pm10",
            color_discrete_sequence=["darkcyan"],
            opacity=0.75,
            marginal="box",
        )
        fig = add_density(fig, data["conc_pm10"][data["conc_pm10"] < thres])
        st.plotly_chart(fig)

    villes_uniques = data["lib_zone"].dropna().unique()
    list_lyon = ["Lyon", "Villeurbanne", "Feyzin", "Vénissieux"]
    list_grenoble = ["Grenoble", "Gières", "Meylan", "Eybens", "Fontaine"]
    zone_1_txt = st.sidebar.text_input("Nom de la zone", key="txt1")

    df_lyon = (data[data["lib_zone"].isin(list_lyon)])[
        ["X", "Y", "lib_zone", "conc_pm10"]
    ]
    df_grenoble = (data[data["lib_zone"].isin(list_grenoble)])[
        ["X", "Y", "lib_zone", "conc_pm10"]
    ]

    # add area column
    df_lyon["area"] = "Lyon"
    df_grenoble["area"] = "Grenoble"

    conca_pm10 = pd.concat([df_lyon, df_grenoble])
    conca_pm10 = conca_pm10.reset_index()

    fig = px.box(conca_pm10, x="area", y="conc_pm10")

    map = px.scatter_mapbox(
        conca_pm10,
        lat="Y",  #  latitude column name
        lon="X",  #  longitude column name
        color="area",  # color points by area
        hover_name="lib_zone",  # city names on hover
        mapbox_style="open-street-map",  # or 'open-street-map', 'stamen-terrain'
        zoom=10,
    )

    # Center the map on your data
    map.update_layout(
        mapbox=dict(center=dict(lat=conca_pm10["Y"].mean(), lon=conca_pm10["X"].mean()))
    )

    st.plotly_chart(map)

    concentrations = data[["conc_o3", "conc_pm10"]].isin(list_lyon)
    corr = concentrations.corr()
    plot_heatmap(corr)


def plot_heatmap(corr):
    # Plot heatmap
    fig = px.imshow(
        corr, color_continuous_scale="RdBu_r", aspect="auto"  # Red-Blue scale
    )

    # Add text annotations:
    for i in range(len(corr.columns)):
        for j in range(len(corr.index)):
            fig.add_annotation(
                x=i, y=j, text=str(round(corr.iloc[j, i], 2)), showarrow=False
            )

    st.plotly_chart(fig)


def add_density(fig, df):
    # Calculate the KDE
    kde_x = np.linspace(df.min(), df.max(), 100)
    kde = stats.gaussian_kde(df)
    kde_y = kde(kde_x)

    # Add the KDE as a line trace
    fig.add_traces(
        go.Scatter(x=kde_x, y=kde_y, name="Density", line=dict(color="red", width=2))
    )

    return fig


@st.cache_data(persist=True)
def load_data(filename="data/Indice_ATMO_ARA.csv"):
    """
    Load the data from a csv file.
    """
    df = pd.read_csv(filename)

    df["date_dif"] = pd.to_datetime(df["date_dif"])
    df["date_ech"] = pd.to_datetime(df["date_ech"])

    return df


if __name__ == "__main__":
    main()

# to run the app, run in the terminal:
# streamlit run app_init.py
# in the browser a new page will be opened
