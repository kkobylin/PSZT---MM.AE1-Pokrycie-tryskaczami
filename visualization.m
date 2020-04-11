input = fopen('input.txt', 'r');
for i = 1:4
    param = fgets(input);
    eval(param);
end
% restricted area
param = fgets(input);
param  = strrep(param, '[', '{');
param  = strrep(param, ']', '}');
param  = strrep(param, '(', '[');
param  = strrep(param, ')', ']');
eval(param);

fclose(input);
rectangle('Position', [0 0 width height]);
axis([0-radius, width+radius, 0-radius, height+radius]);
grid on;
for i = 1:size(rest_area, 2)
    rectangle('Position', [rest_area{i}(1) rest_area{i}(3) rest_area{i}(2)-rest_area{i}(1) rest_area{i}(4)-rest_area{i}(3)], 'FaceColor', [0.749, 0.749, 0.749], 'EdgeColor', [0.749, 0.749, 0.749]);
end
output = fopen('output.txt', 'r');
while ~feof(output)
    circles = fgets(output);
    eval(circles);
end

fclose(output);