import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns
import os

################### Reading Image and data set ###############
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "outlier.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "iris.csv")

############## Title ############

st.title("Outlier Handling - Iris Data")

############ Defination ##########

st.markdown(
    '''
    #### Outliers 
    - An **Outlier** is a data-item/object that deviates significantly from the rest of the (so-called normal)objects.
    - They can be caused by measurement or execution errors.
    - Or can have significant meaning depends upon use case.
    #### How to detect ?
    - Graghically - **Box plot** is widely used to detect Outlier.
    - Theoratically - For Detecting and Removing **Inter Quartile Range** is used for Outliers.
    '''
)

########## Image ##########

img = image.imread(IMAGE_PATH)
st.image(img)

########### Detection #########

st.markdown(''' ### Graghically Detecting''')

st.code('''# Reading the CSV file
df = pd.read_csv("Iris.csv")
 
# Printing top 5 rows
df.head()''')

st.markdown(''' ##### Output: ''')
df = pd.read_csv(DATA_PATH)
st.dataframe(df.iloc[0:5])

st.code('''# Orginal Shape of the dataset
df.shape''')
st.markdown(''' ##### Output: ''')
st.code(" (150,6)")

st.markdown(''' ##### Graphical Representation: 
    - Using Box Plot
''')
st.code('''# Box plot
# importing packages
import seaborn as sns
 
sns.boxplot(x='SepalWidthCm', data=df)''')
st.markdown(''' ##### Output: ''')
fig_1 = px.box(df, y="SepalWidthCm")
st.plotly_chart(fig_1, use_container_width=True)

st.write(''' In the above graph, the values above 4 and below 2.2 are acting as outliers
''')

########### Removing Outliers ############

st.markdown(''' ##### Removing Outliers: 
    - Using Inter Quartile Range
''')

st.code('''# IQR
# importing packages
import numpy as np
 
Q1 = np.percentile(df['SepalWidthCm'], 25, interpolation = 'midpoint')
 
Q3 = np.percentile(df['SepalWidthCm'], 75, interpolation = 'midpoint')
IQR = Q3 - Q1

# Upper bound
upper = (Q3+1.5*IQR)
 
# Lower bound
lower = (Q1-1.5*IQR)

Print("Upper Bound: ", upper)
Print("Lower Bound: ", lower)

new_df = df[(df['SepalWidthCm'] < upper) & (df['SepalWidthCm'] > lower)]

# New shape after outlier removal
new_df.shape''')

st.markdown(''' ##### Output: ''')

Q1 = np.percentile(df['SepalWidthCm'], 25, interpolation = 'midpoint')
 
Q3 = np.percentile(df['SepalWidthCm'], 75, interpolation = 'midpoint')
IQR = Q3 - Q1

# Upper bound
upper = (Q3+1.5*IQR)
 
# Lower bound
lower = (Q1-1.5*IQR)

new_df = df[(df['SepalWidthCm'] < upper) & (df['SepalWidthCm'] > lower)]
st.write("Old shape: ",df.shape)
st.write("New shape: ",new_df.shape)
st.write("Upper Bound: ", upper)
st.write("Lower Bound: ", lower)

st.markdown(''' ##### Box plot: 
    - After Outlier removal
''')

fig_2 = px.box(new_df, y="SepalWidthCm")
st.plotly_chart(fig_2, use_container_width=True)

st.write(''' In the above graph, the outliers are removed.
''')

############## Ending Note ##########

st.markdown( ''' ###                Thank you, for reading till here :clap:
''')