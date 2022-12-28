import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    sea_lvl = pd.read_csv("epa-sea-level.csv")
    x = sea_lvl['Year']
    y = sea_lvl['CSIRO Adjusted Sea Level']
    # Create scatter plot
    fig,ax = plt.subplots()
    plt.scatter(x,y)
    # Create first line of best fit

    res = linregress(x,y)
    x_pred = pd.Series([i for i in range(1880,2051)])
    y_pred = res.slope*x_pred + res.intercept
    plt.plot(x_pred,y_pred,color="red")

    # Create second line of best fit
    new_sea_lvl = sea_lvl.loc[sea_lvl['Year']>=2000]
    new_x = new_sea_lvl['Year']
    new_y = new_sea_lvl['CSIRO Adjusted Sea Level']
    new_res = linregress(new_x,new_y)
    x_pred_t = pd.Series([i for i in range(2000,2051)])
    y_pred_t = new_res.slope*x_pred_t + new_res.intercept
    plt.plot(x_pred_t,y_pred_t,color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()
