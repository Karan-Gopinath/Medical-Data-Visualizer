import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 

# readin the data

df = pd.read_csv('medical_examinations.csv')


# BMI as well as overweight colum

df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25 ).astype(int)



#normalise the cholestrol and glucose

df['cholesterol'] = (df['cholesterol'] > 1 ).astype(int)
df['gluc'] = (df[ ' gluc'] > 1).astype(int)


# plot

def draw_cat_plot():
     df_cat = pd.melt(
        df, 
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
     )

  # group them and count
  df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = 'total')


  #plot using the seaborn

  fig = sns.catplot(

    x = "variable",
    y = "total",
    hue = "value",
    col = "cardio",
    data=df_cat,
    kind= "bar"
  ).fig
  return fig

  # heatmap
  ef draw_heat_map():
    
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]


    # correlection matrix
    corr = df_heat.corr()

    #Mask for  upper triangle

    mask = np.triu(np.ones_like(corr , dtype=bool))


    #plot
    fig, ax = plt.subplots(figsize= (12, 10))
    sns.heatmap(
        corr,
        mask =mask,
        annot=True,
        fmt = ".1f"
        center= 0
        square = True
        cbar_kws={'shrink' : 0.5}
    )

    return fig


