%% 3:42
im = imread('tomato_124.jpg');

%% 3:45
imshow(im)

%% 4:39
[L,centers] = imsegkmeans(im,4);

%% 4:59
figure

%% 5:04
[L,Centers] = imsegkmeans(im,3);
B = labeloverlay(im,L);
imshow(B)

%% 6:00
tom = L == 3;

%% 6:02
idisp(tom)

%% 7:39 - 9:17
% Mathworks image processing and computer vision toolbox does not have
% equivalent functionality for iclose function
