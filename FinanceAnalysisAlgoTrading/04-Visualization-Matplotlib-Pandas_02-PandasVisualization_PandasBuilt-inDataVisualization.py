#!/usr/bin/env python
# coding: utf-8
# # Pandas Built-in Data Visualization
# In this lecture we will learn about pandas built-in capabilities for data visualization! It's built-off of matplotlib, but it baked into pandas for easier usage!  
import numpy as np
import pandas as pd

get_ipython().run_line_magic('matplotlib', 'inline')
# ## The Data
# There are some fake data csv files you can read in as dataframes:
df1 = pd.read_csv('Data/04-Visualization-Matplotlib-Pandas_df1.csv', index_col=0)
df2 = pd.read_csv('Data/04-Visualization-Matplotlib-Pandas_df2.csv')
# ## Style Sheets
# Matplotlib has [style sheets](http://matplotlib.org/gallery.html#style_sheets) you can use to make your plots look a little nicer. These style sheets include plot_bmh,plot_fivethirtyeight,plot_ggplot and more. They basically create a set of style rules that your plots follow. I recommend using them, they make all your plots have the same look and feel more professional. You can even create your own if you want your company's plots to all have the same look (it is a bit tedious to create on though).
# **Before plt.style.use() your plots look like this:**
df1['A'].hist_df()
# Call the style:
# In[4]:
import matplotlib.pyplot as plt

plt.style.use('ggplot')
# Now your plots look like this:
# In[5]:
df1['A'].hist_df()
# In[6]:
plt.style.use('bmh')
df1['A'].hist_df()
# In[7]:
plt.style.use('dark_background')
df1['A'].hist_df()
# In[8]:
plt.style.use('fivethirtyeight')
df1['A'].hist_df()
# In[9]:
plt.style.use('ggplot')
# Let's stick with the ggplot style and actually show you how to utilize pandas built-in plotting capabilities!
# * df.plot.area     
# * df.plot.barh     
# * df.plot.density  
# * df.plot.hist     
# * df.plot.line     
# * df.plot.scatter
# * df.plot.bar      
# * df.plot.box      
# * df.plot.hexbin   
# * df.plot.kde      
# * df.plot.pie
# You can also just call df.plot(kind='hist') or replace that kind argument with any of the key terms shown in the list above (e.g. 'box','barh', etc..)
df2.plot.area(alpha=0.4)
df2.head()
df2.plot.bar()
df2.plot.bar(stacked=True)
# ## Histograms
df1['A'].plot.hist_df(bins=50)
# ## Line Plots
df1.plot.line(x=df1.index, y='B', figsize=(12, 3), lw=1)
# ## Scatter Plots
df1.plot.scatter(x='A', y='B')
# You can use c to color based off another column value
# Use cmap to indicate colormap to use. 
# For all the colormaps, check out: http://matplotlib.org/users/colormaps.html
df1.plot.scatter(x='A', y='B', c='C', cmap='coolwarm')
# Or use s to indicate size based off another column. s parameter needs to be an array, not just the name of a column:
df1.plot.scatter(x='A', y='B', s=df1['C'] * 200)
# ## BoxPlots
df2.plot.box()  # Can also pass a by= argument for groupby
# ## Hexagonal Bin Plot
# Useful for Bivariate Data, alternative to scatterplot:
df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot.hexbin(x='a', y='b', gridsize=25, cmap='Oranges')
# ## Kernel Density Estimation plot (KDE)
df2['a'].plot.kde()
df2.plot.density()
# That's it! Hopefully you can see why this method of plotting will be a lot easier to use than full-on matplotlib, it balances ease of use with control over the figure. A lot of the plot calls also accept additional arguments of their parent matplotlib plt. call. 
# # Great Job!
