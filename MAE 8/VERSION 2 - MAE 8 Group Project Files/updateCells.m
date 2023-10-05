function updateCells(cells,m,n)

clf
drawCells(m,n);
for i = 1:m
    for j = 1:n
        if cells(i,j) ==1
            rectangle('Position',[j-1,i-1,1,1],'FaceColor','k','EdgeColor',0.8*[1 1 1],'LineWidth',3)
        end
    end
end

end