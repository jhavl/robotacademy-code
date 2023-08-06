import machinevisiontoolbox as mv
import matplotlib.pyplot as plt

# 5:16
im = mv.Image.Read('shark2.png')

im.disp()

# 5:38
L, nb = im.labels_binary()

# 5:43
print(nb,"\n")

# 6:00
L.disp()

# 6:50
(L==1).disp()

# 7:00
(L==2).disp()

# 7:42
b = im.blobs()

# 8:36
im.disp()

# 8:44
b[0].plot_box(color = 'g')
plt.show()

# 8:50
b[1].plot_box(color = 'g')
plt.show()

# 9:07

# 9:13
print(b[1].area,"\n")

# 9:19
print(b[1].parent,"\n")

# 9:28
print(b[1].centroid,"\n")

# 9:34
print(b[1].centroid[0],"\n")

# 9:41
print(b[1].moments.m01,"\n")

input("Press any key to exit")