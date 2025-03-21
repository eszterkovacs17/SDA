#!/usr/bin/ env python3

from bokeh.plotting import figure, output_file, save

# Create your plot
p = figure(title="Bokeh Plot Example", x_axis_label="X", y_axis_label="Y")
p.circle([1, 2, 3], [4, 5, 6], size=10)

# Save to an HTML file
output_file("bokeh_plot.html")
save(p)

