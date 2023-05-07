%% 1:46
im = iread('multiblobs.png');

%% 1:51
idisp(im)

%% 2:01
[L, nb] = ilabel(im);

%% 2:03
nb

%% 2:11
figure(2)

%% 2:13
idisp(L)

%% 2:39
b = iblobs(im)
