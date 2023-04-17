%% 2:14 - 6:57

q0 = quaternion([0 0 0],'euler','XYZ','point');
qF = quaternion([-pi/2 pi/2 pi/4],'euler','XYZ','point');
[x,w1,a1] = rottraj(q0,qF,[0,99],0:1:99);

plot(0:1:99,compact(x))

R = eul2tform(quat2eul(x));

R(:,:,1)
R(:,:,10)

q1 = quaternion(so3(0,"rotx"))

q2 = quaternion(so3(pi/2,"rotx"))

q0 = quat2rotm(q1)
qF = quat2rotm(q2)

rottraj(q0,qF,[0 1],0)

rotm2quat(rottraj(q0,qF,[0 1],1))

rotm2quat(rottraj(q0,qF,[0 2],1))

quat2rotm(ans)