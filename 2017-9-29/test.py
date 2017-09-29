import json
from echarts import Echart, Legend, Bar, Axis
with open(u'温度数据.json','r') as fr:
    data = json.load(fr,encoding='utf-8')

city_list = []
min_list = []
sorted_list = sorted(data,lambda x,y:cmp(int(x['C_min']),int(y['C_min'])),reverse=True)
for item in sorted_list[:20]:
    city_list.append(item[u'城市'])
    min_list.append(item['C_min'])
    #print item[u'省份'], item[u'城市'],item['C_min']
chart = Echart(u'全国TOP20温度', u'全国温度最高的前20个市')
chart.use(Bar(u'temp',min_list))
chart.use(Axis('category', 'bottom','map',city_list))
chart.plot()