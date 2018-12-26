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

# example for reading csv file
def ReadFile():
  dates = []
  djis = []
  sps = []
  with open('DJI-SP.csv') as csvfile:
    rows = csv.reader(csvfile, delimiter = ',')
    
    count = 0
    for row in rows:
      dates.append(row[0])
      djis.append(float(row[1])) 
      sps.append(float(row[2]))

  return dates, djis, sps

# draw a line chart
def DrawFigure(xvalues, yvalues, legend_labels, x_label, y_label, x_min, x_max, y_min, y_max, filename, allow_legend):

  # you may change the figure size on your own.
  fig = plt.figure(figsize=(8,3.2))
  figure = fig.add_subplot(111)

  FIGURE_LABEL = legend_labels

  if not os.path.exists(FIGURE_FOLDER):
    os.makedirs(FIGURE_FOLDER)

  x_values = xvalues

  y_values = yvalues

  lines = [None] * (len(FIGURE_LABEL))
  for i in range(len(y_values)):
    lines[i], = figure.plot(x_values, y_values[i], color=LINE_COLORS[i], \
                linewidth=LINE_WIDTH, marker=MARKERS[i], \
                markersize=MARKER_SIZE, label=FIGURE_LABEL[i])

  # sometimes you may not want to draw legends.
  if allow_legend == True:
    plt.legend(lines, FIGURE_LABEL, prop=LEGEND_FP, 
                     loc='upper center', ncol=2, mode='expand', bbox_to_anchor=(0.45, 1.2), shadow=False,
                     frameon=False, borderaxespad=0.0, handlelength=2, labelspacing=0.2)

  plt.xticks(x_values)
  # you may control the limits on your own.
  plt.xlim(x_min, x_max)
  plt.ylim(y_min, y_max)

  plt.grid(axis='y',color='gray')
  figure.yaxis.set_major_locator(LinearLocator(6))
  figure.xaxis.set_major_locator(LinearLocator(6))
  
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
  LINE_WIDTH = 8.0
  MARKER_SIZE = 12.0
  LEGEND_FP = FontProperties(style='normal', size=26)

  figlegend = pylab.figure(figsize=(12, 0.5))
  idx = 0
  lines = [None] * (len(FIGURE_LABEL))
  data = [1]
  x_values = [1]

  idx = 0
  for group in xrange(len(FIGURE_LABEL)):
      lines[idx], = ax1.plot(x_values, data,
                             color=LINE_COLORS[idx], linewidth=LINE_WIDTH,
                             marker=MARKERS[idx], markersize=MARKER_SIZE, label=str(group))

      idx = idx + 1

  # LEGEND
  figlegend.legend(lines, FIGURE_LABEL, prop=LEGEND_FP, 
                   loc=1, ncol=len(FIGURE_LABEL), mode="expand", shadow=False,
                   frameon=False, borderaxespad=0.0, handlelength=2)

  if not os.path.exists(FIGURE_FOLDER):
    os.makedirs(FIGURE_FOLDER)
  # no need to export eps in this case.
  figlegend.savefig(FIGURE_FOLDER + '/' + filename + '.pdf')


if __name__ == "__main__":

  legend_labels = ['Dow-Jones', 'S&P 500']
  dates, djs, sps = ReadFile()

  # we want to use year as x-axis.
  # we calculate the year own our own.
  years = []
  init = 1991
  for i in range(len(dates)):
    years.append(init + i * 1.0 / 12)
  
  # we want to have two lines: Dow-Jones and S&P 500
  lines = [djs, sps]

  DrawFigure(years, lines, legend_labels, 'Year', 'Index', 1991, 2011, 0, 15000, 'line_chart', False)
  DrawLegend(legend_labels, 'line_chart_legend')
