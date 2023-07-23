%% 2:22
im = imread('building2-1.png');
im = im2gray(im);

%% 2:25
imshow(im)

%% 2:47
C = detectSIFTFeatures(im);

%% 2:57
C(1)

%% 3:37
C(1).Scale = 16
imshow(im);
hold on;
plot(C(1))

%% 4:14
C = detectSIFTFeatures(im);
C.Scale = C.Scale*4
imshow(im);
hold on;
plot(C.selectStrongest(200))

%% 6:10
C = detectSIFTFeatures(im);
d = C(1)