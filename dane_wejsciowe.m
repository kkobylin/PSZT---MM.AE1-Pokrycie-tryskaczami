height = 4;
width = 7;
r = 1;
rectangle('Position', [0 0 width height], 'FaceColor', '#FF00FF');
hold on;
circle(1, 3, 2);
circle(4, 2, 4);
 circle(1, 1, 2);
% for i = 1 : height - 1
%     for j = 1:  width - 1
%         circle(j, i, 1);
%     end
% end
grid on