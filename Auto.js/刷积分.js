requestScreenCapture(true)                   // 请求横屏截图
//bg()
while(true){
    while(1){
        click2(1925, 1016, 0.5)              // 开始游戏
        if (isc(1920, 450, -1319216)){       //普通难度
            click2(1920, 450, 1)
            break
        }
    }
    click2(1594,583,2)                       // 选判官
    for(var i=0; i<5; i++){
        click2(1608,1010,0.2)                // 加被动     
        click2(1600,760,0.2)                 // 加一技能                       
        click2(1700,593,0.2)                 // 加二技能
        click2(1906,508,0.2)                 // 加大招
    }
    swipe2(370,840,470,900,5500,1.0)         // 走到角落
    click2(915,490,1.0)                      // 领取buff
    for(var i=0; i<4; i++){
        press(407,490,10)                    // 积分商店
        sleep(1000)
        click2(1870,570,1)                   // 买金币
        swipe2(370,840,470,900,500,0.3)      // 走到角落
    }
    click2(915,275,1.0)                      // 打开商店
    click2(105,390,1.0)                      // 初级神装  
    click2(566,361,1.0)                      // 摄魂 
    for(var i=0; i<5; i++)
        click2(1158,982,0.6)                 // 购买
    click2(96,710,1.0)                       // 普通道具
    click2(260,500,1.0)                      // 消除防御塔
    click2(1137,990,1)                       // 购买
    click2(790,128,1.0)                      // 关闭商店
    swipe2(370,840,275,640,2700,1.0)         // 走到防守位置
    swipe2(2000,600,1964,416,500,1.0)        // 瞄准上路
    click2(1470,950,6)                       // 使用消除防御塔
    for(var i=0; i<22; i++)
        click2(1574,600,11)                  // 使用额外技能
    click2(99,500,1.0)                       // 打开商店
    click2(96,710,1.0)                       // 普通道具
    click2(558,476,1.0)                      // 刷兵加速
    click2(1158,982,1.5)                     // 购买
    click2(790,128,1)                        // 关闭商店
    click2(1574,600,1)                       // 使用额外技能
    swipe2(370,840,440,960,5000,0.3)         // 走到角落
    click2(495,238,1)                        // 击杀数商店
    click2(1860,400,1)                       // 武神甲
    swipe2(370,840,290,640,3200,1.0)         // 走到防守位置
    swipe2(2000,610,2230,395,500,9.5)        // 瞄准中路
    click2(99,500,1.0)                       // 打开商店
    click2(96,710,1.0)                       // 普通道具
    click2(558,476,1.0)                      // 刷兵加速
    for(var i=0; i<16; i++)
        click2(1158,982,1.5)                 // 购买
    click2(790,128,11)                       // 关闭商店
    click2(1880,125,1)                       // 关闭附近
    var k = 0
    while(true){
        click2(1800, 550, 0.5)               // 开无尽
        if(isc(1750, 999, -6856627))         // 返回房间
            break
        k = k + 1
        if(k > 200){
            click2(1574,600,0.5)             // 使用额外技能
            swipe2(370,840,370,960,2000,0.3) // 向下走
            k = 0
        }
    }
    sleep(1000)
    click2(1750, 999, 1)                  // 返回房间
}

function isc(x,y,num){
    var color = images.pixel(captureScreen(), x, y)       //获取颜色
    n = colors.parseColor(colors.toString(color))         //显示该颜色整数值
    n -= num
    if(n*n < 100)
        return 1
    else
        return 0
}

function click2(x,y,t){
    click(x,y)
    sleep(t*1000)
}

function swipe2(x1,y1,x2,y2,t1,t2){
    swipe(x1,y1,x2,y2,t1)
    sleep(t2*1000)
}


function bg(){
    home()                                   // home
    sleep(500)
    home()                                   // home
    sleep(500)
    home()                                   // home
    sleep(500)
    swipe2(700,1000,400,1000,100,1)          // 滑动,用100毫秒
    swipe2(600,300,600,900,300,1)            // 下拉
    swipe2(600,300,600,900,300,1)            // 下拉
    click2(969,653,5)                        // 清理
    swipe2(600,900,600,300,300,1)            // 上拉
    swipe2(600,900,600,300,300,1)            // 上拉
    click2(700,1675,14)                      // 点击平安京
    click2(1223,903,1)                       // 跳过动画
    click2(1223,903,1)                       // 知道了
    click2(1116,840,6.0)                     // 进入游戏
    click2(2016,102,1)                       // 关闭公告
    click2(1912,824,1)                       // 进入娱乐模式
    click2(1767,717,2)                       // 进入Uni
    click2(1015,1020,1)                      // 收藏关注
    click2(318,314,1)                        // 收藏作品
    click2(1206,314,2)                       // 点击作品
    click2(829,925,2)                        // 创建房间
    fc(1411, 688, -3516834, 0)               // 私密房间
    click2(1137,842,2)                       // 确认创建
}