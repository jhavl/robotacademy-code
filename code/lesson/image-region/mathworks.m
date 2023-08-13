%% 1:04
im = imread('shark1.png');

%% 1:09
imshow(im)

%% 2:06
[v, u] = find(im > 0);

%% 2:24
[u v]

%% 2:55
umin = min(u)

%% 3:03
umax = max(u)

%% 3:14
vmin = min(v)

%% 3:19
vmax = max(v)

%% 3:39
imshow(im)
h = drawrectangle('Position',[umin,vmin,umax-umin,vmax-vmin],'Color','r')

%% 4:08
uc = (umin+umax)/2

%% 4:16
vc = (vmin+vmax)/2

%% 4:32
imshow(im)
drawpoint('Position',[uc vc]);

%% 6:45
% Mathworks computer vision and image processing toolbox does not have
% functionality for this kind of image moment calculation