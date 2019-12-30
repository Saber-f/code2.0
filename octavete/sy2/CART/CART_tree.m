function y = CART_tree(D, Z)
    E = Gini(D(:,end));
    y = [];
    if size(D,2) == 1
        y = [-1,-1];
    elseif E == 0
        y = [0,D(1,end)];
    else
        G = Gini_ndex(D);
        [~,s] = min(G);
        d = unique(D(:,s));
        a = 1:size(D,2);
        a(s) = [];
        Z_ = Z(s);
        Z(s) = [];
        for i = 1:length(d)
            y = [y;Z_,d(i)];
            y = [y;CART_tree(D(D(:,s)==d(i),a),Z)];
        end
    end
end