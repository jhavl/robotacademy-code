%% 3:20 - 8:23

eul2r(0.1, 0.2, 0.3)

tr2eul(ans)

eul2r(0.1, -0.2, 0.3)

tr2eul(ans)

eul2r(ans)

rpy2r(0.3, 0.2, 0.1,'xyz') % I checked all configurations of options and found 
                           % that the only thing that works and gets the 
                           % correct result is not what is stated on the 
                           % video footnotes but rather to reverse
                           % the sequences of the roll pitch and yaw to yaw
                           % pitch and roll with 'xyz' as the option