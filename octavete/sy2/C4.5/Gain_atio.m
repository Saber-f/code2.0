function y = Gain_atio(D)
    % 计算用属性a对样本D进行划分所带来的“增益率”
    y(1:size(D,2)-1) = Ent(D(:,end));   % 信息熵
    n = size(D,1);                      % 行数
    De = D(:,end);
    for i = 1:size(D,2)-1
        dt = D(:,i);
        d = unique(dt);
        IVa = 0;                            % +
        for j = 1:length(d)
            s = dt == d(j);
            di = De(s,end);
            m = sum(s);
            y(i) = y(i) - m/n * Ent(di);
            IVa = IVa - m/n * log2(m/n);    % +
        end
        y(i) = y(i) / IVa;                  % +
    end
end