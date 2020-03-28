width = 3;
height = 3;
rectangle('Position', [0 0 width height], 'FaceColor', '#FF00FF');
hold on;

circle(1, 1, 1)
circle(1, 2, 1)
circle(2, 1, 1)
circle(2, 2, 1)
% for i = 1 : height - 1
%     for j = 1:  width - 1
%         circle(j, i, 1);
%     end
% end
grid on