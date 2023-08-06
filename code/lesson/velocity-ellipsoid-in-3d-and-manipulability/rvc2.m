%% 1:11
mdl_puma560

J = p560.jacobe(qz)

%% 1:18
det(J)

%% 1:25
rank(J)

%% 1:40
J = p560.jacobe(qn)

%% 1:46
det(J)

%% 1:49
rank(J)

%% 4:42
mdl_puma560

%% 4:51
p560.plot(qn)

%% 5:23
p560.vellipse(qn, 'fillcolor', 'b', 'edgecolor', 'w', 'alpha', 0.5)

%% 6:02
p560.plot(qs)

%% 6:16
p560.vellipse(qs, 'fillcolor', 'b', 'edgecolor', 'w', 'alpha', 0.5)