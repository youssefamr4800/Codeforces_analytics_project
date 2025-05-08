import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Title
# st.title("Codeforces Dashboard")

# Connect to PostgreSQL
conn = create_engine("postgresql+psycopg2://airflow:airflow@localhost:5432/codeforces")


# Query the data
df = pd.read_sql_query("SELECT * FROM contests", conn)

# Show dataframe
# st.dataframe(df)

@st.cache_data
def load_data():
    query = "SELECT * FROM contests"
    return pd.read_sql_query(query, conn)

df = load_data()
# print(df.head())
# Set the title of the dashboard
# Display the dataframe
st.subheader("Contests Data")
st.dataframe(df)

# Filter by contest type
st.sidebar.header("Filters")
contest_type = st.sidebar.selectbox("Select Contest Type", options=df['type'].unique())
filtered_df = df[df['type'] == contest_type]

st.subheader(f"Filtered Contests (Type: {contest_type})")
st.dataframe(filtered_df)

# Display summary statistics
st.subheader("Summary Statistics")
st.write((df["durationSeconds"]).describe())


# The name of longest contest and its duration
st.subheader("Longest Contest Duration")
longest_contest_duration = df['durationSeconds'].max()
st.write(longest_contest_duration / 60  , "minutes")
longest_contest = df.loc[df['durationSeconds'].idxmax(), 'name']
st.subheader("Longest Contest Name")
st.write(longest_contest)
# The name of the shortest contest and its duration
st.subheader("Shortest Contest Duration")
shortest_contest_duration = df['durationSeconds'].min()
st.write(shortest_contest_duration / 60 , "minutes")
shortest_contest = df.loc[df['durationSeconds'].idxmin(), 'name']
st.subheader("Shortest Contest Name")
st.write(shortest_contest)
# The number of contests
num_contests = df.shape[0]
st.subheader("Number of Contests")
st.write(num_contests)
# The number of contests by type
num_contests_by_type = df['type'].value_counts()
st.subheader("Number of Contests by Type")
st.bar_chart(num_contests_by_type)

