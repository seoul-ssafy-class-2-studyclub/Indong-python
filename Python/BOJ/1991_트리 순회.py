from sys import stdin

def preorder(node):
    global pre
    left = tree[node][1]
    right = tree[node][2]
    pre += chr(node + ord('A') - 1)
    if left:
        preorder(left)
    if right:
        preorder(right)


def inorder(node):
    global inord
    left = tree[node][1]
    right = tree[node][2]
    if left:
        inorder(left)
    inord += chr(node + ord('A') - 1)
    if right:
        inorder(right)


def postorder(node):
    global post
    left = tree[node][1]
    right = tree[node][2]
    if left:
        postorder(left)
    if right:
        postorder(right)
    post += chr(node + ord('A') - 1)


input = stdin.readline
N = int(input())
# [부모, 왼쪽, 오른쪽]
tree = [[0, 0, 0] for _ in range(N + 1)]
dot = ord('.') - ord('A') + 1
for i in range(N):
    node, left, right = map(lambda x: ord(x) - ord('A') + 1, input().split())
    if left != dot:
        tree[left][0] = node
        tree[node][1] = left
    if right != dot:
        tree[right][0] = node
        tree[node][2] = right


for i in range(1, N + 1):
    if not tree[i][0]:
        pre = ''
        inord = ''
        post = ''
        preorder(i)
        inorder(i)
        postorder(i)
        break

print(pre)
print(inord)
print(post)
