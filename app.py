# sa-province-digital-analysis/app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="SA Provincial Digital Economy", layout="wide")

st.title("🇿🇦 South African Provincial Digital Economy")
st.caption("Analyzing the digital divide between provinces - Gauteng vs Rural Areas")

# Data
data = {
    'Province': ['Gauteng', 'Western Cape', 'KwaZulu-Natal', 'Free State', 
                 'Mpumalanga', 'Eastern Cape', 'Limpopo', 'Northern Cape', 'North West'],
    'Large_Enterprises': [68, 55, 40, 30, 28, 22, 18, 16, 20],
    'SMEs': [25, 18, 12, 9, 8, 6, 5, 4, 5]
}
df = pd.DataFrame(data)

# Sidebar
st.sidebar.header("Filter Data")
show_sme = st.sidebar.checkbox("Show SME data", value=True)

# Main
st.subheader("📊 Provincial Digital Adoption")

df_melted = df.melt(id_vars='Province', var_name='Enterprise Size', value_name='Adoption %')
if not show_sme:
    df_melted = df_melted[df_melted['Enterprise Size'] == 'Large_Enterprises']

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df_melted, x='Province', y='Adoption %', hue='Enterprise Size', palette='coolwarm', ax=ax)
plt.ylim(0, 80)
plt.title('Digital Adoption by Province')
st.pyplot(fig)

# The Gap Analysis
st.subheader("📉 The Gauteng vs Limpopo Gap")
col1, col2, col3 = st.columns(3)
col1.metric("🏙️ Gauteng (Urban)", "68%", "Highest")
col2.metric("🌾 Limpopo (Rural)", "18%", "Lowest")
col3.metric("📊 The Gap", "50%", "Massive Opportunity")

st.info("""
**💡 What this means for FNB:**
- There is a massive digital divide between urban and rural provinces.
- FNB can capture the rural market by offering affordable data bundles, 
  simplified mobile banking, and SME digital training in Limpopo, EC, and NC.
- This data supports a business case for a 'Rural Digital Transformation Fund'.
""")
