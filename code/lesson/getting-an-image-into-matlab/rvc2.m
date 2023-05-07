%% 0:37
im = iread('P1030150.JPG');

%% 0:47
idisp(im)

%% 1:19
[im, meta] = iread('P1030150.JPG');

%% 1:22
meta

%% 1:38
meta.DigitalCamera

%% 2:26
im = iread('street.png');

%% 4:07
idisp(im)

%% 6:07
im(653,562)