# main.py

from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Generate and show categorical plot
cat_fig = draw_cat_plot()
cat_fig.savefig('catplot.png')  # Save the figure to a file (optional)
plt.show()  # Display the figure in your environment

# Generate and show heat map
heat_fig = draw_heat_map()
heat_fig.savefig('heatmap.png')  # Save the figure to a file (optional)
plt.show()  # Display the figure
