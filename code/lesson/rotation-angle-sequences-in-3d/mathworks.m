%% 3:20 - 8:23

rotm(so3([0.1 0.2 0.3],"eul","ZYZ")) % Using ZYZ is the only config to get this to work

ans = so3([0.1 0.2 0.3],"eul","ZYZ");

eul(ans,"ZYZ")

rotm(so3([0.1 -0.2 0.3],"eul","ZYZ")) % Using ZYZ is the only config to get this to work

ans = so3([0.1 -0.2 0.3],"eul","ZYZ");

eul(ans,"ZYZ") % this one converts back to the correct value, so opposite 
               % what is trying to be demonstrated

rotm(so3(ans,"eul","ZYZ"))

eul2rotm([0.1,0.2,0.3],"XYZ") % to get equivalent output to the video this 
                              % is what is used