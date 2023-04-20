%% 2:14 - 6:57

x = jtraj([0 0 0],[-pi/2 pi/2 pi/4],100);

plot(x)

R = rpy2r(x);

R(:,:,1)

R(:,:,10)

tranimate(R)

q1 = Quaternion

q2 = Quaternion( rotx(pi/2) )

q1.interp(q2,0)

q1.interp(q2,1)

q1.interp(q2,0.5)

ans.R