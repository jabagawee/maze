import sys

from maze import Maze

def main():
    maze = Maze(sys.argv[1])
    maze.solve()
    maze.solved_image.save("solved.png")
    maze.solved_image.show()

if __name__ == "__main__":
    main()
