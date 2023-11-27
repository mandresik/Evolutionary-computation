%% plot setup
border = 100;
border_s = 2;
step = 0.1;
step_s = 0.1;
[x, y] = meshgrid(-border : step : border);
[xs, ys] = meshgrid(-border_s : step_s : border_s);
u = -border : step : border;
us = -border_s : step_s : border_s;
%% function values
% F1(u)
 % not defined
% f1(us)
 % not defined
% F2(x,y)
F2 = .5 + ((sin(sqrt(100*x.^2+y.^2))).^2  -.5) ./ (1 + .001 * (x.^2 - 2*x.*y + y.^2).^2);
% f2(xs,ys)
f2 = .5 + ((sin(sqrt(100*xs.^2+ys.^2))).^2  -.5) ./ (1 + .001 * (xs.^2 - 2*xs.*ys + ys.^2).^2);
%% figure with 1 variable
% figure(1); 
% sgtitle("TITLE")
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
sgtitle("Patologická funkce")
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