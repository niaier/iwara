// //
// var mysqlData = [
//     {name:'Liming',age:'25'},
//     {name:'Liming',age:'25'},
//     {name:'Liming',age:'25'},
//     {name:'Liming',age:'25'},
//     {name:'Liming',age:'25'},
//     {name:'Liming',age:'25'},
//     {name:'Liming',age:'234'},
//     {name:'Liming',age:'243'},
//     {name:'Liming',age:'25'},
//     {name:'Liming',age:'26'},
// ];

// dataSlice = function (mysqlData) {
//
//     var result = [];
//     for(var i=0;i<mysqlData.length;i+=3){
//         result.push(mysqlData.slice(i,i+3));
//     }
//     return result;
//
// };
exports.dataSlice = function (mysqlData) {

    var slicelist = [];
    for(var i=0;i<mysqlData.length;i+=36){
        slicelist.push(mysqlData.slice(i,i+36));
    }
    return slicelist;

};

// console.log(dataSlice(mysqlData));

