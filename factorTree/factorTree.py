import sys
from tree.treeNode import TreeNode

# Use
#   alias factorTree='cd ~ && cd rootdir-scripts && cd factorTree && f(){pipenv run python3 factorTree.py "$1"; unset -f f; cd ~;}; f'
# to run from terminal


def createFactorTree():
    num = int(sys.argv[1])
    root = TreeNode(num)

    if root.val < 0:
        root.left = TreeNode(-1)
        root.right = TreeNode(-1 * root.val)
        factorTreeHelper(root.right, num)
    else:
        factorTreeHelper(root, num)
    printOrder(root)


def printOrder(root):
    if root == None:
        return

    numSpaces = 4
    queue = []
    queue.append(root)
    first = True  # Change to a mod of numSpaces
    count = 0
    prev = None

    while len(queue):
        cur = queue.pop(0)
        if first:
            first = False
            print("{0: >{1}}".format(cur.val, numSpaces + 1))
        elif count % 2 == 1:
            if queue[0].val < 10:
                if prev < 10:
                    print("{0: >{1}}".format(cur.val, numSpaces - 3), end="   ")
                else:
                    print("{0: >{1}}".format(cur.val, numSpaces - 4), end="    ")
            else:
                print("{0: >{1}}".format(cur.val, numSpaces - 4), end="   ")
        else:
            print(cur.val)
        count += 1
        prev = cur.val
        if not len(queue) and (cur.left or cur.right):
            numSpaces += 2
            if cur.val < 10:
                print("{0: >{1}}".format("/ \\", numSpaces))
            else:
                print("{0: >{1}}".format("/  \\", numSpaces))
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)


def factorTreeHelper(cur, val):
    for i in range(2, val // 2):
        if val % i == 0:  # Check if i is a factor
            cur.left = TreeNode(i)
            cur.right = TreeNode(val // i)
            factorTreeHelper(cur.left, i)
            factorTreeHelper(cur.right, val // i)
            return

    if val == 4:
        cur.left = TreeNode(2)
        cur.right = TreeNode(2)


createFactorTree()
