%% 2:22
im = iread('building2-1.png', 'grey');

%% 2:25
idisp(im)

%% 2:47
C = isift(im, 'nfeat', 200);

%% 2:57
C(1)

%% 3:37
C(1).plot('y', 'scale', 16, 'clock')

%% 4:04
idisp(im, 'dark')

%% 4:14
C.plot('w', 'scale', 4, 'clock')

%% 6:10
d = C(1).descriptor;
