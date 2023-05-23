import machinevisiontoolbox as mv

# 4:03
im = mv.Image.Read('shark2a.png')

# 4:07
im.disp()

# 4:21
b = mv.Blobs(im)
print(b)

# 6:32
im.draw_circle((int(b.centroid[0][0]),int(b.centroid[0][1])), 85, color = 255)
im.draw_circle((int(b.centroid[1][0]),int(b.centroid[1][1])), 85, color = 255)
im.disp()

# 6:42
im.draw_circle((int(b.centroid[0][0]),int(b.centroid[0][1])), 3, color = 0, thickness = -1)
im.draw_circle((int(b.centroid[1][0]),int(b.centroid[1][1])), 3, color = 0, thickness = -1)
im.disp()

input("press any key to exit")