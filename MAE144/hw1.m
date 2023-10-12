%% Problem 2

% Part a

G = RR_tf([1 0 -29 0 100],[1 0 -46 0 369 0 -324]);                          % The expanded form of the given transfer function

b=RR_poly([1 0 -29 0 100]), a=RR_poly([1 0 -46 0 369 0 -324])               % The polynomials that make the rational function of plant

f=RR_poly([1 20 154 576 1089 972 324])                                      % The desired denominator of the closed-loop transfer function, expanded based on the desired pole locations

[x,y] = RR_diophantine(a,b,f), test=trim(a*x+b*y), residual1=norm(f-test)   % Solving the Diophantine equation aX+bY = f for the components of the controller D and testing for verification

% Note that the transfer function and polynomials are defined using coefficient vectors and not a pole/zero/gain format.

% Part b

