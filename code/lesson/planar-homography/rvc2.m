%% 3:31
H = homography(P, Q)

%% 3:40
homwarp(H, im, 'full')

%% 8:09
H = homography(P, Q)

Q = homtrans(H, P)