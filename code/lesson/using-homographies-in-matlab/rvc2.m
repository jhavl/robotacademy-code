%% 0:00
P = mkgrid(2, 0.2, 'T', transl(1, 2, 0))

cam = CentralCamera('default', 'pose', transl(0, 0, 4)*trotz(pi/3)*troty(pi))

cam.project(P)

%% 0:19
p = cam.project(P)

%% 0:26
P

%% 0:41
Q = P(1:2,:)

%% 1:07
H = homography(p, Q)

%% 1:31
homtrans(H, p)

%% 1:52
homtrans(inv(H), Q)