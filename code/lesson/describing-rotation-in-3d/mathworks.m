%% 5:22 - 6:40

rotm(so3(0.2,'rotx'))

rotm(so3(30*(pi/180),'rotx'))

R = ans

det(R)

inv(R)

R'

rotm(so3(0.2,'roty'))

rotm(so3(0.3,'rotz'))

plotTransforms(se3(ans))
