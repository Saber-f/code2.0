launchApp('微信');
sleep(500)
click2(620,330,0.5);            // 掌上川师
click2(600,2100,0.5);           // 报平安
click2(600,1860,4);             // 本科生
click2(935,2011,2);             // 新增
swipe2(600,2000,600,0,300,0.1)    // 下滑
swipe2(600,2000,600,0,300,0.1)    // 下滑
click2(600,2170,0.5);               //确认提交
click2(747,1344,2);                 // 确认
for(var i=0; i<5; i++){
    back();
    sleep(300);
}




//f(920, 1000)
function f(x, y){
    requestScreenCapture()                                      //请求横屏截图
    color = images.pixel(captureScreen(), x, y)                 //获取颜色
    num = colors.parseColor(colors.toString(color))             //显示该颜色整数值
    log('click3(%d, %d, %d, 0.5)',x,y,color)
}



function click2(x,y,t){
    click(x,y)
    sleep(t*1000)
}

function swipe2(x1,y1,x2,y2,t1,t2){
    swipe(x1,y1,x2,y2,t1)
    sleep(t2*1000)
}
