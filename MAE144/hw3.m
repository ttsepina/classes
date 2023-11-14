%%Problem 1

clear all,clc;

disp('Problem 1');

pause

b0 = 0.1;
a0 = 0.1;
d = 6;

G = tf([b0],[1 a0]) %%The transfer function of the system with zero initial conditions and no delay

bode(G);

pause

Gd = tf([b0],[1 a0],'InputDelay', d) %% Transfer function of the system with the 6 second transport delay

bode(Gd);

pause

clc

disp('Problem 2');

a = 0.6;
b = inf;
g = 0;

disp('For a given Ku that makes the system unstable, the proportional control Kp established is the fraction of Ku expressed by alpha (a = 0.6). The gain margin is therefore the ratio of the max gain before instability Ku over the current gain Kp, which becomes 1/a = 1/0.6 = 1.666667 = GM.')

pause

clc

disp('Problem 3');

disp(' By dialing beta down from infinity and gamma up from 0, the control law goes from proportional control to PID control since the repsective terms in the controller no longer return 0 when calculated.')

pause

clc

disp('Problem 4')

a = 0.6;
b = 0.5;
g = 0.125;
Ku = 3.2;
wu = 0.3;
Tu = 1/wu;

Kp = a*Ku;
Ti = b*Tu;
Td = g*Tu;

D = tf(Kp*Td*[1 1/Td 1/(Td*Ti)],[1 0],);

pause

bode(D*Gd);

disp('');

pause

Kp
wi = 1/Ti
wd = 1/Td

pause

