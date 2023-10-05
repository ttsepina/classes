function I = Igen(m,n,R,C)
I = zeros(m+1,n+1);
for i =1:length(R)
I(R(i)-1,C(i)-1) = 1;
end
I(:,n+1) = [];
I(m+1,:) = [];
end