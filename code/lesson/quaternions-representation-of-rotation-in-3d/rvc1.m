%% 3:46 - 6:20

R = eul2r(0.1, 0.2, 0.3)

Quaternion(R)

q = ans

q.plot()

inv(q)

q * inv(q)

q / q

q * [1 0 0]'

q0 = Quaternion

q0.interp(q,0)

q0.interp(q,1)

q0.interp(q,0.5)
