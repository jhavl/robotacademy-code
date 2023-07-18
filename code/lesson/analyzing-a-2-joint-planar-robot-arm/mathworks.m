%% 3:08
a1 = 1

a2 = 1

q1 = 0.2

q2 = 0.3

%% 3:53
se2(so2(q1, "theta")) .* se2(so2(0, "theta"), [a1, 0]) .*se2(so2(q2, "theta")) .* se2(so2(0, "theta"), [a2, 0])
