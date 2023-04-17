class Node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
nameAry = ['A', 'B', 'C', 'D', 'E', 'F']

node = Node()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = Node()
    node.data = name

    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
        
    memory.append(node)

findName = 'E'

current = root
while True:
    if findName == current.data:
        print(findName, "을 찾음.")
        break
    elif findName < current.data:
        if current.left == None:
            print("X")
            break
        current = current.left
    else:
        if current.right == None:
            print("X")
            break
        current = current.right

    print(current.data)

deleteName = 'C'

current = root
parent = None
while True:
    if deleteName == current.data:
        if current.left == None and current.right == None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del(current)
        
        elif current.left != None and current.right == None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del(current)

        elif current.left == None and current.right != None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            del(current)
        
        print(deleteName, '가 삭제됨')
        break
    elif deleteName < current.data:
        if current.left == None:
            print("data X")
            break
        parent = current
        current = current.left
    else:
        if current.right == None:
            print("data X")
            break
        parent = current
        current = current.right
