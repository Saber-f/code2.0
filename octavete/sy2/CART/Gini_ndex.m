function y = Gini_ndex(D)
    % 计算用属性a对样本D进行划分所产生的“基尼系数”
    y(1:size(D,2)-1) = 0;
    n = size(D,1);                      % 行数
    De = D(:,end);
    for i = 1:size(D,2)-1
        dt = D(:,i);
        d = unique(dt);
        for j = 1:length(d)
            s = dt == d(j);
            di = De(s,end);
            m = sum(s);
            y(i) = y(i) + m/n * Gini(di);
        end
    end
end