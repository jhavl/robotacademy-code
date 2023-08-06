%% 0:36
im = zeros(200, 200);

%% 0:47
im(1, 1) = 1;

%% 0:51
idisp(im)

%% 1:40
im(150:160, 60:70) = 0.5;

%% 1:43
idisp(im)

%% 2:04
circle = kcircle(30);

%% 2:10
idisp(circle)

%% 2:45
idisp(im)

%% 3:24
im = ipaste(im, circle*0.7, [100 30]);

%% 3:35
idisp(im)

%% 4:12
im = iline(im, [30 40], [150, 190], 0.9);

%% 4:18
idisp(im)

%% 4:43
im = testpattern('rampx', 200);

%% 4:46
idisp(im)

%% 5:28
im = testpattern('squares', 200, 50, 25);

%% 5:30
idisp(im)