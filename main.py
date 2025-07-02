# main.py

from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Generate and show the categorical plot
cat_fig = draw_cat_plot()
cat_fig.savefig('catplot.png')  # Optional: save to file
plt.show()  # Display the figure

# Generate and show the heatmap
heat_fig = draw_heat_map()
heat_fig.savefig('heatmap.png')  # Optional: save to file
plt.show()  # Display the figure
