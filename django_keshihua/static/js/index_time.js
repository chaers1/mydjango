// 获取当前时间
function getCurrentTime() {
    var now = new Date();
    var year = now.getFullYear();
    var month = now.getMonth() + 1; // 月份从0开始，需要加1
    var day = now.getDate();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    // 格式化时间
    var formattedTime = year + "年" + formatTime(month) + "月" + formatTime(day) + "日" +
                        formatTime(hours) + ":" + formatTime(minutes) + ":" + formatTime(seconds);
    return formattedTime;
}

// 格式化时间，确保时、分、秒的显示格式为两位数
function formatTime(time) {
    if (time < 10) {
        return "0" + time;
    } else {
        return time;
    }
}

// 更新页面上的时间
function updateTime() {
    var currentTimeElement = document.getElementById("current-time");
    if (currentTimeElement) {
        currentTimeElement.innerText = "当前时间：" + getCurrentTime();
    }
}

// 每秒更新一次时间
setInterval(updateTime, 1000);
