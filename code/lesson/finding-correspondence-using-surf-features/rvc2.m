% Currently the function colorkmeans and match are producing errors, due to
% this those sections of the code and parts requiring the outputs will not
% work correctly.

%% 0:00
im1 = iread('building2-1.png');
im2 = iread('building2-2.png');

%% 0:15
idisp({im1 im2})

%% 0:48
f1 = isurf(im1);

%% 1:45
f1(1:200).plot('wd')

%% 2:11
f2 = isurf(im2);

%% 2:49
m = f1.match(f2);

%% 2:53
m

%% 3:13
m.p

%% 3:50
idisp({im1 im2})

%% 4:14
m.subset(100).plot('w')