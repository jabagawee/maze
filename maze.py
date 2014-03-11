from PIL import Image

from priority_queue import PriorityQueue

class Maze(object):
    def __init__(self, filename):
        self.image = Image.open(filename).convert("1")
        self.w, self.h = self.image.size
        self.pixels = self.image.load()
        self.start, self.end = self.endpoints()
        self.parents = {self.start: None, self.end: None}
        self.g_scores = {self.start: 0}

    def endpoints(self):
        endpoints = []
        for y in range(self.h):
            if self.pixels[0, y]:
                endpoints.append((0, y))
            if self.pixels[self.w - 1, y]:
                endpoints.append((self.w - 1, y))
        for x in range(self.w):
            if self.pixels[x, 0]:
                endpoints.append((x, 0))
            if self.pixels[x, self.h - 1]:
                endpoints.append((x, self.h - 1))
        return endpoints

    def neighbors(self, position):
        x, y = position
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        neighbors = [(x, y) for (x, y) in neighbors
                if 0 <= x < self.w and 0 <= y < self.h and self.pixels[x,y]]
        return neighbors

    # heuristics

    def manhattan(self, position):
        dx = abs(position[0] - self.end[0])
        dy = abs(position[1] - self.end[1])
        return dx + dy

    heuristic = manhattan

    # search algorithms

    def dfs(self, animate=False):
        pass

    def astar(self, animate=False):
        empty_space_count = self.image.histogram()[255]
        fringe = PriorityQueue()
        fringe.push(self.start, self.heuristic(self.start))
        explored = set()

        while fringe:
            if len(explored) % 100000 == 0:
                print "Explored %d/%d nodes! %.3f%% done!" % (len(explored), empty_space_count, len(explored)/float(empty_space_count))

            node, cost = fringe.pop()
            if node == self.end:
                self.path = [node]
                while self.parents[node]:
                    self.path.append(self.parents[node])
                    node = self.parents[node]

            explored.add(node)

            for neighbor in self.neighbors(node):
                if neighbor in explored:
                    continue

                g_score = self.g_scores[node] + 1

                if neighbor not in fringe or g_score < self.g_scores[neighbor]:
                    self.parents[neighbor] = node
                    self.g_scores[neighbor] = g_score
                    fringe.push(neighbor, g_score + self.heuristic(neighbor))

        print "No Solution"

    def bfs(self, animate=False):
        self.heuristic, old_heuristic = lambda position: 0, self.heuristic
        self.astar(animate=animate)
        self.heuristic = old_heuristic

    def jps(self, animate=False):
        """Reference:
            http://zerowidth.com/2013/05/05/jump-point-search-explained.html"""
        pass

    algorithm = astar

    def solve(self, animate=False):
        RED = (255, 0, 0)
        self.algorithm(animate=animate)
        self.solved_image = self.image.convert("RGB")
        self.solved_pixels = self.solved_image.load()
        for pixel in self.path:
            self.solved_pixels[pixel] = RED
