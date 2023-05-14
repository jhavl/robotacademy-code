%% 3:42
im = iread('tomato_124.jpg', 'gamma', 2.2);

%% 3:45
idisp(im)

%% 4:39
[cls, cxy, residue] = colorkmeans(im, 4);

%% 4:59
figure

%% 5:04
idisp(cls)

%% 6:00
tom = cls == 3;

%% 6:02
idisp(tom)

%% 7:39
closed = iclose(tom, ones(15,15) );

%% 7:43
idisp(closed)

%% 8:24
se = kcircle(15);

%% 8:28
idisp(se)

%% 9:12
closed = iclose(tom, se);

%% 9:17
idisp(closed)