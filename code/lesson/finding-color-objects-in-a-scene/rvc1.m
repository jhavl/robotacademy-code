%% 0:21
im = iread('tomato_124.jpg', 'double');

%% 0:25
idisp(im)

%% 1:56
im = iread('tomato_124.jpg', 'double', 'gamma', 2.2);

%% 2:01
idisp(im)

%% 2:35
idisp(im(:, :, 1))

%% 2:44
idisp(im(:, :, 2))

%% 2:58
R = im(:, :, 1);

%% 3:02
G = im(:, :, 2);

%% 3:08
B = im(:, :, 3);

%% 3:13
idisp(G)

%% 3:27
Y = R + G + B;

%% 3:36
idisp(Y)

%% 3:58
r = R ./ Y;

%% 4:20
g = G ./ Y;

%% 4:30
idisp(r)

%% 4:35
figure(2)

%% 4:38
idisp(g)

%% 6:03
tom = (r > 0.8) & (g < 0.2);

%% 6:07
idisp(tom)

%% 6:46
b = iblobs(tom)

%% 7:05
figure(1)

%% 7:07
idisp(im)

%% 7:16
b.plot_box('g')