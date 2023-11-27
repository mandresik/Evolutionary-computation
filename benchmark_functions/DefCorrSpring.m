%% plot setup
border = 100;
border_s = 10;
step = 0.1;
step_s = 0.1;
[x, y] = meshgrid(-border : step : border);
[xs, ys] = meshgrid(0 : step_s : border_s);
u = -border : step : border;
us = 0 : step_s : border_s;
%% function values
% F1(u)
a = 5;
K = 5;
F1 = .1*((u-a).^2 - cos(K*sqrt((u-a).^2)));
% f1(us)
f1 = .1*((us-a).^2 - cos(K*sqrt((us-a).^2)));
% F2(x,y)
F2 = .1*((x-a).^2 - cos(K*sqrt((x-a).^2 + (y-a).^2))  +  (y-a).^2 - cos(K*sqrt((x-a).^2 + (y-a).^2)));
% f2(xs,ys)
f2 = .1*((xs-a).^2 - cos(K*sqrt((xs-a).^2 + (ys-a).^2))  +  (ys-a).^2 - cos(K*sqrt((xs-a).^2 + (ys-a).^2)));
%% figure with 1 variable
figure(1); 
sgtitle("DeflectedCorrugatedSpring funkce")
% subplot 1 on [ 0 , border_s]
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
% subplot 1 on [ 0 , border_s]
figure(2);
sgtitle("DeflectedCorrugatedSpring funkce")
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