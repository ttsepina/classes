function [Rnew,Cnew] = evolveState(R,C,m,n)

cell = Igen(m,n,R,C);

fixedcell = cell   ;
[A,B,G,H] = nearby2(fixedcell);
D = livescore(m,n,A,B); %Matrix counting the number of nearby living cells for each position of the original living cells of the cycle for 
W = livescore(m,n,G,H);


p = W==3;  %Where dead cells have 3 neighbors
o = D==3 ; %Where living cells have 3 neighbors
l = D==2;  %Where living cells have 2 neighbors
    
% p's conditional is the number of living cells near a dead cell for it to come to life
% o and l's conditionals are the number of living cells allowed near a
% living cell for them to survive

    newCells=double(p+o+l);
    updateCells(newCells,m,n);
    [Rnew,Cnew] = coordGen(newCells);
end