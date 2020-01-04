/*
requestScreenCapture(true)                                  //请求横屏截图
color = images.pixel(captureScreen(), 1750, 999)            //获取颜色
num = colors.parseColor(colors.toString(color))             //显示该颜色整数值
log(num)
*/



threads.start(function(){
    //在新线程执行的代码
    while(true){
        log("子线程");
    }
});
while(true){
    log("脚本主线程");
}