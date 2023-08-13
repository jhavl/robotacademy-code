%% 4:03
im = imread('shark2a.png');

%% 4:07
imshow(im)

%% 4:21
Hblob = vision.BlobAnalysis
[area,centroid,bbox] = Hblob(im)

%% 4:48
% Mathworks image processing and computer vision toolbox blob detection
% does not detect the background, no need to filter for it

%% 6:32
drawellipse('Center',[centroid(1,1),centroid(1,2)],'SemiAxes',[bbox(1,3)/2,bbox(1,4)/2],'StripeColor','g');
drawellipse('Center',[centroid(2,1),centroid(2,2)],'SemiAxes',[bbox(2,3)/2,bbox(2,4)/2],'StripeColor','g');

%% 6:42
drawpoint('Position',[centroid(1,1),centroid(1,2)])
drawpoint('Position',[centroid(2,1),centroid(2,2)])