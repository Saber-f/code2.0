f(1808, 1020)
function f(x, y){
    requestScreenCapture(true)                                  //请求横屏截图
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
