//金额转换算法
function formatNum(num) {
    // 将数字串转换成带逗号的显示方式
    if (!/^([+\-])?(\d+)(\.\d+)?$/.test(num)) {
        console.log("wrong!");
        return num;
    }
    let a = RegExp.$1;
    let b = RegExp.$2;
    let c = RegExp.$3;
    let re = new RegExp().compile("(\\d)(\\d{3})(,|$)");
    while (re.test(b))
        b = b.replace(re, "$1,$2$3");
    return a + "" + b + "" + c;
}

//消除特殊字符算法

function removeTip(str) {
    while (true) {
        if (str.indexOf('+') == -1 && str.indexOf('-') == -1 && str.indexOf(',') == -1) {
            break;
        } else {
            str = str.replace('+', '');
            str = str.replace('-', '');
            str = str.replace(',', '');
        }

    }
    return str;
}

//获得标准格式的日期
function getdate(date) {
    var year = date.getFullYear();
    var month =
        date.getMonth() + 1 < 10 ?
            "0" + (date.getMonth() + 1) :
            date.getMonth() + 1;
    var day =
        date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
    var hours =
        date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
    var minutes =
        date.getMinutes() < 10 ?
            "0" + date.getMinutes() :
            date.getMinutes();
    var seconds =
        date.getSeconds() < 10 ?
            "0" + date.getSeconds() :
            date.getSeconds();
    let time =
        year +
        "-" +
        month +
        "-" +
        day +
        " " +
        hours +
        ":" +
        minutes +
        ":" +
        seconds;
    return time
}
