%% 1:11 - 2:26

T0 = eye(4,4)

T1 = tform(se3([1,2,3],"trvec"))*eul2tform([0.6,0.8,1.4])

[T,~,~] = transformtraj(T0,T1,[0 49],0:1:49);

T(:,:,1)

T(:,:,10)

% plotTransforms(T) 
% plot function does not work for animations, Robotics
% toolbox v10 tranimate function will work for this