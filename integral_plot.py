#!/usr/bin/python

# approximating definite integral.
# https://en.wikipedia.org/wiki/Trapezoidal_rule


import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation


area = []
a = 1
b = 3
num_of_iter = 100
x_axis_segment = (b - a) / float(num_of_iter)  # （3-1）/100 = 0.02
x_axis = a + np.true_divide(np.arange(0, num_of_iter), num_of_iter/2)

def f(x):
    return x**2

y_axis =[]
x_axis = x_axis.tolist()
for ith in list(range(0,len(x_axis))):
    y_axis.append(f(x_axis[ith]))


def draw_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x_axis,y_axis)
    curr_text = ax.text(0.2, 8, "area=" + str(0), style='italic', fontsize=30)
    axes = plt.gca()
    axes.set_xlim([0, 4])
    axes.set_ylim([0, 10])
    return fig, ax, axes, curr_text

def plot_ani(i):
    segment_area = x_axis_segment*y_axis[i]
    area.append(segment_area)
    curr_text.set_text("area=" + str(round(sum(area), 4)))
    axes.add_patch(Rectangle((x_axis[i], 0), x_axis_segment, y_axis[i], fill=True, alpha=1))

fig, ax, axes, curr_text = draw_plot()
ani = animation.FuncAnimation(fig, plot_ani, frames=num_of_iter, interval=20, repeat=False)
ani.save('/Users/boo/Desktop/intergral_example.gif', writer='imagemagick', dpi=80)




# python default package, much faster
# def integrate(f, a, b, N):
#     x = np.linspace(a, b, N)
#     fx = f(x)
#     area = np.sum(fx)*(b-a)/N
#     return area
#
# integrate(f, a, b, 100)