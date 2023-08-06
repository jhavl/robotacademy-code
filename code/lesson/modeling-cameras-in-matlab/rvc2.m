%% 0:31
P = [0.2 0.3 5]'

%% 0:47
cam = CentralCamera('focal', 0.008)

%% 1:06
cam.project(P)

%% 2:06
cam = CentralCamera('focal', 0.008, 'pixel', 10e-6, 'resolution', 1024)

%% 2:38
cam.project(P)

%% 2:48
cam.plot(P)

%% 3:01
cam.K

%% 3:06
cam.C

%% 3:32
cam.project(P, 'Tcam', transl(0.1, 0, 0))

%% 4:12
cam.project(P, 'Tcam', troty(0.1))

%% 5:00
P = mkgrid(2, 0.2, 'T', transl(1, 2, 0))

%% 6:04
cam = CentralCamera('default', 'pose', transl(0, 0, 4)*trotz(pi/3)*troty(pi))

%% 6:13
cam.project(P)

%% 6:24
cam.plot(P)

%% 6:38
figure(2)

%% 6:47
cam.plot_camera

%% 7:02
plot_sphere(P, 0.05)