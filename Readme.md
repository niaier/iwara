# iwara本地化

### 项目说明

iwara_spider：

​	爬虫，用于抓取iwara资源，包括数据库信息统计和视频资源下载

iwara_localplay:

​	本地化仿站，搭建nodejs服务器实现本地播放，收藏等功能



如果要实现本地化，你需要以下几个必须步骤

```
1.下载前端和后台程序并运行
2.MySQL数据获取
3.视频资源的获取
```





文件结构说明

```
|-- Readme.md
|-- iwara_check 
|   |-- iwara_check.py //检查下载文件状态并更新数据库
|   |-- iwara_ffmpeg.py //生成视频缩略图
|   `-- 检查空文件.py
|-- iwara_spider //写爬虫时测试程序
|   |-- run_iwara.py
|   `-- test.py
|-- 后台 //nodejs运行 可以使用nodemon
|   |-- controller
|   |-- index.js
|   |-- modules
|   |-- package.json
|   |-- public
|   |-- views
|   `-- yarn.lock
|-- 爬虫 //win10环境下各种爬虫
|   `-- iwara_all_win
|-- 其他 //视频打包压缩分包等操作
|   |-- 1.py
|   |-- 视频压缩.py
|   `-- 下载视频的文件名到数据库.py
`-- 前端
    |-- README.md
    |-- babel.config.js
    |-- package.json
    |-- public
    |-- src
    |-- vue.config.js
    `-- yarn.lock


```



#### 项目当前状况 2020/09/26

```
项目数据从一开始到2020/08
数据采集：
通过MySQL数据库保存
下载资源：
下载的视频5719个，是筛选出400个喜爱以上的视频
后台接口：
express nodejs实现，基本功能完成
前端页面：
vue实现，有喜爱分级，播放列表功能，根据日期等排序

未来目标：
新数据爬取
资源下载，打包上传至网盘
前端页面优化，显示效果，数据筛选等
后台接口优化

```

#### 视频教程

[下载地址]: pan.baidu.com/s/1FuzzdO1xN5-QtUgkGVWB-w

```
链接：1FuzzdO1xN5-QtUgkGVWB-w 
提取码：9dj3 
解压密码：niaier
```



#### 使用方法

```
前端
yarn
yran serve

后端
node ./index.js
注意修改一下静态资源的文件夹

mysql
建议使用sqlyog
数据库命名为iwara就行
```



#### 配置说明

后台配置

```
静态资源地址设置
index.js文件下
app.use(express.static("D:\\iwara_dwon"));
//把"D:\\iwara_dwon"改为你存储视频的文件位置，注意文件结构
端口号
app.listen("3000");
```

前端配置

```
由于前后端分离跨域问题，需要配置代理
vue.config.js文件
host:"0.0.0.0",
    proxy: {
      "/api": {
        target: "http://127.0.0.1:3000/", //目标主机，即后台的域名和端口
        ws: true, //代理的WebSockets
        changeOrigin: true, //需要虚拟主机站点
        pathRewrite: {
          "^/api": ""
        }
      }
    },
axios配置
设置根路径
入口文件main.js
axios.defaults.baseURL='http://192.168.50.221:8080/api'
192.168.50.221是本机的ip地址，win+r 输入cmd调出命令行窗口，输入ipconfig -all即可查询

```

mysql导入数据



### 资源下载

```
b网盘
mysql数据 
链接： 1OCEHoyptVOI8UYLdalURbQ 提取码：hk8j


视频资源 
/s/1pXVmWQVQmmLgJT1jnYsHYw 
提取码：95yn 
解压密码 niaier
```



### 其他：如果有什么意见和建议可以留言交流

niaier@outlook.com