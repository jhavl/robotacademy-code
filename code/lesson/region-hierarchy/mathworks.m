%% 1:46
im = imread('multiblobs.png');

%% 1:51
imshow(im)

%% 2:01 - 2:13
% Mathworks image processing and computer vision toolbox does not have the
% same functionality for image labeling

%% 2:39
Hblob = vision.BlobAnalysis
[area,centroid,bbox] = Hblob(im)