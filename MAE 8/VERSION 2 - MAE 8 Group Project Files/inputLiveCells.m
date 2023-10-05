function [R,C] = inputLiveCells(m,n)
startCells=zeros(m,n);
%Prompt the user (via Figure) to initialize cells
title('Click on the cells you wish to make live. Press <Enter> when done.')

%Recieve mouse coordinates for each click (until user presses <ENTER>)
i = 0;
[x,y] = ginput(1); %Get new mouse coordinates
while ~isempty(x) && ceil(x) <= n && ceil(y) <= m && ceil(x) >= 0 && ceil(y) >= 0 %If user did not click <Enter> (or clicked outside of grid)
    i = i + 1; %count cells that are made live
    c = ceil(x); %Determine row index of the i-th cell clicked
    r = ceil(y); %Determine column index of the i-th cell clicked
    startCells(r,c)=1;
    rectangle('Position',[c-1,r-1,1,1],'FaceColor','k','EdgeColor',0.8*[1 1 1],'LineWidth',3) %fill black (to mark cell as live)
    [x,y] = ginput(1); %Get new mouse coordinates
end

[R,C] = coordGen(startCells);
%Cells=startCells;
%Remove earlier prompt.
title('')

end