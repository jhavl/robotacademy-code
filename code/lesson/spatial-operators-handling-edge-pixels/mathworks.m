%% 1:37
im = im2double(im2gray(imread('monalisa.png')));

s7 = conv2(im,ones(7, 7));
s7 = s7/max(max(s7)); % fix the scale

imshow(im)

figure(2)

imshow(s7)

s21 = conv2(im, ones(21, 21));
s21 = s21/max(max(s21)); % fix the scale

imshow(s21)