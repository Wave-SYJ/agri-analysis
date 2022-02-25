# 农产品市场数据分析系统

本项目为东南大学软件学院2021年暑期实训第五组项目。

## 目录结构

- `agri-analysis-client` 前端项目，由 Vue 开发。
- `agri-analysis-server` 后端项目，由 Python + Flask 开发。
- `agri-analysis-spider` 爬虫项目，由 Python + Scrapy 开发。

## 运行依赖

以下各依赖版本为推荐配置。

- node 14.17.3 LTS 

- npm 7.20.0

- python  3.9.6

- MySQL 8.0.25 （必须为 MySQL 8）

- JDK  8u301 （必须为 JDK 8）

- hadoop 2.7.7 （必须为 hadoop 2.7.x）

- spark-3.0.3-bin-hadoop2.7 （必须）

- nginx 1.20.1 （生产环境需要）

## 运行方法

第一次运行需要以下步骤进行初始化：

1. 运行后端项目。运行后将自动进行数据库建表，并添加一个超级管理员用户，用户名与密码均为“admin”。
2. 运行爬虫项目。首先爬取区域数据（省、市和市场数据）以及农产品种类数据（种类和品种），然后正是爬取农产品价格和售卖行情数据。
3. 运行前端项目。

之后运行只需要将运行前后端项目，并按需要爬取某一时间段农产品价格和售卖行情数据即可。

在 Linux 操作系统下，详细初始化流程如下（Windows 操作系统类似）：

### 1. 运行后端项目

先确保 MySQL Server 服务处于运行状态，并创建名为 `agri_analysis` 的空数据库。

在 `agri-analysis-server/app/config/` 目录下

- 在同一文件夹复制 `database.example.yml` 文件命名为 `database.secret.yml`，修改`development.database.password`配置项为 MySQL 数据库密码
- 在同一文件夹复制 `auth.example.yml` 文件命名为 `auth.example.yml`，修改`development.auth.secret` 配置项为一复杂密码，该配置项用于密码加密

在 `agri-analysis-server` 目录下：

- 建立 python 虚拟环境：
  
  ```shell
  python -m venv venv
  ```

- 启用虚拟环境：
  
  ```shell
  source venv/bin/activate
  ```

- 安装依赖：
  
  ```shell
  pip install -r requirements.txt
  ```

- 运行：
  
  ```shell
  ./run.sh
  ```

后端项目将监听 5050 端口。

### 2. 运行爬虫项目

确保 MySQL 中 `agri_analysis` 数据库已生成了七张表 `t_admin`、`t_city`、`t_market`、`t_product`、`t_province`、`t_type `和 `t_variety` 。

在`agri-analysis-spider/app/config`目录下，复制`database.example.yml` 文件命名为 `database.secret.yml`，修改`development.database.password`配置项为 MySQL 数据库密码。

在 `agri-analysis-spider` 目录下：

- 建立 python 虚拟环境：
  
  ```shell
  python -m venv venv
  ```

- 启用虚拟环境：
  
  ```shell
  source venv/bin/activate
  ```

- 安装依赖：
  
  ```shell
  pip install -r requirements.txt
  ```

- 爬取区域数据和农产品种类数据：
  
  ```shell
  scrapy crawl city & scrapy crawl market & scrapy crawl variety
  ```

- 爬取段农产品价格和售卖行情数据：
  
  ```shell
  scrapy crawl all_product -a start=2021-01-01 -a end=2021-07-28
  ```
  
  其中 `start` 参数为爬取起始日期，为空则默认为`2014-01-01`；`end` 参数为爬虫终止日期，为空则默认为程序运行日期。

### 3. 运行前端项目

在 `agri_analysis-client` 目录下：

- 安装依赖：
  
  ```shell
  npm install
  ```

- 运行：
  
  ```shell
  npm run serve
  ```

项目将在运行在：http://localhost:8080/

### 部署方法

这里采用 nginx 进行部署。

- 静默启动后端：
  
  在后端目录启动虚拟环境，然后执行：
  
  ```shell
  nohup ./run.sh &
  ```

- 前端打包：
  
  在前端目录：
  
  ```shell
  npm run build
  ```
  
  打包文件在 `dist` 文件夹下。

- 配置 nginx ，参考如下配置：
  
  ```nginx
  server {
      listen          8080;
      server_name     localhost;
  
      location / {
          root        /path/to/agri-analysis-client/dist;
          try_files   $uri $uri/ /index.html;
          index       index.html index.html;
      }
  
      location /api/ {
          proxy_pass  http://localhost:5000/;
      }
  }
  ```
  
  启动/重新启动 nginx 加载该配置。
  
  项目运行在 8080 端口。
