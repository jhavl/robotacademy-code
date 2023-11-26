import machinevisiontoolbox as mv

# 0:03
im = mv.iread('lena.pgm')

#
camera = mv.VideoCamera()
im = camera.grab()

#
camera = mv.WebCam('http://wc2.dartmouth.edu')
im = camera.grab()

#
camera = mv.VideoFile('traffic_sequence.mpg')
images = (im for im in camera)
im = next(images, None)


#
camera = mv.EarthView()
im = camera.grab((latitude, longitude), 14)