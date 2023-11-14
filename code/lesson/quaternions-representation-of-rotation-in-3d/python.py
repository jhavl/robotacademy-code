import spatialmath.base as smb
import numpy as np

def qqdiv(q1, q2):
    q1 = smb.getvector(q1, 4)
    q2 = smb.getvector(q2, 4)
    s1 = q1[0]
    v1 = q1[1:4]
    s2 = q2[0]
    v2 = q2[1:4]

    quat = np.zeros(4)
    quat[0] = s1 * s2 + np.dot(v1, v2)
    quat[1:4] = s1 * v2 - s2 * v1 + np.cross(v1, v2)

    return quat

# 3:46 - 6:20
R = smb.eul2r(0.1, 0.2, 0.3)
print(R, "\n")

smb.qprint(smb.r2q(R))
print("\n")

q = smb.r2q(R)
smb.qprint(q)
print("\n")

smb.trplot(R)

smb.qprint(smb.qconj(q))
print("\n")

smb.qprint(smb.qqmul(q, smb.qconj(q)))
print("\n")

smb.qprint(qqdiv(q, q))
print("\n")

print(np.matmul(smb.q2r(q), [1, 0, 0]), "\n")

q0 = smb.qunit([1, 0, 0, 0])
smb.qprint(q0)
print("\n")

smb.qprint(smb.qslerp(q0, q, 0))
print("\n")

smb.qprint(smb.qslerp(q0, q, 1))
print("\n")

smb.qprint(smb.qslerp(q0, q, 0.5))
print("\n")
