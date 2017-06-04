"""

Example
line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render_to_file('/tmp/line.svg')

"""
import pygal

config = pygal.Config(include_x_axis=True, legend_at_bottom=True, legend_at_bottom_columns=4, x_title='X Axis', y_title='Y Axis')
config.style = pygal.style.LightStyle
config.defs.append('''
  <linearGradient id="gradient-0" x1="0" x2="0" y1="0" y2="1">
    <stop offset="0%" stop-color="#ff5995" />
    <stop offset="100%" stop-color="#feed6c" />
  </linearGradient>
''')
config.defs.append('''
  <linearGradient id="gradient-1" x1="0" x2="0" y1="0" y2="1">
    <stop offset="0%" stop-color="#b6e354" />
    <stop offset="100%" stop-color="#8cedff" />
  </linearGradient>
''')
config.css.append('''inline:
  .color-0 {
    fill: url(#gradient-0) !important;
    stroke: url(#gradient-0) !important;
  }''')
config.css.append('''inline:
  .color-1 {
    fill: url(#gradient-1) !important;
    stroke: url(#gradient-1) !important;
  }''')

line_chart = pygal.Line(config)
line_chart.title = "SNMPv3 - MIB :  OID"
line_chart.x_labels = map(str, range(0, 10))
line_chart.add('Description', [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
line_chart.add('Description', [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
line_chart.add('Description', [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
line_chart.add('Description', [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
line_chart.render_to_file('/tmp/pygal_line.svg')
