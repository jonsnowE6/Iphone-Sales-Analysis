#!/usr/bin/env python
# coding: utf-8

# # 📊 A SALES ANALYSYS USING PYTHON
# ### An Extra Ordinary Data Analysys Of Iphone Sales Using Python
# **Tools Used**
# Python | Numpy | Pandas | Matplotlib | Seaborn | Plotly
# 
# **Objective:**
# To analyse sales data,identify important trends and patterns,
# and generate actionable buisness insights

# 

# ## Loading the Dataset and Overview

# In[8]:


import pandas as pd
raw_data=pd.read_csv(r"C:\Users\SIBASISH\Downloads\apple_products.csv")
raw_data.info()


# In[9]:


raw_data.describe()


# ## Cleaning Of Dataset

# In[12]:


raw_data.isnull().sum()


# In[11]:


final_raw_data=raw_data.dropna()
final_raw_data.isnull().sum()


# In[13]:


final_raw_data.duplicated().sum()


# ## Price Analysis

# In[90]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(final_raw_data["Sale Price"])
plt.show()


# ### Analysis
# 
# The sale prices of the iPhones in the dataset range from ₹29,999 to ₹1,40,900. The distribution shows that the products are spread across a wide range of price segments, from relatively affordable models to premium models.
# 
# The median sale price is ₹75,900, while the mean sale price is approximately ₹80,074. This indicates that the dataset contains a significant number of higher-priced models that raise the average selling price.

# In[39]:


top_10_expensive=final_raw_data.sort_values(by=["Sale Price"],ascending=False).head(10)
top_10_expensive


# In[43]:


import plotly.express as px
fig1=px.bar(
    top_10_expensive,
    x="Product Name",
    y="Sale Price",
    title="Top 10 Expensive product"
)
fig1.show()


# ### Analysis
# 
# The analysis shows that the most expensive products are primarily Pro and Pro Max variants with higher storage capacities.
# 
# The highest sale price in the dataset is ₹1,40,900, observed for the iPhone 12 Pro 512 GB variants. The iPhone 11 Pro Max 256 GB variants are also positioned among the highest-priced products.
# 
# This indicates that the Pro/Pro Max series and higher storage configurations occupy the premium segment of the dataset.

# # Discount Analysis

# In[32]:


sns.histplot(final_raw_data["Discount Percentage"])
plt.show()            


# In[44]:


top_discount=final_raw_data.sort_values(by=["Discount Percentage"],ascending=False).head(10)
top_discount


# In[49]:


import plotly.express as px
fig2=px.bar(
    top_discount,
    x="Product Name",
    y="Discount Percentage",
    title="top discount percentage"
)
fig2.show()


# ### Analysis
# 
# The discount percentage varies considerably across the products, ranging from 0% to 29%.
# 
# The highest discount observed is 29%, offered on the iPhone 11 Pro 64 GB. Several iPhone SE and iPhone XR variants also have relatively high discounts.
# 
# This suggests that discounts are not uniformly distributed across the product range and that older or lower-priced models may receive relatively larger percentage discounts.

# # Customer Rating Analysis

# In[33]:


sns.histplot(final_raw_data["Star Rating"])
plt.show()


# In[50]:


highest_rated=final_raw_data.sort_values(by=["Star Rating"],ascending=False).head(10)
highest_rated


# In[54]:


fig3=px.bar(
    highest_rated,
    x="Product Name",
    y="Star Rating",
    title="highest rated products"
)
fig3.show()


# ### Analysis
# 
# Customer ratings are highly concentrated between 4.5 and 4.7 stars, indicating consistently positive customer feedback across the products in the dataset.
# 
# The highest rating is 4.7 stars, achieved by several iPhone 11 Pro Max variants.
# 
# The relatively small variation in ratings suggests that customer satisfaction is generally high across the products, making price, discount and popularity more useful variables for differentiating products.

# # Analysis Of Number Of Rating

# In[55]:


highest_number_rating=final_raw_data.sort_values(by=["Number Of Ratings"],ascending=False).head(10)
highest_number_rating


# In[56]:


fig4=px.bar(
    highest_number_rating,
    x="Product Name",
    y="Number Of Ratings",
    title="highest number of rating"
)
fig4.show()


# ### Analysis
# 
# The number of ratings varies substantially across the products.
# 
# The most-rated products are primarily older and relatively affordable models such as the iPhone SE and iPhone XR. In contrast, several premium models have considerably fewer ratings.
# 
# This suggests that product popularity, affordability and market availability may have a stronger relationship with the number of customer ratings than the selling price alone.

# # Review Analysis

# In[59]:


highest_reviews=final_raw_data.sort_values(by=["Number Of Reviews"],ascending=False).head(10)
highest_reviews


# In[61]:


fig5=px.bar(
    highest_reviews,
    x="Product Name",
    y="Number Of Reviews",
    title="Highest Number Of Reviews"
)
fig5.show()


# ### Analysis
# 
# The number of reviews is strongly concentrated among a small group of products.
# 
# The iPhone SE variants have the highest number of reviews, reaching more than 8,000 reviews in the dataset. These products also have very high numbers of ratings.
# 
# This indicates that the products with the largest customer engagement are not necessarily the most expensive products. Instead, several lower-priced models have accumulated substantially more customer interaction.

# # comparison
# ## Price vs Rating

# In[63]:


figure1=px.scatter(
    final_raw_data,
    x="Sale Price",
    y="Star Rating",
    hover_name="Product Name",
    trendline="ols",
    title="sale price vs star rating"
)
figure1.show()


# ### Analysis
# 
# The scatter plot shows a slight positive relationship between sale price and star rating.
# 
# However, the relationship is relatively weak, with a correlation of approximately 0.30. Therefore, higher-priced products do not necessarily receive substantially higher customer ratings.
# 
# Overall, customer ratings remain relatively high across different price levels.

# ## Discount vs Rating

# In[65]:


figure2=px.scatter(
    final_raw_data,
    x="Discount Percentage",
    y="Star Rating",
    hover_data="Product Name",
    title="discount vs rating",
    trendline="ols"
)
figure2.show()


# ### Analysis
# 
# The scatter plot indicates a weak negative relationship between discount percentage and star rating.
# 
# The correlation coefficient is approximately -0.35, suggesting that products with larger discounts tend to have slightly lower ratings in this dataset.
# 
# However, the relationship is not strong enough to conclude that discounts directly cause lower customer ratings. Other product characteristics may also influence customer satisfaction.

# ## Ram vs Sales Price

# In[69]:


figure3=px.box(
    final_raw_data,
    x="Ram",
    y="Sale Price",
    title="ram vs sales price",
    points="all"
)
figure3.show()


# ### Analysis
# 
# The box plot shows a general increase in sale price across higher RAM configurations.
# 
# The 6 GB RAM products have the highest average sale price at approximately ₹1.02 lakh, while 2 GB RAM products have an average price of approximately ₹56,192.
# 
# The 3 GB category contains only one product, so it should not be used for a strong comparison.
# 
# Overall, higher RAM configurations are associated with higher prices in this dataset.

# ## Ram vs Rating

# In[70]:


figure4=px.box(
    final_raw_data,
    x="Ram",
    y="Star Rating",
    title="Ram vs Rating",
    points="all"
)
figure4.show()


# ### Analysis
# 
# The ratings remain relatively consistent across the different RAM configurations.
# 
# The average ratings for the major RAM categories are all close to 4.5–4.6 stars. Therefore, RAM appears to have little practical relationship with customer ratings in this dataset.
# 
# This suggests that higher RAM configurations command higher prices but do not necessarily provide higher customer ratings.

# ## Review vs Rating

# In[71]:


figure5=px.scatter(
    final_raw_data,
    x="Number Of Ratings",
    y="Number Of Reviews",
    title="number of rating vs number of review",
    hover_data="Product Name",
    trendline="ols"
)
figure5.show()


# ### Analysis
# 
# The scatter plot shows an extremely strong positive relationship between the number of ratings and the number of reviews.
# 
# The correlation coefficient is approximately 0.999, indicating that products with a higher number of ratings also tend to have a higher number of reviews.
# 
# This is expected because ratings and reviews are both measures of customer engagement. Therefore, they provide similar information about product popularity within this dataset.

# ## MRP vs Sales Price

# In[72]:


figure6=px.scatter(
    final_raw_data,
    x="Mrp",
    y="Sale Price",
    title="MRP vs sales price",
    hover_data="Product Name",
    trendline="ols",
    size="Discount Percentage"
)
figure6.show()


# ### Analysis
# 
# The scatter plot shows a very strong positive relationship between MRP and Sale Price.
# 
# The correlation coefficient is approximately 0.985, indicating that products with higher MRP generally have higher selling prices.
# 
# The difference between MRP and Sale Price represents the discount offered to customers. The size of the points also helps identify products with relatively larger discount percentages.
# 
# Therefore, MRP is a strong indicator of the final selling price in this dataset.

# ## Correlation Heatmap

# In[89]:


numeric_cols=[
    "Sale Price",
    "Mrp",
    "Discount Percentage",
    "Number Of Ratings",
    "Number Of Reviews",
    "Star Rating"
]
correlation=final_raw_data[numeric_cols].corr()
figure7=px.imshow(
    correlation,
    text_auto=".2f",
    title="corrlelation matrix Iphone sales variables"
)
fig.update_layout(
    width=1200,
    height=1000,
    title_font_size=50
)
fig.update_traces(
    textfont_size=100
)
figure7.show()


# ### Analysis
# 
# The correlation matrix highlights several important relationships among the numerical variables.
# 
# The strongest positive relationship is between MRP and Sale Price, with a correlation of approximately 0.985. This indicates that higher-MRP products generally have higher selling prices.
# 
# The number of ratings and number of reviews also have an extremely strong positive correlation of approximately 0.999.
# 
# Sale Price has a negative relationship with both Number of Ratings (-0.702) and Number of Reviews (-0.696), indicating that lower-priced products in this dataset tend to have greater customer engagement.
# 
# Discount Percentage shows a moderate negative relationship with Sale Price (-0.570), suggesting that products with higher discounts tend to have lower selling prices.
# 
# Overall, price, discount and customer engagement show meaningful relationships, while Star Rating varies only slightly across products.

# # 💡 Key Business Insights
# 
# 1. **Premium segment:** Pro and Pro Max models with higher storage configurations occupy the highest price segment.
# 
# 2. **Discount strategy:** Discounts range from 0% to 29%, with some older/lower-priced models receiving relatively higher discounts.
# 
# 3. **Customer satisfaction:** Star ratings are consistently high, ranging from 4.5 to 4.7 stars.
# 
# 4. **Product popularity:** Lower-priced models such as iPhone SE and iPhone XR have substantially higher numbers of ratings and reviews than many premium models.
# 
# 5. **Price and rating:** Sale price has only a weak positive relationship with star rating, suggesting that higher price does not necessarily translate into higher customer satisfaction.
# 
# 6. **RAM and price:** Higher RAM configurations, particularly 6 GB models, generally have higher selling prices.
# 
# 7. **RAM and rating:** RAM configuration does not show a meaningful difference in customer ratings.
# 
# 8. **Customer engagement:** Number of ratings and number of reviews have an extremely strong positive relationship.
# 
# 9. **MRP and sale price:** MRP and sale price are very strongly positively correlated, indicating that MRP is closely associated with the final selling price.

# # 🎯 Recommendations
# 
# - Maintain differentiated pricing for premium Pro and Pro Max models.
# 
# - Use higher discounts strategically on older or lower-priced models to improve their competitiveness.
# 
# - Consider customer engagement, not just star rating, when evaluating product popularity.
# 
# - Monitor highly rated products with lower customer engagement separately from highly popular products.
# 
# - Use MRP as an important reference point when designing pricing and discount strategies.
# 
# - Higher RAM configurations can be positioned as premium products because they are associated with higher selling prices in this dataset.
# 
# - Avoid using star rating alone to evaluate product success because ratings are very similar across most products.

# In[ ]:




