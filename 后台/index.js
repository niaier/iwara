const express = require("express");
const app = express();
const router = require("./controller/router.js");

app.use(express.static("./public"));
app.use("/video/:dirname", express.static("./public"));
app.use(express.static("D:\\iwara_dwon")); //视频存放位置

// video页面数据
app.get("/videoListData",router.loadPageData);
app.get("/videoList",router.loadPageData);
app.get("/video/:dirname/api",router.loadVideoData);
app.get("/video/:dirname/loadVideoInfo",router.loadVideoInfo);
app.get("/video/:dirname/loadLoveList",router.loadLoveList);
app.get("/video/:dirname/loadMyPlayList",router.loadMyPlayList);
app.get("/video/:dirname/loadPlayList",router.loadPlayList);

// love页面
app.get("/love",router.loadLovePage);
//playlist页面
app.get("/playlist",router.loadPlayListData);
app.get("/myPlaylist",router.loadMyPlayListData);

//喜爱
console.log(3);
app.get("/video/:dirname/loved",router.addLoved);
console.log(4);
app.get("/video/:dirname/addlist",router.addList);
console.log(5);

app.get("/video/:dirname/addMylist",router.addMyList);
console.log(6);
app.get("/video/:dirname/deletlist",router.deleteList);
console.log(6);
// app.get("/loved",router.addLoved);
app.listen("3000");
// app.set('host','192.168.50.74');