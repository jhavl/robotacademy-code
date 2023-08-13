%% 0:32
im = rgb2gray(imread('monalisa.png'));

%% 0:39
about im

%% 0:57
imshow(im)

%% 1:43
im(194, 276)

%% 2:17
im(180:210, 260:290)

%% 2:36
im2 = im(180:210, 260:290)

%% 2:44
figure

%% 2:48
imshow(im2)

%% 3:19
lin = im(190, 260:290)

%% 3:30
plot(lin)

%% 4:21
im3 = im(1:4:end, 1:4:end);

%% 4:24
imshow(im3)

%% 5:19
im4 = im(end:-1:1, 1:end);

%% 5:23
imshow(im4)

%% 5:59
im4 = im(end:-1:1, :);