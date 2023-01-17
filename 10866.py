from collections import deque
import sys

arr=deque()

def empty():
    if len(arr)==0:
        return 1
    else: return 0
def push_front(x):
    arr.appendleft(x)
def push_back (x):
    arr.append(x)
def pop_front():
    if empty()==1:
        print(-1)
    else:
        print(arr.popleft())
def pop_back():
    if empty() == 1:
        print(-1)
    else:
        print(arr.pop())
def front():
    if empty() == 1:
        print(-1)
    else:
         print(arr[0])
def back():
    if len(arr) == 0:
         print(-1)
    else:
         print(arr[len(arr)-1])

def size():
    print(len(arr))


r=int(input())
cmd=[]
for _ in range(r):
    cmd=list(sys.stdin.readline().split())

    if cmd[0]=='push_front':
        push_front(cmd[1])
    elif cmd[0]=='push_back':
        push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        pop_front()
    elif cmd[0] == 'pop_back':
        pop_back()
    elif cmd[0] == 'size':
        size();
    elif cmd[0] == 'empty':
        print(empty())
    elif cmd[0] == 'front':
        front()
    elif cmd[0] == 'back':
        back()
