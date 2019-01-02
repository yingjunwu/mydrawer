from common import *

# draw a line chart
def DrawFigure(x_values, y_values, legend_labels, x_label, y_label, y_min, y_max, filename, allow_legend, color_map = COLOR_MAP, patterns = PATTERNS):

  assert(len(legend_labels) == len(y_values))
  
  # you may change the figure size on your own.
  fig = plt.figure(figsize=(8,3.2))
  figure = fig.add_subplot(111)

  if not os.path.exists(FIGURE_FOLDER):
    os.makedirs(FIGURE_FOLDER)

  # values in the x_xis
  index = np.arange(len(x_values))
  # the bar width. 
  # you may need to tune it to get the best figure.
  width = 0.3
  # draw the bars
  bars = [None] * (len(legend_labels))
  for i in range(len(y_values)):
    bars[i] = plt.bar(index + i * width + width / 2, y_values[i], width, hatch=patterns[i], color=color_map[i], label=legend_labels[i])

  # sometimes you may not want to draw legends.
  if allow_legend == True:
    plt.legend(bars, legend_labels, prop=LEGEND_FP, 
                     loc='upper center', ncol=2, mode='expand', bbox_to_anchor=(0.45, 1.2), shadow=False,
                     frameon=False, borderaxespad=0.0, handlelength=2, labelspacing=0.2)

  # you may need to tune the xticks position to get the best figure.
  plt.xticks(index + 1.5 * width, x_values)

  # plt.xlim(0,)
  plt.ylim(y_min,y_max)

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


def DrawLegend(legend_labels, filename, color_map = COLOR_MAP, patterns = PATTERNS):
  fig = pylab.figure()
  ax1 = fig.add_subplot(111)
  LEGEND_FP = FontProperties(style='normal', size=26)

  bars = [None] * (len(legend_labels))
  data = [1]
  x_values = [1]

  width = 0.3
  for i in range(len(legend_labels)):
    bars[i] = ax1.bar(x_values, data, width, hatch=patterns[i], color=color_map[i], 
                      linewidth=0.2)

  # LEGEND
  figlegend = pylab.figure(figsize=(12, 0.5))
  figlegend.legend(bars, legend_labels, prop=LEGEND_FP, \
                   loc=1, ncol=len(legend_labels), mode="expand", shadow=False, \
                   frameon=False, borderaxespad=0.0, handlelength=2)

  figlegend.savefig(FIGURE_FOLDER + '/' + filename + '.pdf')


