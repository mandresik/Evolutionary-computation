%% plot setup
border = 100;
border_s = 10;
step = 0.1;
step_s = 0.05;
[x, y] = meshgrid(-border : step : border);
[xs, ys] = meshgrid(0 : step_s : 5);
u = -border : step : border;
us = -0 : step_s : 5;
%% function values
% F1(u)
m = 10;
F1 = -(sin(u).*(sin(1/pi .* u.^2)).^(2*m));
% f1(us)
f1 = -(sin(us).*(sin(1/pi .* us.^2)).^(2*m));
% F2(x,y)
F2 = -(sin(x).*(sin(1/pi .* x.^2)).^(2*m) + sin(y).*(sin(1/pi .* 2*(y.^2))).^(2*m));
% f2(xs,ys)
f2 = -(sin(xs).*(sin(1/pi .* xs.^2)).^(2*m) + sin(ys).*(sin(1/pi .* 2*(ys.^2))).^(2*m));
%% figure with 1 variable
figure(1); 
sgtitle("Michalewitzova funkce (m=10)")
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
sgtitle("Michalewitzova funkce (m=10)")
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