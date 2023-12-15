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
wu = 1 + 1/4*(u - 1);
F1 = (sin(pi*wu)).^2 + ((wu - 1).^2) .* (1 + (sin(2*pi*wu).^2));
% f1(us)
wus = 1 + 1/4*(us - 1);
f1 = (sin(pi*wus)).^2 + ((wus - 1).^2) .* (1 + (sin(2*pi*wus).^2));
wx = 1 + 1/4*(x - 1);
wy = 1 + 1/4*(y - 1);
F2 = (sin(pi*wx)).^2 + ((wx - 1).^2) .* (1 + 10*(sin(pi*wx + 1)).^2) + ((wy - 1).^2) .* (1 + (sin(2*pi*wy).^2));
% f2(xs,ys)
wxs = 1 + 1/4*(xs - 1);
wys = 1 + 1/4*(ys - 1);
f2 = (sin(pi*wxs)).^2 + ((wxs - 1).^2) .* (1 + 10*(sin(pi*wxs + 1)).^2) + ((wys - 1).^2) .* (1 + (sin(2*pi*wys).^2));
%% figure with 1 variable
figure(1); 
sgtitle("Levyho funkce")
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
sgtitle("Levyho funkce")
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