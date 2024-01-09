%% 0:19
im = imread('flowers8.png');

%% 0:52
imshow(im)

%% 2:10
imshow( im(:,:,1) )

%% 2:37
imshow( im(:,:,2) )

%% 2:59
imshow( im(:,:,3) )

%% 5:39
im = imread('flowers8.png');

imshow(im)

%% 5:52
im(100,100,:)

%% 6:11
squeeze( im(100,100,:) )