%% plot setup
border = 100;
border_s = 10;
step = 0.1;
step_s = 0.1;
[x, y] = meshgrid(-border : step : border);
[xs, ys] = meshgrid(-border_s : step_s : border_s);
u = -border : step : border;
us = -border_s : step_s : border_s;
%% function values
% F1(u)
F1 = 1 - cos(2*pi*abs(u)) + .1*abs(u);
% f1(us)
f1 = 1 - cos(2*pi*abs(us)) + .1*abs(us);
% F2(x,y)
n = sqrt(x.^2 + y.^2);
F2 = 1 - cos(2*pi*n) + .1*n;
% f2(xs,ys)
ns = sqrt(xs.^2 + ys.^2);
f2 = 1 - cos(2*pi*ns) + .1*ns;
%% figure with 1 variable
figure(1); 
sgtitle("Salomonova funkce")
% subplot 1 on [-border_s, border_s]
subplot(1,2,1);
plot(us, f1);
xlabel('x');
ylabel('f(x)');
title('f (x)');
% subplot 2 on [-border, border]
subplot(1,2,2);
plot(u, F1);
xlabel('x');
ylabel('f(x)');
title('f (x)');
set(gcf, 'Position', [0,0,1000,400]);
%% figure with 2 variables
% subplot 1 on [-border_s, border_s]
figure(2);
sgtitle("Salomonova funkce")
subplot(1,2,1);
mesh(xs, ys, f2);
xlabel('x');
ylabel('y');
zlabel('f(x,y)');
title('f (x, y)');
% subplot 2 on [-border, border]
subplot(1,2,2);
mesh(x, y, F2);
xlabel('x');
ylabel('y');
zlabel('f(x,y)');
title('f (x, y)');
set(gcf, 'Position', [0,0,1000,400]);