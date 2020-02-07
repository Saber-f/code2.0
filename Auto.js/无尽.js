var n = 0;
t = 15;
while(true){
    press(1470,950,t);
    sleep(t);
    n++;
    if(2*t*n >= 20000){
        swipe(2000,610,2230,395,500);           // 瞄准中路
        n = 0;
    }
}

