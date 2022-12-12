class Node: pass

class Node:

    def __init__(self, height : str):
        self.__height = height
        self.__edges = []

    def add_edge(self, node : Node):
        self.__edges.append(node)

    def is_start(self):
        return self.__height == 'S'

    def is_end(self):
        return self.__height == 'E'

    def is_start_candidate(self):
        return self.__height == 'a'

    @property
    def height(self):
        if self.__height == 'S':
            height = 'a'
        elif self.__height == 'E':
            height = 'z'
        else:
            height = self.__height
        return ord(height) - ord('a')

    @property
    def neighbors(self):
        return self.__edges

    @staticmethod
    def shortest_path(start : Node, unvisited : set):

        distances = {node: float('inf') for node in unvisited}
        distances[start] = 0
        
        while unvisited:
            current = min(unvisited, key=lambda node: distances[node])

            # Mark the current node as visited
            unvisited.remove(current)

            # Update the distances to the neighbors of the current node
            for neighbor in current.neighbors:
                if neighbor in unvisited:
                    distances[neighbor] = min(distances[neighbor], distances[current] + 1)

        return distances

def part_1():
    with open("data/data_12") as fp_in:
        buffer = fp_in.read()
        grid = [[Node(ele) for ele in line] for line in buffer.split()]

        N = len(grid)
        M = len(grid[0])

        start = None
        end = None
        nodes = set()
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if 0 < i: 
                    next = grid[i-1][j]
                    if next.height <= ele.height + 1: ele.add_edge(next)
                if i < N-1: 
                    next = grid[i+1][j]
                    if next.height <= ele.height + 1: ele.add_edge(next)
                if 0 < j: 
                    next = grid[i][j-1]
                    if next.height <= ele.height + 1: ele.add_edge(next)
                if j < M-1: 
                    next = grid[i][j+1]
                    if next.height <= ele.height + 1: ele.add_edge(next)

                if ele.is_start():
                    start = ele
                if ele.is_end():
                    end = ele
                nodes.add(ele)

        distances = Node.shortest_path(start, nodes)

        print( "Part 1:", distances[end] )

def part_2():
    with open("data/data_12") as fp_in:
        buffer = fp_in.read()
        grid = [[Node(ele) for ele in line] for line in buffer.split()]

        N = len(grid)
        M = len(grid[0])

        end = None
        nodes = set()
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if ele.is_end():
                    end = ele
                if 0 < i: 
                    next = grid[i-1][j]
                    if next.height <= ele.height + 1: next.add_edge(ele)
                if i < N-1: 
                    next = grid[i+1][j]
                    if next.height <= ele.height + 1: next.add_edge(ele)
                if 0 < j: 
                    next = grid[i][j-1]
                    if next.height <= ele.height + 1: next.add_edge(ele)
                if j < M-1: 
                    next = grid[i][j+1]
                    if next.height <= ele.height + 1: next.add_edge(ele)

                nodes.add(ele)

        distances = Node.shortest_path(end, set(nodes))

        start_distances = [distance for node, distance in distances.items() if node.is_start_candidate()]

        print( "Part 2:", min(start_distances) )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()