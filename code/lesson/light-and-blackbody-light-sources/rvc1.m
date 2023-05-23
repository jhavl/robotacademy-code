%% 5:02
nm = 1e-9;

%% 5:25
lambda = [300:10:1000]*nm;

%% 5:41
E = blackbody(lambda, 6500);

%% 5:49
plot(lambda, E)

%% 5:56
grid

%% 6:09
E = blackbody(lambda, 6000);

%% 6:14
hold on

%% 6:23
plot(lambda, E, '--')