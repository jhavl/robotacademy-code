%% 5:16
im = iread('shark2.png');

idisp(im)

%% 5:38
[L, nb] = ilabel(im);

%% 5:43
nb

%% 5:56
figure(2)

%% 6:00
idisp(L)

%% 6:50
idisp(L == 1)

%% 7:00
idisp(L == 2)

%% 7:42
b = iblobs(im)

%% 8:36
idisp(im)

%% 8:44
b(1).plot_box('g')

%% 8:50
b(2).plot_box('g')

%% 9:07
b(1).plot('b*')

%% 9:13
b(1).area

%% 9:19
b(1).class

%% 9:28
b(1).p

%% 9:34
b(1).uc

%% 9:41
b(1).moments.m01