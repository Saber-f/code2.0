D = [
    1,1;
    2,1;
    1,2;
    2,2;
    4,3;
    5,3;
    4,4;
    5,4];

N = 2;  % 聚类中心个数

Z = D([4,7],:);
Z_ = Z;        % 新的聚类中心

while true
    C = {};
    for i = 1:N
        C{i} = [];
    end
    for i = 1:size(D,1)
        d = Z - D(i,:);
        d = sum(d.*d,2);
        [~,s] = min(d);
        C{s} = [C{s};D(i,:)];
    end
    for i = 1:N
        Z_(i,:) = sum(C{i})/size(C{i},1);
    end
    if all(all(Z==Z_))
        break;
    end
    Z = Z_;
end

Z       % 聚类中心
C       % 聚类结果