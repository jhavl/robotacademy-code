%% 0:45
T0 = eye(4,4)

T1 = se3([1, 2, 3], "trvec") * se3([1.4, 0.8, 0.6], "eul")

%% 1:26
plotTransforms(se3(T0))

%% 1:39
plotTransforms(se3(T1))

%% 1:53
tInterval = [0 1];
tvec = 0:0.05:1;
[tfInterp, ~, ~] = transformtraj(T0,T1,tInterval,tvec);
rotations = tform2quat(tfInterp);
translations = tform2trvec(tfInterp);
plotTransforms(translations,rotations)