%% 1:58
first = [10 20]

%% 2:03
last = [30 10]

%% 2:17
x = jtraj(first, last, 50)

%% 2:34
plot(x)

%% 2:52
[x, xd] = jtraj(first, last, 50)

%% 2:57
plot(xd)

%% 3:20
[x, xd] = jtraj(first, last, 50, [0 0], [10 10])

%% 3:22
plot(x)

%% 4:39
start = [40 50]

%% 4:55
via = [60 30; 40 10; 20 30; start] 

%% 5:22
x = mstraj(via, 2, [], start, 0.1, 1);

%% 5:41
plot(x)

%% 5:56
plot(x(:,1), x(:,2))

%% 7:56
x = mstraj(via, [1 3], [], start, 0.1, 1);

%% 8:32
plot(x)

%% 8:40
plot(x(:,1), x(:,2))

