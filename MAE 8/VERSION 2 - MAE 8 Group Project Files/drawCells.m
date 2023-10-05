function drawCells(m,n)

hold on
axis off
pbaspect([1 1 1])

X = [0:m;0:m];
Y = [zeros(1,m+1);m*ones(1,m+1)];

line(X,Y,'Color',0.8*[1 1 1],'LineWidth', 3)
line(Y,X,'Color',0.8*[1 1 1],'LineWidth', 3)
    
end