from enum import Enum

class FSType(Enum):
    file = 0,
    directory = 1,
    pipe = 2,
    link = 3,
    unk = 4,

class FSNode: pass # python IDE voodoo
class FSNode():

    def __init__(self, name : str, type : FSType, parent=None, size=0):
        self.__name = name
        self.__size = size
        self.__parent = parent
        self.__type = type
        self.__children = []

    def add_child(self, node : FSNode):
        for child in self.__children:
            if child.name == node.name:
                return
        self.__children.append(node)

    def size(self):
        _sum = sum([child.size() for child in self.__children])
        return self.__size + _sum

    @property
    def type(self):
        return self.__type

    @property
    def name(self):
        return self.__name

    @property
    def children(self):
        return self.__children

    @property
    def parent(self):
        return self.__parent

    @staticmethod
    def construct_fs(lines : list[str]):
        
        # I just chop of the first 2 lines for simplicity
        lines = lines[1:]
        root = FSNode("/", FSType.directory)
        
        curr = root
        i = 0
        while i < len(lines):
            line = lines[i]
            
            i+=1
            if line.startswith("$ ls"):
                while i < len(lines):
                    line = lines[i]
                    if line.startswith("$"): break
                    c1, name = line.split(" ")
                    if c1 == "dir":
                        curr.add_child(FSNode(name, FSType.directory, parent=curr))
                    else:
                        curr.add_child(FSNode(name, FSType.file, parent=curr, size=int(c1)))    
                    i+=1
            elif line.startswith("$ cd"):
                _, __, directory = line.split(" ")
                if directory == "..":
                    parent = curr.parent
                    if parent:
                        curr = parent
                else:
                    found = False
                    for child in curr.children:
                        if child.name == directory:
                            if child.type != FSType.directory:
                                print(f"Warning! {directory} is not a directory.")
                                break
                            curr = (child)
                            found = True
                            break
                    if not found:
                        print("Warning, tried to cd somewhere that don't exist.")

        return root

def part_1():
    with open("data/data_7") as fp_in:
        buffer = fp_in.read()
        lines = buffer.split("\n")

        fs = FSNode.construct_fs(lines)

        size_total = 0
        def dfs(node : FSNode):
            nonlocal size_total
            size = node.size()
            if size <= 100000:
                size_total += size
            for child in node.children:
                if child.type == FSType.directory:
                    dfs(child)

        dfs(fs)

        print( "Part 1:", size_total )

def part_2():
    with open("data/data_7") as fp_in:
        buffer = fp_in.read()
        lines = buffer.split("\n")

        fs = FSNode.construct_fs(lines)

        size_min = fs.size()
        node_min = fs
        def dfs(node : FSNode):
            nonlocal space_to_delete
            nonlocal size_min
            nonlocal node_min

            size = node.size()
            if space_to_delete <= size and size < size_min:
                size_min = size
                node_min = node

            for child in node.children:
                if child.type == FSType.directory:
                    dfs(child)

        space_total = 70000000
        space_needed = 30000000
        space_to_delete = space_needed - (space_total - fs.size())

        dfs(fs)

        print( "Part 2:", node_min.size() )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()