%% 6:23
cam = CentralCamera('default')

d = 0.5; z = 1;
P = [-d -sqrt(3)/2*d z; d -sqrt(3)/2*d z; 0 sqrt(3)/2*d z]'

Tcam = transl(3.5, 3.5, -5)*trotx(0.1)*troty(-0.1)*trotz(0.2)

%% 7:14
p = cam.plot(P, 'Tcam', Tcam)

%% 8:07
J = cam.visjac_p(p, 5)

%% 8:19
inv(J)