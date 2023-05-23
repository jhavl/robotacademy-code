import machinevisiontoolbox as mv

# 2:16
L = mv.Image.Read("rocks2-l.png", reduce = 2)

# 2:23
R = mv.Image.Read("rocks2-r.png", reduce = 2)

# 2:46
L.anaglyph(R).disp()

# 3:05
L.stdisp(R)

# 5:00
disparity, similarity, DSI = L.stereo_simple(R, hw=3, drange=[40, 90])

# 5:04
disparity.disp()

input("press any key to exit")