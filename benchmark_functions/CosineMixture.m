%% plot setup
border = 100;
border_s = 1;
step = 0.1;
step_s = 0.025;
[x, y] = meshgrid(-border : step : border);
[xs, ys] = meshgrid(-border_s : step_s : border_s);
u = -border : step : border;
us = -border_s : step_s : border_s;
%% function values
% F1(u)
F1 = -.1*cos(5*pi*u) + u.^2;
% f1(us)
f1 = -.1*cos(5*pi*us) + us.^2;
% F2(x,y)
F2 = -.1*(cos(5*pi*x) + cos(5*pi*y))  +  (x.^2 + y.^2);
% f2(xs,ys)
f2 = -.1*(cos(5*pi*xs) + cos(5*pi*ys))  +  (xs.^2 + ys.^2);
%% figure with 1 variable
figure(1); 
sgtitle("CosineMixture funkce")
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
sgtitle("CosineMixture funkce")
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