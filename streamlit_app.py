import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 StatBot Pro - CSV Data Analyzer")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    option = st.selectbox(
        "Choose Analysis",
        [
            "Total Sales",
            "Average Revenue",
            "Highest Sales Region",
            "Plot Sales",
            "Plot Revenue",
            "Monthly Sales",
            "Total Revenue",
            "Region Sales"
        ]
    )

    if option == "Total Sales":
        st.write("Total Sales:", df["Sales"].sum())

    elif option == "Average Revenue":
        st.write("Average Revenue:", df["Revenue"].mean())

    elif option == "Highest Sales Region":
        max_region = df.loc[df["Sales"].idxmax()]["Region"]
        st.write("Region with Highest Sales:", max_region)

    elif option == "Plot Sales":
        fig, ax = plt.subplots()
        ax.plot(df["Date"], df["Sales"], marker='o')
        ax.set_title("Sales Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Sales")
        st.pyplot(fig)

    elif option == "Plot Revenue":
        fig, ax = plt.subplots()
        ax.plot(df["Date"], df["Revenue"], marker='o')
        ax.set_title("Revenue Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Revenue")
        st.pyplot(fig)

    elif option == "Monthly Sales":
        monthly = df.resample("M", on="Date")["Sales"].sum()
        st.write(monthly)

    elif option == "Total Revenue":
        st.write("Total Revenue:", df["Revenue"].sum())

    elif option == "Region Sales":
        st.write(df.groupby("Region")["Sales"].sum())

else:
    st.info("Please upload a CSV file to begin.")