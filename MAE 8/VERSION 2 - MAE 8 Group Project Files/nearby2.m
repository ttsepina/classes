function [A,B,G,H] = nearby2(I)
A = []; % y-coordinates for nearby living cells
B = []; % x-coordinates for nearby living cells
G = []; % y-coordinates of nearby dead cells
H = []; % x-coordinates of nearby dead cells



    for i = 1:(size(I,2)) % for the number of columns
        for j = 1:(size(I,1)) %for the number of rows
            if i == 1
                cMin = 0;
            else
                cMin = -1;
            end
            if j == 1
                rMin = 0;
            else
                rMin = -1;
            end
            if i == size(I,2)
                cMax = 0;
            else
                cMax = 1;
            end
            if j == size(I,1)
                rMax = 0;
            else
                rMax = 1;
            end
            %These are dynamic scanning bounds for when the scan area
            %approaches edges
            
            if I(j,i) == 1      %checking for living cell
                for r = rMin:rMax    %for rows above and below the cell
                    for c = cMin:cMax %for columns to the left and right of the cell
                        
                        if i+c == i && j+r == j
                            
%                             i;
%                             c;
%                             j;
%                             r;
                            
                        else
                            if I(j+r, i+c) == 1
                        A = [A, j+r];
                        B = [B, i+c];

                            else
                                if I(j+r, i+c) == 0
                                    G = [G,j+r];
                                    H = [H, i+c];
                                end
                            end
                        end
                    end
                end
            end
            
            
        end
    end
  
end