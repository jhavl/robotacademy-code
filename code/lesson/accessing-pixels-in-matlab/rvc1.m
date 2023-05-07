%% 0:32
im = iread('monalisa.png', 'grey');

%% 0:39
about im

%% 0:57
idisp(im)

%% 1:43
im(194, 276)

%% 2:17
im(180:210, 260:290)

%% 2:36
im2 = im(180:210, 260:290)

%% 2:44
figure

%% 2:48
idisp(im2)

%% 3:19
lin = im(190, 260:290)

%% 3:30
plot(lin)

%% 4:21
im3 = im(1:4:end, 1:4:end);

%% 4:24
idisp(im3)

%% 5:19
im4 = im(end:-1:1, 1:end);

%% 5:23
idisp(im4)

%% 5:54
im4 = im(end:-1:1, :);