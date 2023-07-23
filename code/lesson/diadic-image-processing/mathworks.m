%% 5:24
cam = VideoReader('traffic_sequence.mp4');

%% 5:44
im1 = readFrame(cam);
im1 = double(rgb2gray(im1))/255;

%% 5:53
im2 = readFrame(cam);
im2 = double(rgb2gray(im2))/255;

%% 6:02
imshow(im1-im2)

%% 6:30
imshow((im1-im2)+0.5);
mymap = [1 0 0; 0 0 0; 0 0 1];
colormap(mymap)