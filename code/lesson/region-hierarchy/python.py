import machinevisiontoolbox as mv

# 1:46
im = mv.Image.Read('multiblobs.png')

# 1:51
im.disp()

# 2:01
L, nb = im.labels_binary()

# 2:03
print(nb,"\n")

# 2:11
L.disp()

# 2:39
b = im.blobs()
print(b,"\n")