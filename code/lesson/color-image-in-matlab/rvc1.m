%% 0:19
im = iread('flowers8.png');

%% 0:52
idisp(im)

%% 2:10
idisp( im(:,:,1) )

%% 2:37
idisp( im(:,:,2) )

%% 2:59
idisp( im(:,:,3) )

%% 5:39
im = iread('flowers8.png');

idisp(im)

%% 5:52
im(100,100,:)

%% 6:11
squeeze( im(100,100,:) )