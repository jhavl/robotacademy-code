%% 1:32 - 4:03

R = eul2r(0.1, 0.2, 0.3)

trplot(R)

eig(R)

[v,e] = eig(R)

tr2angvec(R)

[th,v] = tr2angvec(R)

angvec2r(th, v)
