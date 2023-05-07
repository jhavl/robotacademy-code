%% 3:32
crowd = iread('wheres_walle.png', 'grey', 'double');

%% 3:36
idisp(crowd)

%% 3:53
bender = iread('bender.png', 'double');

%% 4:03
figure(2)

%% 4:09
idisp(bender)

%% 5:03
S = isimilarity(bender, crowd, @zncc);

%% 5:12
idisp(S)

%% 6:48
[mx, p] = peak2(S, 1, 'npeaks', 5)

%% 8:14
plot_circle(p, 30, 'fillcolor', 'b', 'alpha', 0.3, 'edgecolor', 'none')

%% 8:34
plot_circle(p, 'sequence', 'bold', 'textsize', 36, 'textcolor', 'y')

%% 9:35
iroi(crowd, p(:,1), 50)