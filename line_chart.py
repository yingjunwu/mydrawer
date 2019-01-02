from common import *

# draw a line chart
def DrawFigure(x_values, y_values, legend_labels, x_label, y_label, x_min, x_max, y_min, y_max, filename, allow_legend, color_map = COLOR_MAP):

  assert(len(legend_labels) == len(y_values))

  # you may change the figure size on your own.
  fig = plt.figure(figsize=(8,3.2))
  figure = fig.add_subplot(111)

  if not os.path.exists(FIGURE_FOLDER):
    os.makedirs(FIGURE_FOLDER)

  lines = [None] * (len(legend_labels))
  for i in range(len(y_values)):
    lines[i], = figure.plot(x_values, y_values[i], color=color_map[i], \
                linewidth=LINE_WIDTH, marker=MARKERS[i], \
                markersize=MARKER_SIZE, label=legend_labels[i])

  # sometimes you may not want to draw legends.
  if allow_legend == True:
    plt.legend(lines, legend_labels, prop=LEGEND_FP, 
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

def DrawLegend(legend_labels, filename, color_map = COLOR_MAP):
  fig = pylab.figure()
  ax1 = fig.add_subplot(111)
  LINE_WIDTH = 8.0
  MARKER_SIZE = 12.0
  LEGEND_FP = FontProperties(style='normal', size=26)

  idx = 0
  lines = [None] * (len(legend_labels))
  data = [1]
  x_values = [1]

  for i in range(len(legend_labels)):
      lines[i], = ax1.plot(x_values, data,
                             color=color_map[i], linewidth=LINE_WIDTH,
                             marker=MARKERS[idx], markersize=MARKER_SIZE)

  # LEGEND
  figlegend = pylab.figure(figsize=(12, 0.5))
  figlegend.legend(lines, legend_labels, prop=LEGEND_FP, 
                   loc=1, ncol=len(legend_labels), mode="expand", shadow=False,
                   frameon=False, borderaxespad=0.0, handlelength=2)

  # no need to export eps in this case.
  figlegend.savefig(FIGURE_FOLDER + '/' + filename + '.pdf')

