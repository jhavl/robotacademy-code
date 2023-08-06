%% 2:32
cam = CentralCamera('default')

%% 3:03
J = cam.visjac_p([600 600]', 5)

%% 3:19
J*[1 0 0 0 0 0]'

%% 3:38
J*[0 1 0 0 0 0]'

%% 3:53
J*[0 0 1 0 0 0]'