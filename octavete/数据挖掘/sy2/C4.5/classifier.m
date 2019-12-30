function y = classifier(D,Y)
    for i = 1:size(D,1)
        j = 1;
        t = Y(j,1);     % 当前根据第几列判断
        while true
            if Y(j,1) == t && D(i,t) == Y(j,2)
                j = j + 1;
                t = Y(j,1);
                if  Y(j,1) < 1
                    if Y(j,1) == 0
                        y(i,1) = Y(j,2);
                    else
                        y(i,1) = -1;
                    end
                    break;
                end
            else
                j = j + 1;
            end

        end
    end
end