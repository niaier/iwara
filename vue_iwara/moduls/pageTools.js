// 获取数组下标
function getArrayIndex(arr, obj) {
    var i = arr.length;
    while (i--) {
        if (arr[i] === obj) {
            return i;
        }
    }
    return -1;
};



exports.page_List = function (cur_page,final_page) {
    let pageList =[];
    let pageUrl =[];
    let pageObj = {};
    if(cur_page < 5){
        let pageList = [1,2,3,4,5,6,7,'...',final_page];
        let pageUrl = [1,2,3,4,5,6,7,8,final_page];
        let pageObj = {
            'pagelist':pageList,
            'pageurl':pageUrl,
            'curPageOrder':getArrayIndex(pageUrl,cur_page+1)
        };
        return pageObj
    }
    else if (final_page-4 > cur_page >=5){
        let pageList = [1,'...',cur_page-2,cur_page-1,cur_page,cur_page+1,cur_page+2,'...',final_page];
        let pageUrl = [1,cur_page-3,cur_page-2,cur_page-1,cur_page,cur_page+1,cur_page+2,cur_page+3,final_page];
        let pageObj = {
            'pagelist':pageList,
            'pageurl':pageUrl,
            'curPageOrder':getArrayIndex(pageUrl,cur_page+1)
        };
        return pageObj
    }
    else if(cur_page < final_page-4){
        let pageList = [1,'...',cur_page-2,cur_page-1,cur_page,cur_page+1,cur_page+2,'...',final_page];
        let pageUrl = [1,cur_page-3,cur_page-2,cur_page-1,cur_page,cur_page+1,cur_page+2,cur_page+3,final_page];
        let pageObj = {
            'pagelist':pageList,
            'pageurl':pageUrl,
            'curPageOrder':getArrayIndex(pageUrl,cur_page+1)
        };
        return pageObj
    }
    else if (cur_page >= final_page-4) {
        let pageList = [1,'...',final_page-6,final_page-5,final_page-4,final_page-3,final_page-2,final_page-1,final_page];
        let pageUrl = [1,final_page-7,final_page-6,final_page-5,final_page-4,final_page-3,final_page-2,final_page-1,final_page];
        let pageObj = {
            'pagelist':pageList,
            'pageurl':pageUrl,
            'curPageOrder':getArrayIndex(pageUrl,cur_page+1)
        };
        return pageObj
    }
};

// console.log(page_List(7,20));