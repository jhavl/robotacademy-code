%% 1:47
cam = CentralCamera('default')

%% 1:59
P = [1 1 5]'

%% 2:09
p0 = cam.project(P)

%% 2:52
px = cam.project(P, 'Tcam', transl(0.1, 0, 0))

%% 3:18
(px-p0)/0.1

%% 3:47
(cam.project(P, 'Tcam', transl(0, 0, 0.1))-p0)/0.1

%% 4:08
(cam.project(P, 'Tcam', trotx(0.1))-p0)/0.1

%% 4:47
cam.flowfield([1 0 0 0 0 0])

%% 5:02
cam.flowfield([0 1 0 0 0 0])

%% 5:22
cam.flowfield([0 0 1 0 0 0])

%% 5:38
cam.flowfield([0 0 0 0 0 1])
