function y = Gini(D)
    % 计算基尼值
    d = unique(D);
    n = length(D);                 % 分类类数
    l = length(d);
    y = 1;
    for i = 1:l
        pk = sum(D == d(i))/n;
        y = y - pk * pk;
    end
end