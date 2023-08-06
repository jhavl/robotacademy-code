%% 0:13
nm = 1e-9;

%% 0:34
lambda = [350:5:800]*nm;

%% 0:54
E = loadspectrum(lambda, 'solar.dat');

%% 1:07
plot(lambda, E)

%% 1:30
R = loadspectrum(lambda, 'redbrick.dat');

%% 1:34
figure(2)

%% 1:41
plot(lambda, R)

%% 2:13
L = E.*R;

%% 2:23
plot(lambda, L)

%% 2:52
cones = loadspectrum(lambda, 'cones.dat');

%% 3:11
plot(lambda, cones)

%% 3:41
plot(lambda, L.*cones(:,1))

%% 4:06
plot(lambda, L.*cones(:,2))

%% 4:24
plot(lambda, L.*cones(:,3))

%% 5:04
sum( L.*cones(:,1)*5*nm)

%% 5:09
sum( L.*cones(:,2)*5*nm)

%% 5:15
sum( L.*cones(:,3)*5*nm)