%% 0:00 - 4:07
p560 = loadrobot("puma560")
J = geometricJacobian(p560,randomConfiguration(p560),'link7') %using random position instead of qn

det(J)

inv(J)

p560 = loadrobot("puma560")
J = geometricJacobian(p560,randomConfiguration(p560),'link7') %using random position instead of qn

nu = [0 0 1 0 0 0]'

inv(J) * nu
