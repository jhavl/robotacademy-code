%% 0:36
im = zeros(200, 200);

%% 0:47
im(1, 1) = 1;

%% 0:51
imshow(im)

%% 1:40
im(150:160, 60:70) = 0.5;

%% 1:43
imshow(im)

%% 2:04 -%% 5:30
% Mathworks image processing and computer vision toolbox does not support
% this kind of circle drawing, line drawing, pasting of images, and
% producing test patters