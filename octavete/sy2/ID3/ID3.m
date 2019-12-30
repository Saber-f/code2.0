# 数据
num_name = {
    {'fine','cloudy','rain','fine'},
    {'hot','warmth','cool'},
    {'hight','normal'},
    {'no','yes'},
    {'no','yes'}
    };

D = [
    1,1,1,1,1;
    1,1,1,2,1;
    2,1,1,1,2;
    3,2,1,1,2;
    3,3,2,1,2;
    3,3,2,2,1;
    2,3,2,2,2;
    1,2,1,1,1;
    1,3,2,1,2;
    3,3,2,1,2;
    1,3,2,2,2;
    2,2,1,2,2;
    2,1,2,1,2;
    3,2,1,2,1];

D2 = [
    2,3,1,2;
    1,1,2,2];


Y = ID3_tree(D,1:size(D,2));
C = classifier(D2,Y);
[D2,C]


% 参考资料::https://blog.csdn.net/qq_27717921/article/details/74784400