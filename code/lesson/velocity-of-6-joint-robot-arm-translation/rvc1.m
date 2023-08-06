%% 3:19
mdl_puma560

%% 3:41
p560.plot(qn)

%% 3:59
T = p560.fkine(qn)

%% 4:28
Td = p560.fkine(qn + [0.01 0 0 0 0 0])
