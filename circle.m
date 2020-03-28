function h = circle(x,y,r)
    hold on
    th = 0:pi/50:2*pi;
    xunit = r * cos(th) + x;
    yunit = r * sin(th) + y;
    h = plot(xunit, yunit);
    scatter(x, y, 'MarkerFaceColor', h.Color, 'MarkerEdgeColor', h.Color, 'MarkerFaceAlpha', 0.5, 'LineWidth', 0.2);
    %fill(xunit, yunit, 'r')
    hold off
    axis equal
end