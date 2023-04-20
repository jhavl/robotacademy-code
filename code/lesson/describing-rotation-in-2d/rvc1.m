%% 5:50 -7:08

rot2(0)
rot2(0.2)
rot2(30, 'deg')

R = ans

c1 = R(:, 1)
c2 = R(:, 2)

dot(c1, c2)
det(R)
inv(R)

R'

%% 7:26

trplot2(R)
axis equal