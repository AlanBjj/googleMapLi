import requests
import json

# 设置经纬度和搜索半径（米）
latitude = 25.034690561731164
longitude = 121.52188139057928
radius = 50

# Overpass API 查询
query = f"""
[out:json];
(
  way(around:{radius},{latitude},{longitude})["building"];
);
out body;
>;
out skel qt;
"""

response = requests.get("http://overpass-api.de/api/interpreter", params={'data': query})
data = response.json()

# 解析响应以获取建筑物轮廓的经纬度
for element in data['elements']:
    if 'nodes' in element:
        print(f"Building ID: {element['id']}")
        for node_id in element['nodes']:
            node = next(item for item in data['elements'] if item['type'] == 'node' and item['id'] == node_id)
            print(f"Lat: {node['lat']}, Lon: {node['lon']}")
