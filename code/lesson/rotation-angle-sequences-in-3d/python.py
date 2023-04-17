import spatialmath.base as smb

# 3:20 - 8:23

print(smb.eul2r(0.1, 0.2, 0.3), "\n")

print(smb.tr2eul(smb.eul2r(0.1, 0.2, 0.3)), "\n")

print(smb.eul2r(0.1, -0.2, 0.3), "\n")

print(smb.tr2eul(smb.eul2r(0.1, -0.2, 0.3)), "\n")

ans = smb.tr2eul(smb.eul2r(0.1, -0.2, 0.3))

print(smb.eul2r(ans), "\n")

print(smb.rpy2r([0.3, 0.2, 0.1], order="xyz"), "\n")
