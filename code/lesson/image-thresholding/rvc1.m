%% 2:06
2>1

%% 2:41
1>2

%% 2:52
true

%% 2:57
false

%% 3:05
1==2

%% 3:11
2==2

%% 3:20
a = 2==3

%% 4:13
m = randi(10, 4)

%% 4:19
m > 5

%% 5:03
m == 3

%% 5:12
im = iread('penguins.png', 'grey', 'double');

idisp(im)

figure

ihist(im)

%% 5:34
b = im > 0.45;

%% 5:55
idisp(b)

%% 6:55
b = im > 0.6;

%% 7:01
idisp(b)

%% 7:21
ithresh(im)