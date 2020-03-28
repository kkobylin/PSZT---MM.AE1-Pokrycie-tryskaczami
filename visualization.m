input = fopen('input.txt', 'r');
while ~feof(input)
    param = fgets(input);
    eval(param);
end
fclose(input);
rectangle('Position', [0 0 x y], 'FaceColor', '#FF00FF');
output = fopen('output.txt', 'r');
while ~feof(output)
    circles = fgets(output);
    eval(circles);
end
fclose(output);
