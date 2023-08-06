%% 3:36
im = iread('monalisa.png', 'grey', 'double');

%% 4:36
s7 = iconv(im, ones(7, 7));

%% 4:42
idisp(im)

%% 4:44
figure(2)

%% 4:47
idisp(s7)

%% 5:16
s21 = iconv(im, ones(21, 21));

%% 5:22
idisp(s21)