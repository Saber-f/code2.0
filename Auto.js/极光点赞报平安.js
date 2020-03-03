auto.waitFor();                     // 检查等待开启无障碍服务
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

for(var i=0; i<2; i++){
    x = 160 + i*250;
    click2(x, 1377,6);              // 打开极光单词
    click2(947, 619, 0.5);          // X
    click2(920, 1040, 1)            // 开始学习
    click2(800, 1280, 1);           // 继续学习
    for (var j = 0; j<n; j++){
        sleep(1000)
        click2(550,1650, t);        // 不确定
        click2(310, 2160, t);       // 知道了
    }
    for(var j=0; j<3; j++){
        back();
        sleep(200);
    }
    sleep(1000);
}



// 点赞
app.startActivity({data:"mqq://card/show_pslcard?&uin=670824032"});
sleep(2000)
for(var i=0; i<10; i++)
    click2(1008,620,0.1);


// 报平安
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



function click2(x,y,t){
    click(x,y);
    sleep(t*1000);
}


function swipe2(x1,y1,x2,y2,t1,t2){
    swipe(x1,y1,x2,y2,t1);
    sleep(t2*1000);
}
