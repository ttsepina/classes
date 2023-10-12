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


f=RR_poly([-1 -1 -3 -3 -6 -6 -20 -20 -20 -20 -20 ],1)                               % Try k = 5 additional poles for f

[x,y] = RR_diophantine(a,b,f), test=trim(a*x+b*y), residual1=norm(f-test)       % Degree of both x and y is 5, meaning the controller is now proper

% I suspect that having k = 5 allows for higher degrees of x (in order to satisy the Diophantine equation, if the degree of y does not increase due to minimization, then the degree of x must increase to maintain the new degree of f)
% However, it would seem that the degree of x only rises to 5 when k = 5 and not any less; both f and x only increase their degree by 2 to become degree 11 and 5 resepctively, which does not strictly reflect the fact that k = 5

pause

%% Problem 3

clear all, clc
disp('Problem 3')

function [Dz] = TTT_C2D_matched(Ds,h,causality,omega_bar)

arguments
    Ds (1,1) RR_tf
    h (1,1)
    causality (1,1) string = 'semi'
    omega_bar (1,1) double = 0

end

m = Ds.num.n;            % initialize degree of polynomials that compose D(s) and its poles and roots
n = Ds.den.n;
z = Ds.z;
p = Ds.p;
r = [];
t = RR_tf([1],[1]);      % create empty transfer function to modify
o = RR_tf([1],[1]);

for i = 1:n
    if p(i) == 0
        r(i) = p(i);
    end
end

    if isempty(r) ~= 1
        if omega_bar == 0
            error('omega_bar must be nonzero when there are poles at the origin')
        end
    else
        for i = 1:length(r)
            o = o*RR_tf([1],[1 -1]);
        end
    end



if m == 0               % check if numerator has no finite zeros
dz = [];

else 

for i = 1:m
    dz(i) = exp(z(i)*h);      %calculate zeros and poles based on z = exp(s*h)
end
end

for i = 1:n
    dp(i) = exp(p(i)*h);
end

switch causality

    case 'strict'

        if n-m > 1                          %Strictly causal case where n>m in D(z)
            for i = 1:(n-m)-1           %Adds infinite zeros to empty tf based on # of poles and zeros
            t = t* RR_tf([1 1],[1]);
            end
            t = t*RR_tf([1],[1 0]);
        else if n-m == 1
            t = t*RR_tf([1],[1 0]);
            end
        end

    case 'semi'

        if n>m                          %Semi-causal case where n>m in D(z)
            for i = 1:(n-m)             %Adds infinite zeros to empty tf based on # of poles and zeros
            t = t* RR_tf([1 1],[1]);
            end
        
        end
        

    otherwise
        error('Causality must either be ''strict'' or ''semi''')
end

Dz = t*RR_tf(dz,dp,1)                                      %Define D(z) using poles and zeros calculated and with infinite zeros
Dz.h = h                                                   %Define D(z) as DTTF by initializing time step h

ks = RR_evaluate(Ds,omega_bar)
kz = RR_evaluate(Dz,1)

k = ks/kz            %Ensure matching gain between CT and DT by computing relative DC gains and dividing to find their ratio
                                                            %Allow input of omega_bar to get critical gain input (here is s = iw for w  = 0)
Dz = k*Dz*o                                                  %Implement gain correction

end