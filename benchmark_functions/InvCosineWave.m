%% plot setup
border = 100;
border_s = 5;
step = 0.1;
step_s = 0.1;
[x, y] = meshgrid(-border : step : border);
[xs, ys] = meshgrid(-border_s : step_s : border_s);
u = -border : step : border;
us = -border_s : step_s : border_s;
%% function values
% % F1(u)
% F1 = -20*exp(-.2*sqrt(u.*u)) - exp(cos(2*pi*u)) + 20 + exp(1);
% % f1(us)
% f1 = -20*exp(-.2*sqrt(us.*us)) - exp(cos(2*pi*us)) + 20 + exp(1);
% F2(x,y)
% F2(x,y)
F2 = -exp(-1/8*(x.^2 + y.^2 + 0.5*x.*y)) .* cos(4*sqrt(x.^2 + y.^2 + .5*x.*y));
% f2(xs,ys)
f2 = -exp(-1/8*(xs.^2 + ys.^2 + 0.5*xs.*ys)) .* cos(4*sqrt(xs.^2 + ys.^2 + .5*xs.*ys));
%% figure with 1 variable
% figure(1); 
% sgtitle("Inverted Cosine-Wave function")
% % subplot 1 on [-border_s, border_s]
% subplot(1,2,1);
% plot(us, f1);
% xlabel('x');
% ylabel('f(x)');
% title('f (x)');
% % subplot 2 on [-border, border]
% subplot(1,2,2);
% plot(u, F1);
% xlabel('x');
% ylabel('f(x)');
% title('f (x)');
% set(gcf, 'Position', [0,0,1000,400]);
%% figure with 2 variables
% subplot 1 on [-border_s, border_s]
figure(2);
sgtitle("InvertedCosineWave funkce")
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