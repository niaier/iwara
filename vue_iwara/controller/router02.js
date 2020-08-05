const mysqlTools = require("../moduls/mysqlTools");
const dataProcess = require("../moduls/dataProcessing");
const pageTools = require("../moduls/pageTools");
const page_List =pageTools.page_List;

exports.showIndex = function (req,res){
    let cur_page = 0;
    const p1 = mysqlTools.setMysqlData();
    p1.then(
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
                "final_url":final_url
            });
        }
    ).catch(reason => {
        console.log(reason)
    });

    // (result=>{});

};


exports.showPage = function(req,res){
    let cur_page = Number(req.params.page);
    let p = req.params;
    if (!cur_page && cur_page!==0) {
        // res.send("输入正确页码");
        console.log("错误参数",req.params);
        res.render("404");
    }


    // const p1 = mysqlTools.setMysqlData();
    mysqlTools.setMysqlData().then(
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
            let final_page = slicedData.length;
            let final_url = "/"+(final_page-1);
            let pageList = page_List(cur_page,final_page);
            // console.log(final_url);

            res.render("index",{
                "pageList":pageList,
                "curPage" : cur_page,
                "pageLength":pageLength,
                "videoIndex" : cur_page_index,
                "final_page" : final_page,
                "final_url":final_url
            });
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


exports.showVideo = function (req,res) {

    console.log(req.params);
    let dirname = req.params.dirname;

    console.log(dirname);


    //   mysqlTools.selectTitle(dirname,result=>{
    //     console.log(result);
    //     let src = "/video/"+dirname+'/'+result[0].title+".mp4";
    //     console.log(src);
    //     src = encodeURI(src);
    //     console.log(src);
    //     res.render("videoPlay",{
    //         "title":result[0].title,
    //         "producer":result[0].producer,
    //         "love":result[0].love,
    //         "views":result[0].views,
    //         "description":result[0].description,
    //         "src" : src,
    //         "dirname":dirname
    //     });
    // });
    mysqlTools.selectTitle(dirname).then(
        result => {
            console.log(result);
            let src = "/video/"+dirname+'/'+result[0].title+".mp4";
            console.log(src);
            src = encodeURI(src);
            console.log(src);
            res.render("videoPlay",{
                "title":result[0].title,
                "producer":result[0].producer,
                "love":result[0].love,
                "views":result[0].views,
                "description":result[0].description,
                "src" : src,
                "dirname":dirname
            });
        }
    );





    // [0].title+'.mp4';

};


exports.addLoved = function(req,res){
    let dirname = req.params.dirname;

    // let shujuceshi = [{"aaa":dirname}];
    // res.json(shujuceshi)
    // mysqlTools.selectBydirname(dirname).then(value => {
    //     let videoId = value.;
    // })


    // mysqlTools.addMysqlLoved().then(value => {
    //
    // })
};

exports.src = function (req,res) {


};
