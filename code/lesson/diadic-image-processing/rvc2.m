%% 5:24
cam = Movie('traffic_sequence.mp4', 'double', 'grey');

%% 5:44
im1 = cam.grab();

%% 5:53
im2 = cam.grab();

%% 6:02
idisp(im1-im2)

%% 6:30
idisp(im1-im2, 'signed')