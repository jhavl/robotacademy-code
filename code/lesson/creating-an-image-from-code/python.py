import machinevisiontoolbox as mv

# 0:36
im = mv.Image.Zeros(200, dtype = 'float32')

# 0:47
im.draw_box(lt=(0, 0), rb=(1, 1), color=255, thickness = -1)

# 0:51
im.disp()

# 1:40
im.draw_box(lt=(60, 150), rb=(70, 160), color=123, thickness = -1)

# 1:43
im.disp()

# 2:04
circle = mv.Image.Zeros(61)
circle.draw_circle((30, 30), 30, color = 255, thickness = -1)

# 2:10
circle.disp()

# 2:45
im.disp()

# 3:24
im.paste(circle*0.7, (99, 29))

# 3:35
im.disp()

# 4:12
im.draw_line((29, 39), (149, 189), color = 255, thickness = 1)

# 4:18
im.disp()

# 4:43
im = mv.Image.Ramp(200,1)

# 4:46
im.disp()

# 5:28
im = mv.Image.Squares(4, 200, bg = 0, fg = 1)

# 5:30
im.disp()