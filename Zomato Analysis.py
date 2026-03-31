# Zomato Restaurant Data Analysis - Professional Version

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os  # For safe file path handling

# Step 2: Load Dataset Safely
# Get current folder where this Python script is located
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "zomato_dataset.xlsx")

# Load Excel file
try:
    df = pd.read_excel(file_path)
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print(f"Error: Excel file not found at {file_path}")
    exit()  # Stop script if file is missing

# Step 3: Explore Dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMissing Values per Column:")
print(df.isnull().sum())

# Step 4: Clean the Data
df = df.drop_duplicates()
df = df.dropna()
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')  # Convert ratings to numeric

# Step 5: Analysis

# 5.1 Number of Restaurants by City
restaurants_city = df['Location'].value_counts()
print("\nRestaurants by City:")
print(restaurants_city)

# 5.2 Average Rating by City
avg_rating_city = df.groupby('Location')['Rating'].mean().sort_values(ascending=False)
print("\nAverage Rating by City:")
print(avg_rating_city)

# 5.3 Most Popular Cuisines
top_cuisine = df['Cuisine'].value_counts()
print("\nMost Popular Cuisines:")
print(top_cuisine.head(10))

# 5.4 Top Rated Restaurants
top_restaurants = df.sort_values(by='Rating', ascending=False).head(10)
print("\nTop 10 Restaurants by Rating:")
print(top_restaurants[['Restaurant','Location','Cuisine','Rating']])

# Step 6: Visualization
sns.set_style("whitegrid")

# 6.1 Restaurants by City
plt.figure(figsize=(8,5))
sns.barplot(x=restaurants_city.index, y=restaurants_city.values, palette="viridis")
plt.title("Number of Restaurants by City")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.show()

# 6.2 Average Rating by City
plt.figure(figsize=(8,5))
sns.barplot(x=avg_rating_city.index, y=avg_rating_city.values, palette="magma")
plt.title("Average Rating by City")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# 6.3 Most Popular Cuisines
plt.figure(figsize=(8,5))
sns.barplot(x=top_cuisine.values[:10], y=top_cuisine.index[:10], palette="coolwarm")
plt.title("Top 10 Most Popular Cuisines")
plt.xlabel("Number of Restaurants")
plt.ylabel("Cuisine")
plt.tight_layout()
plt.show()

# 6.4 Cost vs Rating Scatter
plt.figure(figsize=(8,5))
sns.scatterplot(x=df['Cost_for_two'], y=df['Rating'], hue=df['Location'], palette="tab10")
plt.title("Cost vs Rating by Restaurant")
plt.xlabel("Cost for Two (INR)")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()

# 6.5 Rating Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Rating'], bins=10, kde=True, color="teal")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 6.6 Correlation Heatmap (numeric columns only)
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# Step 7: Save Cleaned Data
cleaned_file_path = os.path.join(folder_path, "cleaned_zomato_data.csv")
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved as '{cleaned_file_path}'")