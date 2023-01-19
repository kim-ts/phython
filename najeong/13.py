# -*- coding = utf-8 -*-
# @Time : 2022-06-21오후 10:27
# @Author : 金泰式,3180300014
# @Site : 
# @File : 13.py
# @Software: PyCharm

import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']), cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]])) ])

fig.show()