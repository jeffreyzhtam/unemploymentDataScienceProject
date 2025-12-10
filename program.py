import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set a Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")  # larger fonts for better readability

# Reads in data
df = pd.read_csv("youth_unemployment_global.csv")

# Clean data: drop NaN and duplicates
df_clean = df.dropna().drop_duplicates().reset_index(drop=True)
print(df_clean.columns)

# -------------------------------------------------------
# Q. What does the unemployment rate look like over the years
# 1. Average Global Youth Unemployment Over Time

# Find the latest year
latest_year = df_clean['Year'].max()

# Filter for the latest year
latest_df = df_clean[df_clean['Year'] == latest_year]

# Get the 10 countries with the lowest youth unemployment
lowest10 = latest_df.sort_values('YouthUnemployment', ascending=True).head(10)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(data=lowest10, x='YouthUnemployment', y='Country', palette='Greens_r')
plt.title(f"Top 10 Countries with Lowest Youth Unemployment ({latest_year})", fontsize=16, weight='bold')
plt.xlabel("Youth Unemployment (%)", fontsize=14)
plt.ylabel("Country", fontsize=14)
plt.tight_layout()
plt.savefig("youth_unemployment.png")
plt.show()
# -------------------------------------------------------
# Q - Which countries has the most unemployment and why
# 2. Top 10 Countries by Youth Unemployment (Latest Year)

latest_year = df_clean["Year"].max()
latest_df = df_clean[df_clean["Year"] == latest_year]
top10 = latest_df.sort_values('YouthUnemployment', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top10, x='YouthUnemployment', y='Country', palette='Reds_r')
plt.title(f"Top 10 Countries by Youth Unemployment ({latest_year})", fontsize=16, weight='bold')
plt.xlabel("Youth Unemployment (%)", fontsize=14)
plt.ylabel("Country", fontsize=14)
plt.tight_layout()
plt.savefig("top_10_unemployment.png")
plt.show()

# -------------------------------------------------------
# Q - How does US unemployment compare to the world
# 3. Global vs US Youth Unemployment Over Time

global_yearly = df_clean.groupby("Year")['YouthUnemployment'].mean().reset_index()
us_yearly = df_clean[df_clean['Country'].str.contains("United States", case=False)] \
    .groupby("Year")['YouthUnemployment'].mean().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(x=global_yearly["Year"], y=global_yearly['YouthUnemployment'], marker="o", label="Global Average", linewidth=2, color='navy')
sns.lineplot(x=us_yearly["Year"], y=us_yearly['YouthUnemployment'], marker="o", label="United States", linewidth=2, color='orange')
plt.title("US Youth Unemployment vs Global Average", fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=14)
plt.ylabel("Youth Unemployment (%)", fontsize=14)
plt.legend(fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("us_vs_world_unemployment.png")
plt.show()
