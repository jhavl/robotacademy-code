import machinevisiontoolbox as mv

# 1:18
video = mv.VideoFile("traffic_sequence.mp4")

# 1:31 - 1:42
for im in video:
    im.disp()

    if im.id == 6:
        break

# 1:50
print(video)
