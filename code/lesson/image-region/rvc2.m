%% 1:04
im = iread('shark1.png');

%% 1:09
idisp(im)

%% 2:06
[v, u] = find(im > 0);

%% 2:24
[u v]

%% 2:55
umin = min(u)

%% 3:03
umax = max(u)

%% 3:14
vmin = min(v)

%% 3:19
vmax = max(v)

%% 3:39
plot_box(umin, vmin, umax, vmax, 'g')

%% 4:08
uc = (umin+umax)/2

%% 4:16
vc = (vmin+vmax)/2

%% 4:32
plot_point([uc, vc]' ,'*')

%% 6:45
m00 = mpq(im, 0, 0)

%% 7:05
m10 = mpq(im, 1, 0)

%% 7:05
m01 = mpq(im, 0, 1)

%% 7:30
ucen = m10 / m00

%% 7:38
vcen = m01 / m00

%% 7:57
plot_point([ucen vcen]', 'o')