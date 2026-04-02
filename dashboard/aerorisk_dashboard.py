import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("AeroRisk Intelligence Platform")

st.write("Global Aviation Route Risk Analysis")

DATA_FILE = "route_risk_results.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    return df


df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Risk Distribution")

fig, ax = plt.subplots()
ax.hist(df["risk_score"], bins=20)
ax.set_xlabel("Risk Score")
ax.set_ylabel("Frequency")

st.pyplot(fig)


st.subheader("Top Risk Routes")

top_risk = df.sort_values(by="risk_score", ascending=False).head(10)

st.table(top_risk)