%% 5:14 - 11:17

transl2(1,2)

rot2(30, 'deg')

trot2(30, 'deg')

transl2(1,2) * trot2(30,'deg')

SE2(1,2,30,'deg')

axis([0 5 0 5])

xis square

hold on

T1 = SE2(1,2,30,'deg')

trplot2(T1,'frame','1','color','b')

T2 = SE2(2,1,0)

trplot2(T2,'frame','2','color','r')

T3 = T1 * T2

trplot2(T3,'frame','3','color','g')

T4 = T2 * T1

trplot2(T4,'frame','4','color','c')

P = [3 2]'

plot_point(P,'*')

P1 = inv(T1.T) * [P ; 1]
