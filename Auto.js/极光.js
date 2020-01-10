var n = 10;
var t = 25;

requestScreenCapture();             // 申请截图权限


if(0){
    // 返回第一个桌面
    for (var i=0; i<3; i++){
        home();
        sleep(500);
    }
    click2(920, 1377,6);           // 打开极光单词
    click2(920, 1000, 1)            // 继续学习
    click2(800, 1250, 1);           // 继续学习
    for (var i = 0; i<n; i++){
        sleep(1000)
        click2(550,1650, t);        // 不确定
        click2(310, 2160, t);       // 知道了
    }
}

if(1){
    // 返回第一个桌面
    for (var i=0; i<3; i++){
        home();
        sleep(500);
    }
    swipe2(700,1120,200,1120,400,0.5);      // 右滑
    swipe2(700,1120,200,1120,400,1.0);      // 右滑
    click2(410, 850,6);                     // 打开微信分生
    click2(400, 2150, 1);                   // 打开通讯录
    click2(95, 740, 1);                     // 公众号
    click2(110, 360, 1);                    // 极光单词
    click2(610, 2157, 1);                   // 开始学习
    click2(640, 2015, 3);                   // 开始学习
    click2(777, 1020, 1);                   // 继续学习
    click2(560, 1270, 3);                   // 继续学习
    for (var i = 0; i<n; i++){
        sleep(1000)
        click2(550,1650, t);                // 不确定
        click2(310, 2160, t);               // 知道了
    }   
    home();         
}

function click2(x,y,t){
    click(x,y);
    sleep(t*1000);
}


function swipe2(x1,y1,x2,y2,t1,t2){
    swipe(x1,y1,x2,y2,t1);
    sleep(t2*1000);
}
