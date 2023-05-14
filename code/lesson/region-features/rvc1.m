%% 4:03
im = iread('shark2a.png');

%% 4:07
idisp(im)

%% 4:21
b = iblobs(im)

%% 4:48
b = iblobs(im, 'class', 1)

%% 6:32
b.plot_ellipse('g')

%% 6:42
b.plot('b*')