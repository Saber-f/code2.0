function y = Ent(D)
    % 计算信息熵
    d = unique(D);
    n = length(D);                 % 分类类数
    l = length(d);
    y = 0;
    for i = 1:l
        pk = sum(D == d(i))/n;
        y = y - pk * log2(pk);
    end
end