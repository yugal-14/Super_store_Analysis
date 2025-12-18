# -------------------------------
# Preparing the Environment
# -------------------------------
# Import libraries and alias for easy reading
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
%matplotlib inline

# Read in data in CSV format
superstore = pd.read_csv('/Users/katiehuang/Documents/Data Analytics/The Sparks Internship/Super Store/SampleSuperstore.csv')

# -------------------------------
# Data Exploration
# -------------------------------
# Preview first 5 rows of data set
superstore.head()

# Preview last 5 rows of data set
superstore.tail()

# Shape of data set
superstore.shape

# Summarised information of data set
superstore.info()

# -------------------------------
# Data Cleaning
# -------------------------------
# Handling Missing Values
# Find the number of null values for all columns
superstore.isnull().sum()

# Handling Duplicate Data
# Find the number of duplicate data
superstore.duplicated().sum()

# Show the duplicated rows
superstore[superstore.duplicated(keep = 'last')]

# Drop the duplicated rows
superstore.drop_duplicates(inplace = True)

# Find the no. of rows and columns after dropping duplicates
superstore.shape

# -------------------------------
# Calculated Field
# -------------------------------
# Create a Profit Margin column
superstore['Profit Margin %'] = (superstore.Profit / superstore.Sales) * 100
superstore.head(5)

# -------------------------------
# Descriptive Statistics
# -------------------------------
# Get descriptive statistics summary
superstore.describe(include = "all")

# -------------------------------
# 1. Which Category is Best Selling and Most Profitable?
# -------------------------------
# Group sales, profit and quantity by category
category_analysis = pd.DataFrame(superstore.groupby(['Category'])[['Sales', 'Profit', 'Quantity']].sum())

# Set for grouped plots - figure with a 1x3 grid of Axes
sns.set_theme(style="whitegrid")
figure, axis = plt.subplots(1, 3, figsize=(8, 5))

# Plot barplots
cat1 = sns.barplot(x = category_analysis.index, y = category_analysis.Sales, ax=axis[0])
cat2 = sns.barplot(x = category_analysis.index, y = category_analysis.Profit, ax=axis[1])
cat3 = sns.barplot(x = category_analysis.index, y = category_analysis.Quantity, ax=axis[2])

# Set titles
cat1.set(title = 'Sales')
cat2.set(title = 'Profit')
cat3.set(title = 'Quantity')

# Rotate axis for x-axis
plt.setp(cat1.get_xticklabels(), rotation = 'vertical', size = 9)
plt.setp(cat2.get_xticklabels(), rotation = 'vertical', size = 9)
plt.setp(cat3.get_xticklabels(), rotation = 'vertical', size = 9)

# Set spacing between subplots
figure.tight_layout()

# -------------------------------
# 2. Best Selling and Most Profitable Sub-Category
# -------------------------------
# Group by sub-category
subcat_analysis = pd.DataFrame(superstore.groupby(['Sub-Category'])[['Sales', 'Profit']].sum())

# Sort by descending order according to sales
subcat_sales = pd.DataFrame(subcat_analysis.sort_values('Sales', ascending = False))

# Sort by descending order according to profit
subcat_profit = pd.DataFrame(subcat_analysis.sort_values('Profit', ascending = False))

# Plot Bar Plots
sns.set_theme(style="whitegrid")
figure, axis = plt.subplots(1, 2, figsize=(12, 6))

# Plot Bar Plot for Best Selling Sub-Category
subcat1 = sns.barplot(data = subcat_sales, x = subcat_sales.index, y = subcat_sales.Sales, ax=axis[0])
subcat1.set(title="Best Selling Sub-Category")
subcat1.set_xticklabels(subcat1.get_xticklabels(),rotation = "vertical", size = 10)

# Plot Bar Plot for Most Profitable Sub-Category
subcat2 = sns.barplot(data = subcat_profit, x = subcat_profit.index, y = subcat_profit.Profit, ax=axis[1])
subcat2.set(title = "Most Profitable Sub-Category")
subcat2.set_xticklabels(subcat2.get_xticklabels(),rotation = "vertical", size = 10)

# Set spacing between subplots
figure.tight_layout()
plt.show()

# -------------------------------
# 3. Top Selling Sub-Category
# -------------------------------
subcat_quantity = pd.DataFrame(superstore.groupby(['Sub-Category'])[['Quantity']].sum().sort_values('Quantity',ascending=False))

# Plot Bar Plot for Top Selling Sub-Category
sns.set_theme(style="whitegrid")
sns.barplot(data = subcat_quantity, y = subcat_quantity.index, x = subcat_quantity.Quantity, palette = "muted")
plt.title("Top Selling Sub-Category")
plt.show()

# -------------------------------
# 4. Most Profitable Customer Segment
# -------------------------------
segment_analysis = pd.DataFrame(superstore.groupby(['Segment'])[['Profit']].sum())

# Plot Bar Plot
sns.set_theme(style="whitegrid")
sns.barplot(data = segment_analysis, x = segment_analysis.index, y = segment_analysis.Profit, palette = "rocket")
plt.title("Customer Segment Profitability")
plt.show()

# -------------------------------
# 5. Preferred Ship Mode
# -------------------------------
# Plot shipment mode
sns.set_theme(style="whitegrid")
sns.countplot(superstore['Ship Mode'])
plt.title("Ship Mode")
plt.show()

# -------------------------------
# 6. Most Profitable Region
# -------------------------------
region_analysis = pd.DataFrame(superstore.groupby(['Region'])['Profit'].sum().reset_index())

# Plot Pie Chart
explode = [0, 0, 0, 0.1]
plt.pie(region_analysis.Profit, labels = region_analysis.Region, startangle = 90, autopct = "%1.0f%%", explode = explode, shadow = True)
plt.title("Most Profitable by Region")
plt.show()

# -------------------------------
# 7. Cities with Highest Sales
# -------------------------------
city_sales = pd.DataFrame(superstore.groupby(['City'])[['Sales', 'Quantity']].sum().sort_values('Sales',ascending = False))

# Top 10 and Bottom 10 Cities
top10 = city_sales[:10]
bottom10 = city_sales[-10:]

# Set for grouped plots - figure with a 1x2 grid of Axes
figure, axis = plt.subplots(1, 2, figsize=(12, 5))
sns.set_theme(style="whitegrid")

# Top 10 Cities
top10c = sns.barplot(data = top10, y = top10.index, x = top10.Sales, palette = "coolwarm", ax = axis[0])
top10c.set(Title = "Top 10 Cities with Highest Sales")
top10c.set_yticklabels(top10c.get_yticklabels(),size = 10)

# Bottom 10 Cities
bottom10c = sns.barplot(data = bottom10, y = bottom10.index, x = bottom10.Sales, palette = "coolwarm", ax=axis[1])
bottom10c.set(Title = "Bottom 10 Cities with Lowest Sales")
bottom10c.set_yticklabels(bottom10c.get_yticklabels(),size = 10)

# Set spacing between subplots
figure.tight_layout()
plt.show()
