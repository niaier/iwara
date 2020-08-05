const express = require("express");
const app = express();
const router =require("./controller/router.js");

//模版引擎
app.set("view engine","ejs");

// 静态页面
app.use(express.static("./public"));
app.use("/video/:dirname",express.static("./public"));
app.use(express.static("D:\\iwara_dwon")); //视频存放位置

//首页
app.get("/",router.loadPage);
app.get("/api",router.loadPageData);
//其他页
console.log(1);
app.get("/:page",router.loadPage);
app.get("/:page/api",router.loadPageData);
//播放页
console.log(2);
app.get("/video/:dirname",router.loadVideo);
app.get("/video/:dirname/api",router.loadVideoData);
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

app.use(function (req,res) {
    res.render("404")
});
// app.use()
app.listen("3000");
// app.set('host','192.168.50.74');

