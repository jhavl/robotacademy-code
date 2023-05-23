import machinevisiontoolbox as mv
import numpy as np

# 3:42
im = mv.Image.Read("tomato_124.png", gamma = 2.2)
im = im/255 # image was not between 0-1 but 0-255 so adjusting it

# 3:45
im.disp()

# 4:39
cls, cxy, residue = im.kmeans_color(k=4, seed = 0)

# 5:04
cls.disp()

# 6:00
tom = cls == 2 # changed to two to make sure tomatos are selected

# 6:02
tom.disp()

# 7:39
closed = tom.close(np.ones((15, 15)))

# 7:43
closed.disp()

# 8:24
se = mv.Image.Zeros(31)
se.draw_circle((15,15), 15, color = 1, thickness = -1)

# 8:28
se.disp()

# 9:12
closed = tom.close(se.image)

# 9:17
closed.disp()

input("press any key to exit")