%% 2:16
L = iread('rocks2-l.png', 'reduce', 2);

%% 2:23
R = iread('rocks2-r.png', 'reduce', 2);

%% 2:46
anaglyph(L, R)

%% 3:05
stdisp(L, R)

%% 5:00
d = istereo(L, R, [40 90], 3);

%% 5:04
idisp(d)
