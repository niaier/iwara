const path =require('path');
const fs =require('fs');
var mysql = require('mysql');

var connection = mysql.createConnection({
    host:'127.0.0.1',
    user:'root',
    password: 'root',
    port:'3306',
    database: 'iwara'
});
// a
connection.connect();

exports.setMysqlData = function(sql, value_list=[]){

    return new Promise((resolved, rejected)=>{
        connection.query(sql,value_list,function (err,result) {
            if(err){
                // res.render("404");
                console.log('Select Error - ',err.message);
            }
            else if(result === null){
                rejected(null);
            }
            else{
                resolved(result);
            }
        });

    });
};

// setMysqlData(sql).then(value => {
//     console.log(value)
// });