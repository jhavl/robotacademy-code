%% 0:21
im = im2double(imread('tomato_124.jpg'));

%% 0:25
imshow(im)

%% 1:56
im = imadjust(im2double(imread('tomato_124.jpg')),[],[],2.2);

%% 2:01
imshow(im)

%% 2:35
imshow(im(:, :, 1))

%% 2:44
imshow(im(:, :, 2))

%% 2:58
R = im(:, :, 1);

%% 3:02
G = im(:, :, 2);

%% 3:08
B = im(:, :, 3);

%% 3:13
imshow(G)

%% 3:27
Y = R + G + B;

%% 3:36
imshow(Y)

%% 3:58
r = R ./ Y;

%% 4:20
g = G ./ Y;

%% 4:30
imshow(r)

%% 4:35
figure(2)

%% 4:38
imshow(g)

%% 6:03
tom = (r > 0.8) & (g < 0.2);

%% 6:07
imshow(tom)

%% 6:46
Hblob = vision.BlobAnalysis
[area,centroid,bbox] = Hblob(tom)

%% 7:05
figure(1)

%% 7:07
imshow(im)

%% 7:16
for I = 1:size(area)
    drawrectangle('Position',[bbox(I,1),bbox(I,2),bbox(I,3),bbox(I,4)],'Color','g')
end