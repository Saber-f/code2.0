var n = 10;
var t = 25;

requestScreenCapture();             // 申请截图权限

// 返回第一个桌面
for (var i=0; i<2; i++){
    home();
    sleep(1000);
}
swipe2(600,1100,200,1100,300,0.8);
swipe2(600,1100,200,1100,300,0.8);

x = 410;
for(var i=0; i<1; i++){
    click2(x, 1377,6);              // 打开极光单词
    click2(947, 619, 0.5);          // X
    click2(920, 1040, 1)            // 开始学习
    click2(800, 1280, 1);           // 继续学习
    for (var i = 0; i<n; i++){
        sleep(1000)
        click2(550,1650, t);        // 不确定
        click2(310, 2160, t);       // 知道了
    }
    x += 250;
    home()
    sleep(1000);
}

function click2(x,y,t){
    click(x,y);
    sleep(t*1000);
}


function swipe2(x1,y1,x2,y2,t1,t2){
    swipe(x1,y1,x2,y2,t1);
    sleep(t2*1000);
}
