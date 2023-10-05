function D = livescore(m,n,A,B) 
livescore = zeros(m,n);
for i = 1:length(A)
    livescore(A(i),B(i)) = livescore(A(i),B(i)) + 1;
end
D = livescore;
end
