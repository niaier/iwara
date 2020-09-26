const mysqlTools = require("../modules/mysqlTools");
const dataProcess = require("../modules/dataProcessing");
const pageTools = require("../modules/pageTools");
const page_List = pageTools.page_List;
const path = require('path');



exports.loadPageData = function (req, res) {
    console.log(req.query.page, "==============");
    let curPage = req.query.page;
    let sortBy = req.query.sortby || 'upload_time';
    console.log(sortBy)
    if (curPage === undefined) {
        curPage = 0;
    }
    else {
        curPage = Number(req.query.page);
    }
    console.log("当前页面转化数字", curPage);
    if (!curPage && curPage !== 0) {
        // res.send("输入正确页码");
        console.log("错误参数", req.query);
        res.render("404")
    }
    // const p1 = mysqlTools.setMysqlData();
    let sql = 'SELECT * FROM iwara_info WHERE isDown=1 order by ' + sortBy + ' desc';
    mysqlTools.setMysqlData(sql).then(
        value => {
            //当前页的目录
            let slicedData = dataProcess.dataSlice(value);
            let curPageIndex = slicedData[curPage];
            let pageLength = curPageIndex.length;
            //切片分组的数
            // console.log(dataProcess.dataSlice(value).length);
            console.log("当前页项目数量", curPageIndex.length);
            console.log("当前页参数", req.params);
            // console.log(curPageOrder);
            let finalPage = slicedData.length;
            let finalUrl = "/" + (finalPage - 1);
            let pageList = page_List(curPage, finalPage);
            console.log(pageList);
            let data = {
                "pageList": pageList,
                "curPage": curPage,
                "pageLength": pageLength,
                "videoIndex": curPageIndex,
                "finalPage": finalPage,
                "finalUrl": finalUrl,
            };
            res.json(data);
        }
    ).catch(reason => {
        console.log(reason)
    });



};

exports.loadLovePage = function (req, res) {
    let query = req.query;
    console.log("loadLovePage----query", query);
    let love_level = req.query.love_level;
    console.log(love_level, 'love_level');
    let curPage = req.query.page;
    let sortBy = req.query.sortby || 'upload_time';
    console.log(sortBy)
    if (curPage === undefined) {
        curPage = 0;
    }
    else {
        curPage = Number(req.query.page);
    }
    console.log("当前页面转化数字", curPage);
    if (!curPage && curPage !== 0) {
        // res.send("输入正确页码");
        console.log("错误参数", req.query);
        res.render("404")
    }
    // 查询喜爱的列表
    let sql;

    if (love_level == undefined) {
        sql = "SELECT * FROM iwara_info,love_list WHERE love_list.`v_id`=iwara_info.`dirname` AND love_list.`love_level`>0 order by " + sortBy + " desc";
    }
    else {
        sql = "SELECT * FROM iwara_info,love_list WHERE love_list.`v_id`=iwara_info.`dirname` AND love_list.`love_level`>0 AND love_list.`love_level`=? order by " + sortBy + " desc";
    }

    console.log(sql)
    mysqlTools.setMysqlData(sql, love_level).then(
        value => {
            let slicedData = dataProcess.dataSlice(value);
            let curPageIndex = slicedData[curPage];
            let pageLength = curPageIndex.length;
            //切片分组的数
            // console.log(dataProcess.dataSlice(value).length);
            console.log("当前页项目数量", curPageIndex.length);
            console.log("当前页参数", req.params);
            // console.log(curPageOrder);
            let finalPage = slicedData.length;
            let finalUrl = "/" + (finalPage - 1);
            let pageList = page_List(curPage, finalPage);
            console.log(pageList);
            let data = {
                "pageList": pageList,
                "curPage": curPage,
                "pageLength": pageLength,
                "videoIndex": curPageIndex,
                "finalPage": finalPage,
                "finalUrl": finalUrl,
            };
            res.json(data);

        }
    ).catch(reason => {
        console.log(reason)
        res.setHeader('Content-Type', 'text/plain;charset=utf-8');
        res.end('超出查询范围');
    });




}

//playlist界面
exports.loadPlayListData = function (req, res) {
    let sql = 'select * from playlist';
    mysqlTools.setMysqlData(sql).then(value => {
        console.log(value);
        res.json(value);
    })
}

exports.loadMyPlayListData = function(req,res){
    let love_level = req.query.love_level;
    let curPage = req.query.page;
    let sortBy = req.query.sortby || 'upload_time';
    let playListId = req.query.playlistid ||'1';
    let sql;
    console.log('=====================\n',
    req.query,
    curPage,"----",playListId,love_level,
    '\n===================================')
    if(love_level==undefined){
        sql = 'SELECT * FROM myplaylist,iwara_info WHERE myplaylist.`p_id_playListId`=? AND myplaylist.v_id_dirname = iwara_info.dirname order by ' + sortBy + " desc";

    }
    else{
    sql = 'SELECT * FROM myplaylist,iwara_info,love_list WHERE myplaylist.`p_id_playListId`=? AND myplaylist.v_id_dirname = iwara_info.dirname AND iwara_info.dirname= love_list.`v_id`  AND love_list.`love_level`=? order by ' + sortBy + " desc";

    }
    console.log(sql);
    mysqlTools.setMysqlData(sql,[playListId,love_level]).then(value => {
        console.log(value);
        let slicedData = dataProcess.dataSlice(value);
        let curPageIndex = slicedData[curPage];
        let pageLength = curPageIndex.length;
        //切片分组的数
        // console.log(dataProcess.dataSlice(value).length);
        console.log("当前页项目数量", curPageIndex.length);
        console.log("当前页参数", req.params);
        let finalPage = slicedData.length;
        let finalUrl = "/" + (finalPage - 1);
        let pageList = page_List(curPage, finalPage);
        console.log(pageList);
        let data = {
            "pageList": pageList,
            "curPage": curPage,
            "pageLength": pageLength,
            "videoIndex": curPageIndex,
            "finalPage": finalPage,
            "finalUrl": finalUrl,
        };
        res.json(data);
    }).catch(reason => {
        console.log(reason)
        res.setHeader('Content-Type', 'text/plain;charset=utf-8');
        res.json('none');
    });

}

// 播放界面数据
exports.loadVideoData = function (req, res) {
    //获取当前页参数
    let dirname = req.params.dirname;
    console.log(dirname);
    //根据dirname从数据库获取数据
    let sql = `select * from iwara_info where dirname=? `;
    let presult;
    let myplaylisResult;
    mysqlTools.setMysqlData(sql, dirname
    ).then(value => {
        presult = value;
        let sql = "select * from myplaylist where v_id_dirname=?";
        return mysqlTools.setMysqlData(sql, [dirname]);
    }
    ).then(value => {
        myplaylisResult = JSON.stringify(value);
        let sql02 = 'select * from playlist';
        return mysqlTools.setMysqlData(sql02);

    }).then(value => {
        // console.log("========presult=======",presult);
        // console.log(value);
        let src = "/video/" + dirname + '/' + presult[0].title + ".mp4";
        // console.log(src);
        src = encodeURI(src);
        // console.log(src);
        // console.log("========json========",myplaylisResult);
        let data = {
            "title": presult[0].title,
            "producer": presult[0].producer,
            "love": presult[0].love,
            "views": presult[0].views,
            "description": presult[0].description,
            "src": src,
            "dirname": dirname,
            "isLoved": presult[0].isLoved,
            "playlist": value,
            "myplaylisResult": myplaylisResult,
        };
        res.json(data);
    });

};

// 播放界面info列表数据
exports.loadVideoInfo = function (req, res) {
    let dirname = req.params.dirname;
    let sql = `select * from iwara_info where dirname=? `;
    mysqlTools.setMysqlData(sql, dirname)
        .then(value => {
            let data = value;
            res.json(value[0])
        })
}


//播放界面love_list数据
exports.loadLoveList = function (req, res) {
    let v_id = req.params.dirname;
    let sql = `select * from love_list where v_id=? `;
    mysqlTools.setMysqlData(sql, v_id)
        .then(value => {
            let data = value;
            res.json(value[0])
        })
}
//播放界面myplaylist数据
exports.loadMyPlayList = function (req, res) {
    let dirname = req.params.dirname;
    // let sql = `select * from myplaylist where dirname=? `;
    let sql = `select * from myplaylist where v_id_dirname=?`;

    mysqlTools.setMysqlData(sql, dirname)
        .then(value => {
            let data = value;
            res.json(value)
        })
}
//播放界面playlist数据
exports.loadPlayList = function (req, res) {
    // let dirname = req.params.dirname;
    let sql = `select * from playlist`;
    mysqlTools.setMysqlData(sql, [])
        .then(value => {
            let data = value;
            res.json(value)
        })
}


exports.addLoved = function (req, res) {
    let v_id = req.params.dirname;
    let love_level = req.query.add;
    console.log("======love_level===", love_level)
    let sql = "select * from love_list where v_id=? "
    mysqlTools.setMysqlData(sql, v_id).then(value => {
        let sql;
        if (value.length) {
            sql = "update love_list set love_level=? where v_id=?";
            console.log("======love_level===", love_level, v_id, "pppppppppppppppp")
            return mysqlTools.setMysqlData(sql, [love_level, v_id])
        }
        else {
            sql = "insert into love_list (v_id,love_level) value (?,?)";
            return mysqlTools.setMysqlData(sql, [v_id, love_level])
        }

    }).then(value => {
        console.log(value);
        res.end();
    });

};

exports.addList = function (req, res) {
    let dirname = req.params.dirname;
    let addName = req.query.addName;
    console.log("===========addName==============", addName);
    let sql = 'insert into playlist (playListName) values(?)';
    mysqlTools.setMysqlData(sql, [addName]).then(value => {
        let sql02 = 'select * from playlist';
        return mysqlTools.setMysqlData(sql02);
    }).then(value => {
        let json_value = JSON.stringify(value);
        res.json(json_value);
    })
};

exports.addMyList = function (req, res) {
    let dirname = req.params.dirname;
    let isMylist = req.query.isMylist;
    let playlist_id = req.query.playListId;
    console.log("playlist_id", dirname, isMylist, playlist_id)
    let sql = "select * from myplaylist where v_id_dirname=? and p_id_playListId=?";
    mysqlTools.setMysqlData(sql, [dirname, playlist_id]).then(value => {
        console.log(value.length);
        if (value.length !== 0 && isMylist === 'true') {
            let sql02 = "update myplaylist set v_id_dirname=?,p_id_playListId=? where v_id_dirname=? and p_id_playListId=?";
            console.log(sql02);
            return mysqlTools.setMysqlData(sql02, [dirname, playlist_id], dirname, playlist_id)
        }
        else if (value.length !== 0 && isMylist === 'false') {
            let sql02 = "delete from myplaylist where v_id_dirname=? and p_id_playListId=?";
            console.log(sql02);
            return mysqlTools.setMysqlData(sql02, [dirname, playlist_id]);
        }
        else if (value.length === 0 && isMylist === 'true') {
            let sql02 = "insert into myplaylist (v_id_dirname,p_id_playListId) value(?,?)";
            console.log(sql02);
            return mysqlTools.setMysqlData(sql02, [dirname, playlist_id]);
        } else {
            console.log("都不是")
        }
    }).then(value => {
        console.log("--------列表结果-------------", value);
        let json_value = JSON.stringify(value);
        res.json(json_value);
    })
};


exports.deleteList = function (req, res) {
    let dirname = req.params.dirname;
    let deletPlayListId = req.query.deletPlayListId;
    let sql = "DELETE FROM playlist WHERE playListId=?";
    mysqlTools.setMysqlData(sql, deletPlayListId).then(value => {
        console.log("---------deleteplaylist------s-------", value);
        let sql = "DELETE FROM myplaylist WHERE p_id_playListId=?";
        return mysqlTools.setMysqlData(sql, deletPlayListId);
    }).then(value => {
        let json_value = JSON.stringify(value);
        res.json(json_value);
    })
};

exports.src = function (req, res) {


};