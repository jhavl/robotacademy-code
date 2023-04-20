%% 4:20 - 6:11
mdl_hyper3d(20)

q = rand(1,20)

h3d.plot(q)

J = h3d.jacobn(q)

inv(J)

pinv(J)

N = null(J)

rank(J)
