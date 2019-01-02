import bar_chart
import breakdown_chart
import line_chart
import csv

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

if __name__ == "__main__":


  figure_folder='figures/'

  # draw bar chart
  x_values = ['1.0%','2.5%','5.0%','7.5%','10%']

  y_values = []
  y_values.append([10,5,2.5,1,0.5])
  y_values.append([20,10,5,2,1])

  legend_labels = ['test0','test1']

  bar_chart.DrawFigure(x_values, y_values, legend_labels, 'percentage', 'Performance', 0, 30, figure_folder, 'bar_chart', True)

  bar_chart.DrawLegend(legend_labels, figure_folder, 'bar_chart_legend')


  # draw breakdown chart
  x_values = ['1.0%','2.5%','5.0%','7.5%','10%']

  y_values = []

  y_values.append([1,3,5,7,9])

  y_values.append([11,13,15,17,19])

  y_values.append([2,4,6,8,10])

  y_values.append([12,14,16,18,20])

  y_norm_values = breakdown_chart.normalize(y_values)
  
  # break into 4 parts
  legend_labels = ['part0','part1','part2','part3']

  breakdown_chart.DrawFigure(x_values, y_norm_values, legend_labels, 'percentage', 'breakdown', figure_folder, 'breakdown_chart', False)

  breakdown_chart.DrawLegend(legend_labels, figure_folder, 'breakdown_chart_legend')


  # draw line chart
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

  line_chart.DrawFigure(years, lines, legend_labels, 'Year', 'Index', 1991, 2011, 0, 15000, figure_folder, 'line_chart', False)
  line_chart.DrawLegend(legend_labels, figure_folder, 'line_chart_legend')


