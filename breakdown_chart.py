import matplotlib.pyplot as plt
import numpy as np
import pickle
import os
import pylab
import matplotlib
import csv
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import LinearLocator


OPT_FONT_NAME = 'Helvetica'
TICK_FONT_SIZE = 20
LABEL_FONT_SIZE = 22
LEGEND_FONT_SIZE = 24
LABEL_FP = FontProperties(style='normal', size=LABEL_FONT_SIZE)
LEGEND_FP = FontProperties(style='normal', size=LEGEND_FONT_SIZE)
TICK_FP = FontProperties(style='normal', size=TICK_FONT_SIZE)

MARKERS = (['o', 's', 'v', "^", "h", "v", ">", "x", "d", "<", "|", "", "|", "_"])
# you may want to change the color map for different figures
COLOR_MAP = ('#F15854', '#5DA5DA', '#60BD68',  '#B276B2', '#DECF3F', '#F17CB0', '#B2912F', '#FAA43A', '#AFAFAF')
# you may want to change the patterns for different figures
PATTERNS = ([ "////", "\\\\", "//////", "o", "o", "\\\\" , "\\\\" , "//////", "//////", "." , "\\\\\\" , "\\\\\\" ])
LABEL_WEIGHT = 'bold'
LINE_COLORS = COLOR_MAP
LINE_WIDTH = 3.0
MARKER_SIZE = 0.0
MARKER_FREQUENCY = 1000

matplotlib.rcParams['ps.useafm'] = True
matplotlib.rcParams['pdf.use14corefonts'] = True
matplotlib.rcParams['xtick.labelsize'] = TICK_FONT_SIZE
matplotlib.rcParams['ytick.labelsize'] = TICK_FONT_SIZE
matplotlib.rcParams['font.family'] = OPT_FONT_NAME

FIGURE_FOLDER='figures/'

# there are some embedding problems if directly exporting the pdf figure using matplotlib.
# so we generate the eps format first and convert it to pdf.
def ConvertEpsToPdf(dir_filename):
  os.system("epstopdf --outfile " + dir_filename + ".pdf " + dir_filename + ".eps")
  os.system("rm -rf " + dir_filename + ".eps")

# draw a line chart
def DrawFigure(x_values, y_values, legend_labels, x_label, y_label, filename, allow_legend):

  # you may change the figure size on your own.
  fig = plt.figure(figsize=(8,3.2))
  figure = fig.add_subplot(111)

  FIGURE_LABEL = legend_labels

  if not os.path.exists(FIGURE_FOLDER):
    os.makedirs(FIGURE_FOLDER)

  # values in the x_xis
  index = np.arange(len(x_values))
  # the bar width. 
  # you may need to tune it to get the best figure.
  width = 0.36
  # draw the bars
  bottom_base = np.zeros(len(y_values[0]))
  bars = [None] * (len(FIGURE_LABEL))
  for i in range(len(y_values)):
    bars[i] = plt.bar(index + width / 2, y_values[i], width, hatch=PATTERNS[i], color=LINE_COLORS[i], label=FIGURE_LABEL[i], bottom=bottom_base)
    bottom_base = np.array(y_values[i]) + bottom_base

  # sometimes you may not want to draw legends.
  if allow_legend == True:
    plt.legend(bars, FIGURE_LABEL, prop=LEGEND_FP, 
                     loc='upper center', ncol=len(legend_labels), mode='expand', bbox_to_anchor=(0.45, 1.2), shadow=False,
                     frameon=False, borderaxespad=0.0, handlelength=2, labelspacing=0.2)

  # you may need to tune the xticks position to get the best figure.
  plt.xticks(index + 1.5 * width, x_values)

  # plt.xlim(0,)
  plt.ylim(0,1)

  plt.grid(axis='y',color='gray')
  figure.yaxis.set_major_locator(LinearLocator(6))
  
  figure.get_xaxis().set_tick_params(direction='in', pad=10)
  figure.get_yaxis().set_tick_params(direction='in', pad=10)
  
  plt.xlabel(x_label, fontproperties=LABEL_FP)
  plt.ylabel(y_label, fontproperties=LABEL_FP)

  size = fig.get_size_inches()
  dpi = fig.get_dpi()
  
  plt.savefig(FIGURE_FOLDER + "/" + filename + ".eps", bbox_inches='tight', format='eps')
  ConvertEpsToPdf(FIGURE_FOLDER + "/" + filename)


def DrawLegend(legend_labels, filename):
  fig = pylab.figure()
  ax1 = fig.add_subplot(111)
  FIGURE_LABEL = legend_labels
  LEGEND_FP = FontProperties(style='normal', size=26)

  bars = [None] * (len(FIGURE_LABEL))
  data = [1]
  x_values = [1]

  width = 0.3
  for i in range(len(FIGURE_LABEL)):
    bars[i] = ax1.bar(x_values, data, width, hatch=PATTERNS[i], color=LINE_COLORS[i], 
                      linewidth=0.2)

  # LEGEND
  figlegend = pylab.figure(figsize=(12, 0.5))
  figlegend.legend(bars, FIGURE_LABEL, prop=LEGEND_FP, \
                   loc=1, ncol=len(FIGURE_LABEL), mode="expand", shadow=False, \
                   frameon=False, borderaxespad=0.0, handlelength=2)

  figlegend.savefig(FIGURE_FOLDER + '/' + filename + '.pdf')


def normalize(y_values):
  y_total_values = np.zeros(len(y_values[0]))

  for i in range(len(y_values)):
    y_total_values += np.array(y_values[i])
  y_norm_values = []

  for i in range(len(y_values)):
    y_norm_values.append(np.array(y_values[i]) / (y_total_values * 1.0))
  return y_norm_values


if __name__ == "__main__":

  x_values = ['1.0%','2.5%','5.0%','7.5%','10%']

  y_values = []

  y_values.append([1,3,5,7,9])

  y_values.append([11,13,15,17,19])

  y_values.append([2,4,6,8,10])

  y_values.append([12,14,16,18,20])

  y_norm_values = normalize(y_values)
  
  # break into 4 parts
  legend_labels = ['part0','part1','part2','part3']

  DrawFigure(x_values, y_norm_values, legend_labels, 'percentage', 'breakdown', 'breakdown_chart', False)

  DrawLegend(legend_labels, 'breakdown_chart_legend')
