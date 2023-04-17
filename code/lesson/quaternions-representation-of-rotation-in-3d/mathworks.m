%% 3:46 - 6:20

R = eul2rotm([0.1,0.2,0.3],"ZYZ")

quaternion(R,'rotmat','point')

q = ans

plotTransforms([0 0 0],q)

q'

q .* q'

q ./ q

rotmat(q,'point') * [1 0 0]'

q0 = quaternion(1,0,0,0)

slerp(q0,q,0)

slerp(q0,q,1)

slerp(q0,q,0.5)
