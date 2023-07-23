%% 0:00
im1 = imread('building2-1.png');
im2 = imread('building2-2.png');

%% 0:15
imshowpair(im1, im2,'montage')

%% 0:48
f1 = detectSURFFeatures(im1);

%% 1:45
imshow(im1); hold on;
plot(f1.selectStrongest(200));

%% 2:11
f2 = detectSURFFeatures(im2);

%% 2:49
[features1,valid_points1] = extractFeatures(im1,f1);
[features2,valid_points2] = extractFeatures(im2,f2);
m = matchFeatures(features1,features2);

%% 2:53
m

%% 3:50
imshowpair(im1, im2,'montage')

%% 4:14
matchedPoints1 = valid_points1(m(:,1),:);
matchedPoints2 = valid_points2(m(:,2),:);
showMatchedFeatures(im1,im2,matchedPoints1,matchedPoints2);