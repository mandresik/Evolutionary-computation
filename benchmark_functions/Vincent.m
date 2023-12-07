%% plot setup
border = 100;
border_s = 5;
step = 0.1;
step_s = 0.01;
[x, y] = meshgrid(-border : step : border);
[xs, ys] = meshgrid(-100 : step_s : -90);
u = -border : step : border;
us = -100 : step_s : -90;
%% function values
% F1(u)
F1 = -sin(10*log(u+101));
% f1(us)
f1 = -sin(10*log(us+101));
% F2(x,y)
F2 = -(sin(10*log10(x+101)) + sin(10*log10(y+101)));
% f2(xs,ys)
f2 = -(sin(10*log10(xs+101)) + sin(10*log10(ys+101)));
%% figure with 1 variable
figure(1); 
sgtitle("Vincentova funkce")
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
sgtitle("Vincentova funkce")
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