%% 数据
D= [5,5;
    1,5;
    4,5;
    4.5,4;
    5,1;
    4.7,1];

N = 3;  % 到N个簇时结束

Z = D;  % 初始聚类中心
C = {};
for i = 1:size(D,1)
    C{i} = D(i,:);
end

while true
    if size(Z,1) <= N 
        break;
    end

    d = inf;
    for i = 1:size(Z,1)-1
        for j = i+1:size(Z,1)
            d_ = Z(i,:) - Z(j,:);
            d_ = sum(d_ .* d_);
            if d_ < d
                d = d_;
                I = [i,j];
            end
        end
    end

    C{I(1)} = [C{I(1)};C{I(2)}];
    Z(I(1),:) = sum(C{I(1)}) / size(C{I(1)},1);
    C(I(2)) = [];
    Z(I(2),:) = [];
end

Z       % 聚类中心
C       % 聚类结果