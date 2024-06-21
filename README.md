# googleMapLi
automatically recognizing a building's edge by its address Name.

# 方案一：基于Nominatim项目实现
Nominatim是一种按名称和地址（地理编码）搜索 OpenStreetMap 数据并生成OSM点以及反向地理编码的工具。它用作OpenStreetMap主页上搜索框的检索任务。本项目是基于Nominatim的docker项目来实现，输入地址名称，返回建筑边缘经纬度。

## 部署Nominatim的docker项目
本项目的该方案实现基于[Nominatim的docker项目](https://github.com/mediagis/nominatim-docker/tree/master/4.4)。在本项目下具体的部署过程可以见下文所示。

### 下载包含所需地址的数据
在[下载地址](https://download.geofabrik.de/)，对所需要地址的地图pbf数据进行下载。笔者保存于地址C:/Users/USTC/Desktop/Nominatim/data

### docker部署指令
```
docker run -e PBF_PATH=/nominatim/data/taiwan-latest.osm.pbf -p 8080:8080 -v C:/Users/USTC/Desktop/Nominatim/data:/nominatim/data --name nominatim mediagis/nominatim:4.4
```
其中，-e参数后接在镜像目录中地图数据所在的地址。-p参数为端口映射。-v参数表示目录的映射，-v参数的格式为"本机地图数据目录:镜像地图数据目录"。--name参数可自动下载nominatim:4.4项目镜像。

该指令只需更改本机地图数据目录即可。同时，创建服务器的时间相当长（可能数小时）这个的原因是：加载导入的地图数据，数据库构建和加载过程会比较耗时。

### 本地使用样例
搭建好了之后，在本机可以运行服务器，可在浏览器访问。更多使用方法的API请见[API](https://nominatim.org/release-docs/develop/api/Overview/)。

示例，例如想知道清华大学相关的建筑物轮廓信息：
```
http://localhost:8080/search.php?q=清华大学&polygon_geojson=1&format=jsonv2
```
即可得到json格式的返回，其中geojson返回的建筑物轮廓经纬度，coordinates为轮廓各点的经纬度坐标
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
                    
                    ...省略数个坐标...
                    
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

# 方案二：基于Segment Anything进行图像语意分割实现
[Segment Anything(SAM)](https://arxiv.org/abs/2304.02643
)是一种可提示的分割系统，对未见过的对象和图像进行零样本泛化，无需额外训练。根据点、框、输入提示等生成高质量的对象掩膜。本项目可以将经纬度坐标点作为输入，SAM模型输出建筑掩膜。

## 首先部署Segment Anything项目
本项目的该方案实现基于[Segment Anything项目](https://github.com/CASIA-IVA-Lab/FastSAM)，可以根据该仓库的Readme配置项目所需环境。本节简述配置过程。
```
// 克隆项目
git clone https://github.com/CASIA-IVA-Lab/FastSAM.git
// 创建conda环境
conda create -n FastSAM python=3.9
conda activate FastSAM
// 安装项目所需库
cd FastSAM
pip install -r requirements.txt
// 安装CLIP
pip install git+https://github.com/openai/CLIP.git
```

## 本项目的整体思路
大概思路可以分成3步，代码实现思路可以查看cvMethod.ipynb文件：
1. 输入是一个地址（自然语言），要能够自动获取该地址在地图中的图像经纬度；
2. 以第1步获取的经纬度作为输入，通过static image API获得以这个经纬度为中心的一张图像；
3. 以第2步获得的图像为输入，识别出包含中心经纬度的建筑物的轮廓，并输出拐角处的像素位置；
4. 根据像素位置计算出对应的经纬度；

### 本项目环境配置
```
// 安装项目所需库
pip install googlemaps
```

### 获取地址经纬度
根据输入的自然语言地址获取其在地图上的确切经纬度。通过使用Google Maps API中的Geocoding API来完成。Geocoding API能够将地址（如“清华大学”）转换为地理坐标（经度和纬度）。

### 获取该经纬度中心图像
接着使用Google Maps Static API可以根据经纬度获取地图上的静态图像。
本节的代码可参考cvMethod.ipynb文件

### 识别建筑图的轮廓并输出拐点的像素
本节使用SAM模型对上一步获取的静态地图图像进行建筑物的分割，具体内容参考[Segment Anything项目](https://github.com/CASIA-IVA-Lab/FastSAM)，可使用指令如下，：
```
python Inference.py --model_path ./weights/FastSAM.pt --img_path ./images/picture.png  --point_prompt "[[520,360],[620,300]]" --point_label "[1,0]"
```
--model_path表示SAM的预训练权重，可以在SAM项目中下载。--img_path表示图片所在路径。--point_prompt表示该点在地图中所处的位置。--point_label中1表示需要分割，0表示不需要分割。

![建筑物分割效果](figs/fig1.png)
如图，模型可输出将建筑物分割后的图片已实现，怎么让模型输出建筑物轮廓的像素点坐标还需要查看代码，亟须完成的工作。

### 像素点与经纬度之间的映射
本项目中一个需要关注的地方，获取的地图图像上的图片像素点坐标，应该和地球的经纬度实现一一映射对应。即：建筑物中心的经纬度要转换为图片中的像素点的坐标、分割后建筑物轮廓的图片中像素点坐标要转换为地理经纬度。

该地方详见CVmethod.ipynb代码，具体原理可以参考[本链接](https://stackoverflow.com/questions/47106276/converting-pixels-to-latlng-coordinates-from-google-static-image#comment81491489_47106276)。该链接代码实现了像素点到经纬度的映射，从而可以实现从图像中的轮廓坐标到地球的经纬度坐标转换，实现任务。