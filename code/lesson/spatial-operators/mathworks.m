%% 3:36
im = im2double(im2gray(imread('monalisa.png')));

%% 4:36
s7 = conv2(im,ones(7, 7));
s7 = s7/max(max(s7)); % fix the scale

%% 4:42
imshow(im)

%% 4:44
figure(2)

%% 4:47
imshow(s7)

%% 5:16
s21 = conv2(im, ones(21, 21));
s21 = s21/max(max(s21)); % fix the scale

%% 5:22
imshow(s21)