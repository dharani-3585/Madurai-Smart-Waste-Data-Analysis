import streamlit as st
import pandas as pd
import os

# Namma step 1-la create panna file-oda exact address
csv_file = r"C:\Data analyst\MSDB-DATA ANALYSIS\madurai_waste_data.csv"

st.title("🏙️ Madurai Smart Bin Dashboard (MSDB)")

if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    
    # Dropdown to select Ward
    ward = st.sidebar.selectbox("Select Madurai Ward", df['Location'].unique())
    ward_data = df[df['Location'] == ward]
    
    # Metric Boxes
    st.header(f"Live Stats for {ward}")
    st.metric("Total Logs Analyzed", len(ward_data))
    
    critical_count = len(ward_data[ward_data['Status'] == 'Critical'])
    st.metric("Critical Alerts (Action Needed)", critical_count)

    # Graph
    st.subheader("Waste Level Graph")
    st.bar_chart(ward_data['Status'].value_counts())
else:
    st.error(f"❌ Error: {csv_file} file kandupudikka mudiyala. Check step 1!")