width = 12;
height = 5;
rectangle('Position', [0 0 width height], 'FaceColor', '#FF00FF');
hold on;

circle(6, 2, 3);
circle(4, 2, 3);
circle(10, 4, 3);
% for i = 1 : height - 1
%     for j = 1:  width - 1
%         circle(j, i, 1);
%     end
% end
grid on