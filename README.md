# PSZT---MM.AE1-Pokrycie-tryskaczami
Application, which optimize locations of sprinklers on the given area, using evolutionary algorithm.

## How to use
1. In input.txt put algorithm parameters
  - width, height - integers to specify area
  - radius - real number - radius of sprinkler
  - rest_area - list of squared restrictions, where sprinklers may not be located, in format of (x_left, x_right, y_down, y_up)
2. Run the application
  ```python3 main.py ```
3.The output (locations of sprinklers) will be printed in output.txt file. You may visualize results by Matlab, using visualization.m script.
