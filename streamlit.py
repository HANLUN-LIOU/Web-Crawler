import streamlit as st
import matplotlib.pyplot as plt
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('weather_data2.db')
c = conn.cursor()

# Streamlit app
st.title("Weather Data Visualization")

# Define the data retrieval function
def fetch_data(location):
    c.execute("SELECT date, max_temp, min_temp FROM weather WHERE location=?", (location,))
    data = c.fetchall()
    return data

# Define the data
regions = ["北部地區", "中部地區", "南部地區", "東北部地區", "東部地區", "東南部地區"]

# Dropdown to select region
selected_region = st.selectbox("選擇地區", regions)

# Fetch data from the database
data = fetch_data(selected_region)

# Process fetched data
days_data = [day[0] for day in data]
max_temps_data = [int(temp[1]) for temp in data]
min_temps_data = [int(temp[2]) for temp in data]

# Plotting the data
plt.rc('font', family='Microsoft JhengHei')
plt.figure(figsize=(10, 6))
plt.plot(days_data, max_temps_data, marker='o', label='最高溫度')
plt.plot(days_data, min_temps_data, marker='o', label='最低溫度')
plt.xlabel("日期")
plt.ylabel("溫度 (°C)")
plt.title(f"{selected_region} 一週最高/最低溫度")
plt.legend()
plt.xticks(rotation=45)
st.pyplot(plt)

# Close the database connection
conn.close()
