%% 7:54
K = kgauss(5, 15);

%% 8:05
idisp(K)

%% 8:21
figure

%% 8:27
surfl(K)

%% 8:56
im = iread('monalisa.png', 'grey', 'double');

%% 9:04
s = iconv(K, im);

%% 9:09
idisp(s)