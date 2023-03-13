clear; 
theta  = importdata('MotorAt50.csv'); 
V = 50; 
A = 0.0046;
B = 0.098;
syms s 
sys = tf(1,[A B 0]);
Kp = 1.019;


tfin = length(theta)*0.005;

t = 0:0.005:tfin;
theta = [0 theta];

smt = 0.5*(V/A)*t(1:10).^2;
bgt = (V/B)*t - 20;
Y = step(Kp*50*sys,t);

mean(abs(Y'-theta)) % error between sim. and data

hold on 
plot(t,Y,'k','DisplayName','Simulated Data')
plot(t,theta,'r','DisplayName','Measured Data')
xlabel('Time (s)')
ylabel('Angular Displacement (degrees)')
legend
title(['Comparing simulated to measured data for Kp = ' num2str(Kp)])
hold off 
