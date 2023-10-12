%% Problem 2
clear all, clc
disp('Problem 2: Part a')


b=RR_poly([2 -2 5 -5],1), a=RR_poly([1 -1 3 -3 6 -6],1)                     % The polynomials that make the rational function of plant

f=RR_poly([-1 -1 -3 -3 -6 -6],1)                                            % The desired denominator of the closed-loop transfer function

[x,y] = RR_diophantine(a,b,f), test=trim(a*x+b*y), residual1=norm(f-test)   % Solving the Diophantine equation aX+bY = f for the components of the controller D and testing for verification



pause

clear all, clc, disp('Problem 2: Part b') 

% Part b

% The controller D(s) is not proper as the order of the numerator is greater than that of the denominator (5>3).


b=RR_poly([2 -2 5 -5],1), a=RR_poly([1 -1 3 -3 6 -6],1)


f=RR_poly([-1 -1 -3 -3 -6 -6 -20 -20 -20 -20 ],1)                               % Try k = 5 additional poles for f

[x,y] = RR_diophantine(a,b,f), test=trim(a*x+b*y), residual1=norm(f-test)       % Degree of both x and y is 5, meaning the controller is now proper

% I suspect that having k = 5 allows for higher degrees of x (in order to satisy the Diophantine equation, if the degree of y does not increase due to minimization, then the degree of x must increase to maintain the new degree of f)
% However, it would seem that the degree of x only rises to 5 when k = 5 and not any less; both f and x only increase their degree by 2 to become degree 11 and 5 resepctively, which does not strictly reflect the fact that k = 5

pause

%% Problem 3

clear all, clc
disp('Problem 3')

function [Dz] = TTT_C2D_matched(Ds,h)

m = Ds.num.n
n = Ds.den.n
z = Ds.z
p = Ds.p

t = RR_tf([1],[1])

if m == 0
dz = RR_poly(1)

else 

for i = 1:m
    dz(i+1) = exp(z(i)*h) ;
end
end

for i = 1:n
    dp(i) = exp(p(i)*h);
end

if n>m
for i = 1:(n-m)
t = t* RR_tf([1 1],[1]);
end
end

% while length(dz) < length(dp)-1
% t = t* RR_tf([1 1],[1])
% end

Dz = t* RR_tf(dz,dp,1)
Dz.h = h

k = RR_evaluate(Ds,0)/RR_evaluate(Dz,1)

Dz = k*Dz

end