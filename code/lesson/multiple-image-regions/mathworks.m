%% 5:16 - 7:00
% Mathworks image processing and computer vision toolbox does not have the
% same functionality for image labeling

%% 7:42
im = imread('shark2.png');

Hblob = vision.BlobAnalysis
[area,centroid,bbox] = Hblob(im)

%% 8:36
imshow(im)

%% 8:44
drawrectangle('Position',[bbox(1,1),bbox(1,2),bbox(1,3),bbox(1,4)],'Color','g')

%% 8:50
drawrectangle('Position',[bbox(2,1),bbox(2,2),bbox(2,3),bbox(2,4)],'Color','g')

%% 9:07
drawpoint('Position',[centroid(1,1),centroid(1,2)])

%% 9:13
area(1)

%% 9:19 - 9:41
% Mathworks image processing and computer vision toolbox does not have the
% same functionality for blob detection features
