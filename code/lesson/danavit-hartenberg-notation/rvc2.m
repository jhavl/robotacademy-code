%% 7:46
dh = [0 0 1 0
      0 0 1 0]

%% 8:27
r = SerialLink(dh)

%% 8:59
r.plot([0.2 0.3])

%% 9:05
r.teach

%% 9:30
r.fkine([0.2 0.3])

%% 10:41
mdl_puma560

%% 10:47
p560

%% 11:11
p560.plot(qz)

%% 11:21
p560.plot(qr)

%% 11:30
p560.teach

%% 12:12
p560.fkine([0.1 0.2 0.3 0 0 0])
