x = 1; 
y = 1.3; 
L1 = 1; 
L2 = 2; 

L3 = sqrt(1.5^2 + 1.3^2); 

alp2 = acos((L3^2 - L1^2 - L2^2) / (2*L1*L2));
phi = pi-alp2

alp1 = acos((L2^2 - L1^2 -L3^2) / (2*L1*L3));
theta = pi-alp1

