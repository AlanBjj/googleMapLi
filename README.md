# googleMapLi
automatically recognizing a building's edge by its address Name.

# 方案：基于Nominatim项目实现
Nominatim是一种按名称和地址（地理编码）搜索 OpenStreetMap 数据并生成OSM点以及反向地理编码的工具。它用作OpenStreetMap主页上搜索框的检索任务。本项目是基于Nominatim的docker项目来实现，输入地址名称，返回建筑边缘经纬度。

## 部署Nominatim的docker项目
[Nominatim的docker项目](https://github.com/mediagis/nominatim-docker/tree/master/4.4)。具体的部署过程可以见下文所示。

### 下载包含所需地址的数据
在[下载地址](https://download.geofabrik.de/)，对所需要地址的地图pbf数据进行下载。保存于地址C:/Users/USTC/Desktop/Nominatim/data

### docker部署指令
```
docker run -e PBF_PATH=/nominatim/data/taiwan-latest.osm.pbf -p 8080:8080 -v C:/Users/USTC/Desktop/Nominatim/data:/nominatim/data --name nominatim mediagis/nominatim:4.4
```
其中，-e参数后接在镜像目录中地图数据所在的地址。-p参数为端口映射。-v参数表示目录的映射，格式为本机地图数据目录:镜像地图数据目录。--name参数可自动下载nominatim:4.4项目镜像。

该指令只需更改本机地图数据目录即可。同时，创建服务器的时间相当长，原因是：加载导入的地图数据，加载过程会比较耗时。
### 本地使用样例
搭建好了之后，在本机可以运行服务器，可在浏览器访问。更多使用方法的API请见[API](https://nominatim.org/release-docs/develop/api/Overview/)。

示例：
```
http://localhost:8080/search.php?q=清华大学&polygon_geojson=1&format=jsonv2
```
即可得到json格式的返回，其中geojson返回的建筑物轮廓经纬度
```
[
    {
        "place_id": 1609804,
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "relation",
        "osm_id": 3605515,
        "boundingbox": [
            "24.7849692",
            "24.7983978",
            "120.9871303",
            "121.0025382"
        ],
        "lat": "24.7916987",
        "lon": "120.99242952395865",
        "display_name": "國立清華大學, 101, 交清小徑, 光明里, 東區, 新竹市, 30013, 台湾",
        "place_rank": 30,
        "category": "amenity",
        "type": "university",
        "importance": 0.00000999999999995449,
        "geojson": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        120.9871303,
                        24.7896431
                    ],
                    [
                        120.9877897,
                        24.7864404
                    ],
                    [
                        120.9881139,
                        24.7862477
                    ],
                    //
                    ...省略数个坐标
                    //
                    [
                        120.9871994,
                        24.7897975
                    ],
                    [
                        120.9871842,
                        24.7897636
                    ],
                    [
                        120.9871303,
                        24.7896431
                    ]
                ]
            ]
        }
    },
    {
        "place_id": 1608559,
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node",
        "osm_id": 10024571349,
        "boundingbox": [
            "24.7931474",
            "24.7932474",
            "120.9932779",
            "120.9933779"
        ],
        "lat": "24.7931974",
        "lon": "120.9933279",
        "display_name": "清華大學(小吃部), 101, 齋群一路, 光明里, 東區, 新竹市, 30013, 台湾",
        "place_rank": 30,
        "category": "amenity",
        "type": "bicycle_rental",
        "importance": 0.00000999999999995449,
        "geojson": {
            "type": "Point",
            "coordinates": [
                120.9933279,
                24.7931974
            ]
        }
    },
    {
        "place_id": 1612932,
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node",
        "osm_id": 10129850757,
        "boundingbox": [
            "24.796791",
            "24.796891",
            "120.99664",
            "120.99674"
        ],
        "lat": "24.796841",
        "lon": "120.99669",
        "display_name": "清華大學(北校門), 光復路二段, 光明里, 東區, 新竹市, 30070, 台湾",
        "place_rank": 30,
        "category": "amenity",
        "type": "bicycle_rental",
        "importance": 0.00000999999999995449,
        "geojson": {
            "type": "Point",
            "coordinates": [
                120.99669,
                24.796841
            ]
        }
    },
    {
        "place_id": 1638457,
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node",
        "osm_id": 10024571379,
        "boundingbox": [
            "24.7953024",
            "24.7954024",
            "120.9923187",
            "120.9924187"
        ],
        "lat": "24.7953524",
        "lon": "120.9923687",
        "display_name": "清華大學(台達館), 101, 行勝路, 光明里, 東區, 新竹市, 30013, 台湾",
        "place_rank": 30,
        "category": "amenity",
        "type": "bicycle_rental",
        "importance": 0.00000999999999995449,
        "geojson": {
            "type": "Point",
            "coordinates": [
                120.9923687,
                24.7953524
            ]
        }
    },
    {
        "place_id": 1637056,
        "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
        "osm_type": "node",
        "osm_id": 4524886749,
        "boundingbox": [
            "24.7970216",
            "24.7971216",
            "120.9966591",
            "120.9967591"
        ],
        "lat": "24.7970716",
        "lon": "120.9967091",
        "display_name": "清華大學, 光復路二段, 軍功里, 東區, 新竹市, 30070, 台湾",
        "place_rank": 30,
        "category": "highway",
        "type": "bus_stop",
        "importance": 0.00000999999999995449,
        "geojson": {
            "type": "Point",
            "coordinates": [
                120.9967091,
                24.7970716
            ]
        }
    }
]
```