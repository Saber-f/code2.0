requestScreenCapture(true)   
var s = 2                                         // 初始状态(点击收藏作品之后)
while(1){
    log(s);
    switch(s){
        case 0:                                     // 退出到首页
            while(!isc(520, 1040, -12771560))
                click2(1800, 600, 0.5)              // 点一下
            click2(520, 1040, 0.5);                 // 大厅
            click3(2160, 71, -198930, 0.5);         // X
            s = 1;
            break;

        case 1:
            click3(1875, 818, -1, 0.5)              // 娱乐
            click3(1820, 666, -14086137, 0.5)       // Uni
            click3(973, 1040, -11983587, 0.5)       // 收藏关注
            click3(305, 300, -10067873, 0.5)        // 收藏作品
            s = 2;
            break;

        case 2:             
            click3(1071, 245, -9279572, 0.5)        // 点击守！无限后
            s = 3;
            break;

        case 3:                       
            click3(744, 924, -9549506, 0.5)         // 创建房间
            s = 4;
            break;

        case 4:   
            click3(1100, 660, -14252357, 0.5)       // 私密房间
            s = 5;
            break;

        case 5:                              
            click3(1013, 850, -1785721, 0.5)        // 确认创建
            s = 6;
            break;

        case 6:     
            while(1){                             
                if (isc(1808, 1020, -1654140)){     // 开始游戏
                    click2(1808, 1020, 0.5);
                    s = 7;
                    while(isc(1808, 1020, -65536)){
                        click2(1808, 1020, 0.5);
                        if(isc(1900, 455, -1319215))
                            break;
                    }
                }
                if (s == 7)
                    break
                if (isc(1275, 75, -15331575)){       // 离队
                    click2(1275, 75, 0.5)
                    s = 2;
                    break;
                }
                if (isc(1100, 500, -6796963)){      // 返回房间失败
                    s = 0;   
                    break;
                }
                if(isc(1900, 455, -1319215)){      // 困难难度
                    s = 7;   
                    break;
                }
            }
            break;

        case 7:  
            while(1){
                if(isc(1900, 455, -1319215)){
                    click2(1900, 455, 0.5)          // 困难难度
                    s = 8;
                    break;
                }
            }
            break;

        case 8:                   
            brush();
            while(!isc(1658, 1000, -9418177));     // 返回房间
            sleep(6000)
            click2(1880, 1000, 0.5);
            s = 6;
    }
}


function brush(){
    click2(1594,583,1)                          // 选判官
    for(var i=0; i<6; i++){
        click2(1608,1010,0.1);                  // 加被动     
        click2(1600,760,0.1);                   // 加一技能                       
        click2(1700,593,0.1);                   // 加二技能
        click2(1906,508,0.1);                   // 加大招
    }
    swipe2(370,840,470,900,5500,0.5);           // 走到角落
    click2(915,490,0.5);                        // 领取buff
    for(var i=0; i<4; i++){
        press(407,490,10);                      // 积分商店
        sleep(500);
        click2(1870,396,0.5);                   // 买金币
        swipe2(370,840,470,900,500,0.2);        // 走到角落
    }
    click2(915,275,0.5);                        // 打开商店
    click2(105,390,0.5);                        // 初级神装  
    click2(566,361,0.5);                        // 摄魂 
    for(var i=0; i<6; i++)
        click2(1158,982,0.1);                   // 购买
    click2(96,710,0.5);                         // 普通道具
    click2(260,500,0.5);                        // 消除防御塔
    click2(1137,990,0.5);                       // 购买
    click2(790,128,0.5);                        // 关闭商店
    swipe2(370,840,290,640,3100,0.5);           // 走到防守位置
    click2(1328,966,0.5);                       // 使用消除防御塔
    swipe2(2000,610,2230,395,500,270);          // 瞄准中路==
    click2(99,500,0.5);                         // 打开商店
    click2(96,710,0.5);                         // 普通道具
    click2(558,476,0.5);                        // 刷兵加速
    for(var i=0; i<16; i++)
        click2(1158,982,1.5);                   // 购买
    click2(790,128,0.5);                        // 关闭商店

    log(81)
    while(1){
        if(isc(1658, 1000, -9418177))           // 出现返回房间选项
            return;
        if(isc(1671, 556, -2502716)){           // 开无尽
            click2(1671, 556, 0);
            break;
        }
    }
    var k = 0;

    log(82)
    while(true){
        if(isc(864, 384, -4377567))             // 如果胜利
            break;
        k = k + 1;
        if(k > 300){                            // ==
            click2(1470,950,0.5);               // 使用额外技能
            swipe2(370,840,370,960,2000,0.3);   // 向下走
            k = 0
        }
    }
    click2(1120, 990, 0.5);                     // 点击继续
}

// 颜色是否相近
function isc(x,y,num){
    sleep(500)
    var color = images.pixel(captureScreen(), x, y);      //获取颜色
    n = colors.parseColor(colors.toString(color));        //显示该颜色整数值
    n -= num;
    if(n*n < 1000000)
        return 1;
    else
        return 0;
}

function click2(x,y,t){
    click(x,y);
    sleep(t*1000);
}

function click3(x,y,c,t){
    while(!isc(x, y, c));
    click2(x, y, t)              
}

function swipe2(x1,y1,x2,y2,t1,t2){
    swipe(x1,y1,x2,y2,t1);
    sleep(t2*1000);
}