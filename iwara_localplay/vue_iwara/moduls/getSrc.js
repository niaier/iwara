const path =require('path');
const fs =require('fs');
var mysql = require('mysql');


var connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'root',
        port: '3306',
        database: 'iwara'
    });

connection.connect(function () {
        console.log('mysql链接成功！')
    });

exports.selectTitle = function (dirname,callback) {
        var sql = `select * from iwara_info where dirname=?`;
        connection.query(sql, dirname, function (err, result) {
            if (err) {
                console.log('[错误] --- ', err.message);
                return;
            }
            // connection.release();
            console.log(result);
            callback(result);  //此处callback就是将值取出来

        });
    // connection.end();
    };

//
// selectTitle(dirname="201501030621",result=>{
//     console.log("ppppppppppp",result);
// });


// exports.getSrc = getSrc;
