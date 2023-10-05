function [Q,M] = coordGen(I)
    [Q,M] = find(I);
    Q = Q';
    M = M';
     Q = Q +1;
     M = M +1;
end