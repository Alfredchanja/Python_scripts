"""
Alfred Gachanja
31-10-2024
This program creates contour maps for elemental concentration at a particular area.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Geochemical data for assignment one.csv')

# Picking dataset from the 3rd column.
column_to_plot = df[3:]

# Looping Through the data to separate the dataset for plotting the contour maps.
for col in column_to_plot:
    if col == 'Ti':
        Ti_dataset = df[['X', 'Y', col]]
    elif col == 'V':
        V_dataset = df[['X', 'Y', col]]
    elif col == 'Mn':
        Mn_dataset = df[['X', 'Y', col]]
    elif col == 'Fe':
        Fe_dataset = df[['X', 'Y', col]]
    elif col == 'Cr':
        Cr_dataset = df[['X', 'Y', col]]
    elif col == 'Co':
        Co_dataset = df[['X', 'Y', col]]

# List of the required dataset for plotting the contour maps.
list_of_required_dataset = [Ti_dataset, V_dataset, Mn_dataset, Fe_dataset, Cr_dataset, Co_dataset]

# This function plots the required contour maps.
def contour_plt():

    # Looping through the data set to plot the contour maps.
    for dataset in list_of_required_dataset:
        # Preparing to plot the contour map.
        fig, ax = plt.subplots(figsize=(10, 8))

        # Plotting the contour maps
        sns.kdeplot(x=dataset['X'], y=dataset['Y'],
                    weights=dataset.iloc[:, 2], # Selects the data required to plot the contour map from all the rows the 3rd column.
                    fill=True, cmap = 'plasma', levels=20, thresh=0.05, cbar=True
                )

        # Labeling the contour maps.
        ax.set_title(f'Contour Map of {dataset.columns[2]}')
        ax.set_xlabel('Latitudes')
        ax.set_ylabel('Longitude')

        # Saving the contour maps.
        fig.savefig(f'{dataset.columns[2]} Contour Map.png')
    
    return fig

contour_plt()