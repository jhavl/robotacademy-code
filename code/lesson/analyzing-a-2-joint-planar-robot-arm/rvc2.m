%% 3:08
a1 = 1

a2 = 1

q1 = 0.2

q2 = 0.3

%% 3:53
trchain2('R(q1) Tx(a1) R(q2) Tx(a2)', [q1 q2])

%% 4:21
syms q1 q2 a1 a2

%% 4:30
trchain2('R(q1) Tx(a1) R(q2) Tx(a2)', [q1 q2])

%% 4:50
mdl_planar2

%% 5:00
p2.teach

%% 5:35
p2.plot([0 pi/2])

%% 5:49
p2.plot([pi/2 -pi/2])