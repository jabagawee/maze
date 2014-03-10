#! /bin/sh

echo "Press ^C when you're done gathering data!"
python -m cProfile -o temp.profile main.py maze.gif
python gprof2dot.py -f pstats temp.profile | dot -Tpng -o profile.png
open profile.png
