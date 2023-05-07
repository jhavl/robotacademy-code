%% 1:37
im = iread('monalisa.png', 'grey', 'double');

s7 = iconv(im, ones(7, 7));

idisp(im)

figure(2)

idisp(s7)

s21 = iconv(im, ones(21, 21));

idisp(s21)