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


n = size(D,1);
for i = 1:size(D2,1)
    d = unique(D(:,end));
    p = 0;
    for j = 1:length(d)
        s = D(:,end)==d(j);
        m = sum(s);
        p2 = m/n;
        for k = 1:size(D2,2)
            d2 = D(s,k);
            p2 = p2 * sum(d2 == D2(i,k)) / length(d2);
        end
        if p < p2
            p = p2;
            I(i,1) = d(j);
        end
    end
end

[D2,I]








% 参考::https://blog.csdn.net/nextdoor6/article/details/82903946