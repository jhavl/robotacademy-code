%% 0:40
mdl_twolink

syms q1 q2 q1d q2d q1dd q2dd

%% 1:00
twolink.gravload([q1 q2])

%% 3:04
mdl_twolink

%% 3:18
twolink.gravload([0 0])

%% 3:38
twolink.plot([0 0])

%% 3:49
twolink.plot([pi/2 0])

%% 4:06
twolink.gravload([pi/2 0])

%% 4:57
twolink.payload(1, [0 0 0])

%% 5:14
twolink.gravload([0 0])

%% 5:22
twolink.plot([0 0])

%% 5:40
mdl_puma560

%% 5:57
p560.gravload([0 0 0 0 0 0])

%% 6:08
p560.plot([0 0 0 0 0 0])

%% 6:37
p560.gravity = [0 0 9.81/6];

%% 6:50
p560.gravload([0 0 0 0 0 0])