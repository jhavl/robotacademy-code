%% 0:03
im = iread('lena.pgm')

%%
camera = VideoCamera();
im = camera.grab();

%%
camera = AxisWebCamera('http://wc2.dartmouth.edu');
im = camera.grab();

%%
camera = Movie('traffic_sequence.mpg');
im = camera.grab();

%%
camera = EarthView('satellite');
im = camera.grab('brisbane', 14)
