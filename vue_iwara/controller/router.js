const mysqlTools = require("../moduls/mysqlTools");
const dataProcess = require("../moduls/dataProcessing");
const pageTools = require("../moduls/pageTools");
const page_List =pageTools.page_List;
const path = require('path');


// 主页面
exports.loadIndex = function (req, res){
    console.log(req.params.page,"==============");
    let cur_page = 0;
    let sql = 'SELECT * FROM iwara_info WHERE isDown=1 order by dirname desc';
    mysqlTools.setMysqlData(sql).then(
        value=>{
            //当前页的目录
            let slicedData = dataProcess.dataSlice(value);
            let cur_page_index = slicedData[cur_page];
            let pageLength = cur_page_index.length;
            //切片分组的数
            // console.log(dataProcess.dataSlice(value).length);
            console.log(cur_page_index.length,"当前页项目数量");
            console.log(req.params);
            // console.log(curPageOrder);
            //页码总数
            let final_page = slicedData.length;
            let final_url = "/"+(final_page-1);
            // console.log(final_url);0
            let pageList = [1,2,3,4,5,6,7,'...',final_page];
            let pageUrl = [1,2,3,4,5,6,7,8,final_page];
            let pageObj = {
                'pagelist':pageList,
                'pageurl':pageUrl
            };
            res.render("index",{
                "pageList":pageObj,
                "curPage" : cur_page,
                "pageLength":pageLength,
                "videoIndex" : cur_page_index,
                "final_page" : final_page,
                "final_url":final_url,
            });
        }
    ).catch(reason => {
        console.log(reason)
    });

    // (result=>{});

};

exports.loadPage = function(req, res){
    console.log(req.params.page,"==============");
    let curPage = req.params.page;
    if (curPage===undefined) {
        curPage = 0;
    }
    else {
        curPage = Number(req.params.page);
    }
    console.log("当前页面转化数字",curPage);
    if (!curPage && curPage!==0) {
        // res.send("输入正确页码");
        console.log("错误参数",req.params);
        res.render("404")
    }
    res.sendFile(path.join(__dirname,'../views/index.html'));


    // mysqlTools.setMysqlData(function (result) {
    //
    //     console.log(curPageOrder);
    //     console.log("sapspapspaps");
    //     var final_page = curPageOrder.length;
    //     var fianl_url = "/"+final_page;
    //     console.log("final",final_page,typeof final_page,fianl_url);
    //
    //     res.render("index",{
    //         "videoIndex" : curPageOrder,
    //         "final_page" : final_page
    //
    //     });
    //     // res.send(curPageOrder);
    // });


};

exports.loadPageData = function(req, res){
    console.log(req.params.page,"==============");
    let curPage = req.params.page;
    if (curPage===undefined) {
        curPage = 0;
    }
    else {
        curPage = Number(req.params.page);
    }
    console.log("当前页面转化数字",curPage);
    if (!curPage && curPage!==0) {
        // res.send("输入正确页码");
        console.log("错误参数",req.params);
        res.render("404")
    }


    // const p1 = mysqlTools.setMysqlData();
    let sql = 'SELECT * FROM iwara_info WHERE isDown=1 order by dirname desc';
    mysqlTools.setMysqlData(sql).then(
        value=>{
            //当前页的目录
            let slicedData = dataProcess.dataSlice(value);
            let curPageIndex = slicedData[curPage];
            let pageLength = curPageIndex.length;
            //切片分组的数
            // console.log(dataProcess.dataSlice(value).length);
            console.log("当前页项目数量",curPageIndex.length);
            console.log("当前页参数",req.params);
            // console.log(curPageOrder);
            let finalPage = slicedData.length;
            let finalUrl = "/"+(finalPage-1);
            let pageList = page_List(curPage,finalPage);
            console.log(pageList);
            let data = {
                "pageList":pageList,
                "curPage" : curPage,
                "pageLength":pageLength,
                "videoIndex" : curPageIndex,
                "finalPage" : finalPage,
                "finalUrl":finalUrl,
            };
            res.json(data);
            // res.render("index",{
            //     "pageList":pageList,
            //     "curPage" : curPage,
            //     "pageLength":pageLength,
            //     "videoIndex" : curPageIndex,
            //     "finalPage" : finalPage,
            //     "finalUrl":finalUrl,
            // });

        }
    ).catch(reason => {
        console.log(reason)
    });


    // mysqlTools.setMysqlData(function (result) {
    //
    //     console.log(curPageOrder);
    //     console.log("sapspapspaps");
    //     var final_page = curPageOrder.length;
    //     var fianl_url = "/"+final_page;
    //     console.log("final",final_page,typeof final_page,fianl_url);
    //
    //     res.render("index",{
    //         "videoIndex" : curPageOrder,
    //         "final_page" : final_page
    //
    //     });
    //     // res.send(curPageOrder);
    // });


};

exports.loadVideo = function (req, res) {
  // console.log(req.params);
  let dirname = req.params.dirname;
  console.log(dirname);
  // res.sendfile(path.join(__dirname,'../views/videoPlay.html'))
    res.render('videoPlay');
};

exports.loadVideoData = function (req, res) {
  // console.log(req.params);
  let dirname = req.params.dirname;
  console.log(dirname);
    let sql = `select * from iwara_info where dirname=? `;
    let presult;
    let myplaylisResult;
    mysqlTools.setMysqlData(sql,dirname).then(
        value => {
            presult=value;
            let sql = "select * from myplaylist where v_id_dirname=?";
            return mysqlTools.setMysqlData(sql,[dirname]);
        }
    ).then(value => {
        myplaylisResult = JSON.stringify(value);
        // console.log("========let my==========",myplaylisResult);
        let sql02 = 'select * from playlist';
        return mysqlTools.setMysqlData(sql02);

    }).then(value => {
        // console.log("========presult=======",presult);
        // console.log(value);
        let src = "/video/"+dirname+'/'+presult[0].title+".mp4";
        // console.log(src);
        src = encodeURI(src);
        // console.log(src);
        // console.log("========json========",myplaylisResult);
        let data = {
            "title":presult[0].title,
            "producer":presult[0].producer,
            "love":presult[0].love,
            "views":presult[0].views,
            "description":presult[0].description,
            "src" : src,
            "dirname":dirname,
            "isLoved":presult[0].isLoved,
            "playlist":value,
            "myplaylisResult":myplaylisResult,
        };
        res.json(data);
    });

};

exports.addLoved = function(req,res){
    let dirname = req.params.dirname;
    console.log(dirname);
    console.log("======adddloved",req.query);
    console.log("======papams",req.params);
    let addValue = req.query.add;
    // let shujuceshi = [{"aaa":dirname}];
    // res.json(shujuceshi)
    // mysqlTools.selectBydirname(dirname).then(value => {
    //     let videoId = value.;
    // })
    let sql = 'update iwara_info set isLoved=? where dirname=?';
    mysqlTools.setMysqlData(sql,[addValue,dirname]).then(value => {
        console.log(value);
    });
    let sql02 = 'select * from iwara_info where dirname=?';
    mysqlTools.setMysqlData(sql02,[dirname]).then(value => {
        console.log(value[0]);
        res.json({"isLoved":value[0].isLoved});
    })

    // mysqlTools.addMysqlLoved().then(value => {
    //
    // })
};

exports.addList = function(req,res){
    let dirname = req.params.dirname;
    let addName = req.query.addName;
    console.log("===========addName==============",addName);
    let sql = 'insert into playlist (playListName) values(?)';
    mysqlTools.setMysqlData(sql,[addName]).then(value => {
        let sql02 = 'select * from playlist';
        return mysqlTools.setMysqlData(sql02);
    }).then(value => {
        let json_value = JSON.stringify(value);
        res.json(json_value);
    })
};

exports.addMyList = function(req,res){
    let dirname = req.params.dirname;
    let isMylist = req.query.isMylist;
    let playlist_id = req.query.playListId;
    let sql = "select * from myplaylist where v_id_dirname=? and p_id_playListId=?";
    mysqlTools.setMysqlData(sql,[dirname,playlist_id]).then(value => {
        if (value.length!==0 && isMylist==='true' ){
            let sql02 = "update myplaylist set v_id_dirname=?,p_id_playListId=? where v_id_dirname=? and p_id_playListId=?";
            console.log(sql02);
            return mysqlTools.setMysqlData(sql02,[dirname,playlist_id],dirname,playlist_id)
        }
        else if(value.length!==0 && isMylist==='false' ){
            let sql02 = "delete from myplaylist where v_id_dirname=? and p_id_playListId=?";
            console.log(sql02);
            return mysqlTools.setMysqlData(sql02,[dirname,playlist_id]);
        }
        else if(value.length===0 && isMylist==='true' ){
            let sql02 = "insert into myplaylist (v_id_dirname,p_id_playListId) value(?,?)";
            console.log(sql02);
            return mysqlTools.setMysqlData(sql02,[dirname,playlist_id]);
        }
    }).then(value=>{
        console.log("--------列表结果-------------",value);
        let json_value = JSON.stringify(value);
        res.json(json_value);
    })
};


exports.deleteList = function(req,res){
    let dirname = req.params.dirname;
    let deletPlayListId =  req.query.deletPlayListId;
    let sql = "DELETE FROM playlist WHERE playListId=?";
    mysqlTools.setMysqlData(sql,deletPlayListId).then(value => {
        console.log("---------deleteplaylist------s-------",value);
        let sql = "DELETE FROM myplaylist WHERE p_id_playListId=?";
        return mysqlTools.setMysqlData(sql,deletPlayListId);
    }).then(value => {
        let json_value = JSON.stringify(value);
        res.json(json_value);
    })
};

exports.src = function (req,res) {

    
};