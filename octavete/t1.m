minsup = 3;
minconf=5/7;
name_num = {"牛奶","面包","薯片","果汁","奶酪"};
D = [1,2,3,0;
    1,2,4,0;
    1,3,4,0;
    1,2,3,5;
    1,3,5,0;
    2,4,5,0;
    1,2,3,4];

C1 = zeros(length(name_num),2);
for i = 1:length(name_num)
    C1(i,1) = i;
    C1(i,2) = sum(sum(D == i));
end

Lk = Ck2Lk(C1,minsup);
while true
    Ck = Lk2Ckp1(Lk,D);
    if isempty(Ck)
        Lk(end) = [];   % 得到平凡项集
        break;
    end
    Lk_ = Ck2Lk(Ck,minsup);
    if isempty(Lk_)
        Lk(end) = [];   % 得到平凡项集
        break;
    end
    Lk = Lk_;
end

W = size(Lk,1);
L = size(Lk,2);
for w = 1:W
    for i = 1:floor(L/2)
        A = combntns(Lk(w,:),i);            %所有组合
        
        for j = 1:size(A,1)
            a = A(j,:);
            b = setdiff(Lk,a);
            c = f2(a,b,D);

            if c >= minconf
                fprintf(mat2str(a));
                fprintf("===>");
                fprintf(mat2str(b));
                fprintf(" ");
                fprintf(num2str(c))
                fprintf("\n");
            end
            if i ~= L - i
                c = f2(b,a,D);
                if c >= minconf
                    fprintf(mat2str(b));
                    fprintf("===>");
                    fprintf(mat2str(a));
                    fprintf(" ");
                    fprintf(num2str(c))
                    fprintf("\n");
                end
            end
        end
    end
end


%% 函数
function Lk = Ck2Lk(Ck,minsup) 
    Lk = Ck(Ck(:,end) >= minsup,:);
end

function Ckp1 = Lk2Ckp1(Lk,D)
    L = size(Lk,1);%Lk的行�?
    W = size(Lk,2);%Lk的列�?
    Ckp1 = [];
    for i = 1:L
       for j = 1:L
           if Lk(i,W - 1) < Lk(j,W - 1)
               if W == 2 || Lk(i,1:W -2) == Lk(j,1:W - 2)
                   a = [Lk(i,1:W - 1),Lk(j,W - 1)];
                   n = f1(a,D);
                   Ckp1 = [Ckp1;[a,n]];
               end
           end
       end
    end
end

function n = f1(a,D)
    n = 0;          %D有多少行包含了a
    for i = 1:length(D)
        if all(ismember(a,D(i,:)))
            n = n + 1;
        end
    end
end

function y = f2(a,b,D)
    n = 0;  %a出现且b出现的次�?
    m = 0;  %a出现的次�?
    for i = 1:length(D)
        if all(ismember(a,D(i,:)))
            if all(ismember(b,D(i,:)))
                n = n + 1;
            end
            m = m + 1;
        end
    end

    y = n/m;
end