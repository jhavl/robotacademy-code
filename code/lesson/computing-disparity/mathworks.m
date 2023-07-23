%% 2:16
L = imread('rocks2-l.png');

%% 2:23
R = imread('rocks2-r.png');

%% 2:46
imshow(imfuse(L, R));

%% 3:05
imshowpair(L, R,'montage')

%% 5:00
L = rgb2gray(L);
R = rgb2gray(R);
J = disparityBM(L,T,'DisparityRange',[40 90],'UniquenessThreshold',3);

%% 5:04
imshow(J)