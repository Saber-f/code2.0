%% 数据
D= [
    0,1,2,2,3;
    1,0,2,4,3;
    2,2,0,1,4;
    2,4,1,0,3;
    3,3,4,3,0];

N = 2;  % 聚类中心个数

Z = [1,4];
Z_ = Z;        % 新的聚类中心

while true
    C = {};
    for i = 1:N
        C{i} = [];
    end

    for i = 1:size(D,1)
        d = D(i,Z);
        [~,s] = min(d);
        C{s} = [C{s},];
    end

    for i = 1:N
        Z_(i) = 
    end
    if all(all(Z==Z_))
        break;
    end
    Z = Z_;
end

Z       % 聚类中心
C       % 聚类结果