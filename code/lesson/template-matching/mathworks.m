%% 3:32
crowd = im2double(im2gray(imread('wheres_walle.png')));

%% 3:36
imshow(crowd)

%% 3:53
bender = im2double(im2gray(imread('bender.png')));

%% 4:03
figure(2)

%% 4:09
imshow(bender)

%% 5:03
tMatcher = vision.TemplateMatcher
S = tMatcher(crowd, bender);

%% 5:12
% S returns as coordinates for the matched template and not an image

%% 6:48
% Mathworks computer vision and image processing toolbox does not have
% functionality for this kind of peak finding and display 

%% 9:35
imshow(crowd)
drawcircle('Center',S,'Radius',20,'StripeColor','red');