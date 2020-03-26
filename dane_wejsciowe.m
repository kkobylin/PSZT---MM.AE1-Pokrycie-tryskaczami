width = 10;
height = 8;
rectangle('Position', [0 0 width height], 'FaceColor', '#FF00FF');
hold on;

circle(4, 6, 2);
circle(7, 1, 2);
circle(1, 4, 2);
circle(8, 4, 2);
circle(8, 5, 2);
circle(4, 3, 2);
% for i = 1 : height - 1
%     for j = 1:  width - 1
%         circle(j, i, 1);
%     end
% end
grid on