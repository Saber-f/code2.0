requestScreenCapture(true)                                  //请求横屏截图
color = images.pixel(captureScreen(),1411, 688)              //获取颜色
num = colors.parseColor(colors.toString(color))             //显示该颜色整数值
log(num)



swipe2(2000,600,1964,416,500,1.0)        // 瞄准上路



function click2(x,y,t){
    click(x,y)
    sleep(t*1000)
}

function swipe2(x1,y1,x2,y2,t1,t2){
    swipe(x1,y1,x2,y2,t1)
    sleep(t2*1000)
}
