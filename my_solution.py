# Code Up 파이썬 기초 100제 문제풀이

# 6001번
def sol6001():
    print('Hello')

# 6002번
def sol6002():
    print('Hello World')

def sol6003():
    print('Hello')
    print('World')

def sol6004():
    print("'Hello'")

def sol6005():
    print('"Hello World"')

def sol6006():
    print('"!@#$%^&*()\'')

def sol6007():
    print('"C:\\Download\\\'hello\'.py"')

def sol6008():
    print('print("Hello\\nWorld")')
  
def sol6009():
    c = input()
    print(c)

def sol6010():
    n = int(input())
    print(n)

def sol6011():
    f = float(input())
    print(f)

def sol6012():
    num1 = int(input())
    num2 = int(input())
    print(num1)
    print(num2)

def sol6013():
    chr1 = input()
    chr2 = input()
    print(chr2)
    print(chr1)

def sol6014():
    f = float(input())
    for i in range(3):
        print(f)

def sol6015():
    num1, num2 = map(int, input().split())
    print(num1)
    print(num2)

def sol6016():
    chr1, chr2 = input().split()
    print(chr2)
    print(chr1)

def sol6017():
    s = input()
    print(s, s, s)

def sol6018():
    hour, minute = map(int, input().split(':'))
    print(hour, minute, sep=':')

def sol6019():
    year, month, day = map(int, input().split('.'))
    print(day, month, year, sep='-')

def sol6020():
    str1, str2 = input().split('-')
    print(str1, str2, sep='')

def sol6021():
    str = input()
    for c in str:
        print(c)

def sol6022():
    s = input()
    print(s[0:2], s[2:4], s[4:6])

def sol6023():
    s = input().split(':')
    print(s[1])

def sol6024():
    w1, w2 = input().split()
    str = ''.join([w1, w2])
    print(str)

def sol6025():
    num1, num2 = map(int, input().split())
    print(num1+num2)

def sol6026():
    f1 = float(input())
    f2 = float(input())
    print(f1+f2)

def sol6027():
    num = int(input())
    print('%x'%num)

def sol6028():
    num = int(input())
    print('%X'%num)

def sol6029():
    num = int(input(), 16)
    print('%o'%num)

def sol6030():
    c = input()
    print(ord(c))

def sol6031():
    uni = int(input())
    print(chr(uni))

def sol6032():
    num = int(input())
    print(-num)

def sol6033():
    c = input()
    print(chr(ord(c)+1))

def sol6034():
    a, b = map(int, input().split())
    print(a-b)

def sol6035():
    f1, f2 = map(float, input().split())
    print(f1*f2)

def sol6036():
    w, n = input().split()
    print(w*int(n))

def sol6037():
    n = int(input())
    s = input()
    print(s*n)

def sol6038():
    a, b = map(int, input().split())
    print(a**b)

def sol6039():
    f1, f2 = map(float, input().split())
    print(f1**f2)

def sol6040():
    a, b = map(int, input().split())
    print(a//b)

def sol6041():
    a, b = map(int, input().split())
    print(a%b)

def sol6042():
    f = round(float(input()), 2)
    print(f)

def sol6043():
    f1, f2 = map(float, input().split())
    print("%.3f"%round(f1/f2, 3))

def sol6044():
    a, b = map(int, input().split())
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)
    print(round(a/b, 2))

def sol6045():
    a, b, c = map(int, input().split())
    sum = a+b+c
    print(sum, round(sum/3, 2))

def sol6046():
    num = int(input())
    print(num<<1)

def sol6047():
    a, b = map(int, input().split())
    print(a<<b)

def sol6048():
    a, b = map(int, input().split())
    print(a<b)

def sol6049():
    a, b = map(int, input().split())
    print(a==b)

def sol6050():
    a, b = map(int, input().split())
    print(b>=a)

def sol6051():
    a, b = map(int, input().split())
    print(a!=b)

def sol6052():
    num = int(input())
    print(bool(num))

def sol6053():
    a = bool(int(input()))
    print(not a)

def sol6054():
    a, b = map(int, input().split())
    print(bool(a) and bool(b))

def sol6055():
    a, b = map(int, input().split())
    print(bool(a) or bool(b))

def sol6056():
    a, b = map(int, input().split())
    a = bool(a)
    b = bool(b)
    print((a and not b) or (not a and b))

def sol6057():
    a, b = map(int, input().split())
    a = bool(a)
    b = bool(b)
    print((a and b) or (not a and not b))

def sol6058():
    a, b = map(int, input().split())
    a = bool(a)
    b = bool(b)
    print(not (a or b))

def sol6059():
    num = int(input())
    print(~num)

def sol6060():
    a, b = map(int, input().split())
    print(a&b)

def sol6061():
    a, b = map(int, input().split())
    print(a|b)

def sol6062():
    a, b = map(int, input().split())
    print(a^b)

def sol6063():
    a, b = map(int, input().split())
    print(a if a>b else b)

def sol6064():
    a, b, c = map(int, input().split())
    print((a if a<c else c) if a<b else (b if b<c else c))

def sol6065():
    nums = list(map(int, input().split()))
    for num in nums:
        if(num%2==0):
            print(num)

def sol6066():
    nums = list(map(int, input().split()))
    for num in nums:
        print('even' if (num%2==0) else 'odd')

def sol6067():
    num = int(input())
    if num<0:
        print('A' if (num%2==0) else 'B')
    else:
        print('C' if (num%2==0) else 'D')

def sol6068():
    score = int(input())
    if score>=90:
        print('A')
    elif score>=70:
        print('B')
    elif score>=40:
        print('C')
    else:
        print('D')

def sol6069():
    praise = {'A':'best!!!', 'B':'good!!', 'C':'run!', 'D':'slowly~'}
    answer = praise.get(input())
    print(answer if answer!=None else 'what?')

def sol6070():
    season = {0:'winter', 1:'spring', 2:'summer', 3:'fall'}
    print(season[(int(input())%12)//3])

def sol6071():
    while True:
        n = int(input())
        if(n==0):
            break
        print(n)

def sol6072():
    n = int(input())
    while(n!=0):
        print(n)
        n-=1

def sol6073():
    n = int(input())
    for i in range(n-1, -1, -1):
        print(i)

def sol6074():
    for i in range(ord('a'), ord(input())+1):
        print(chr(i), end=' ')

def sol6075():
    for i in range(0,int(input())+1):
        print(i)

def sol6076():
    for i in range(0,int(input())+1):
        print(i)

def sol6077():
    answer = 0
    for i in range(2,int(input())+1, 2):
        answer += i
    print(answer)

def sol6078():
    while True:
        c = input()
        print(c)
        if(c=='q'):
            break

def sol6079():
    n = int(input())
    sum = 0
    for i in range(0,n+1):
        sum += i
        if(sum>=n):
            print(i)
            break
            
def sol6080():
    n, m = map(int,input().split())
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i,j)

def sol6081():
    n = int(input(), 16)
    for i in range(1, 16):
        print('%X*%X=%X'%(n, i, n*i))
    
def sol6082():
    for i in range(1,int(input())+1):
        count = 0
        for j in str(i):
            if(j=='3' or j=='6' or j=='9'):
                count += 1
        if(count==0):
            print(i, end=' ')
        else:
            print('X'*count, end=' ')

def sol6083():
    r, g, b = map(int, input().split())
    for i in range(r):
        for j in range(g):
            for k in range(b):
                print(i,j,k)
    print(r*g*b)

def sol6084():
    h, b, c, s = map(int, input().split())
    print(round((h*b*c*s)/(8*1024*1024), 1), 'MB')

def sol6085():
    w, h, b = map(int, input().split())
    print('%.2f'%round((w*h*b)/(8*1024*1024), 2), 'MB')

def sol6086():
    n = int(input())
    sum = 0
    for i in range(0,n+1):
        sum += i
        if sum>=n:
            print(sum)
            break

def sol6087():
    for i in range(1, int(input())+1):
        if(i%3==0):
            continue
        print(i)

def sol6088():
    a, d, n = map(int,input().split())
    print(a+(n-1)*d)

def sol6089():
    a, r, n = map(int, input().split())
    print(a*(r**(n-1)))

def sol6090():
    a, m, d, n = map(int, input().split())
    answer = a
    for i in range(n-1):
        answer = answer*m+d
    print(answer)

def sol6091():
    a, b, c = map(int, input().split())
    minD = min(a,b,c)
    answer = minD
    while(not (answer%a==0 and answer%b==0 and answer%c==0)):
        answer+=minD
    print(answer)

def sol6092():
    n = int(input())
    called = list(map(int, input().split()))
    counts = [0 for i in range(23)]
    for i in called:
        counts[i-1] += 1
    for i in counts:
        print(i, end=' ')

def sol6093():
    n = int(input())
    called = list(map(int, input().split()))
    called.reverse()
    for num in called:
        print(num, end=' ')

def sol6094():
    n = int(input())
    called = list(map(int, input().split()))
    print(min(called))

def sol6095():
    n = int(input())
    go_pos = []
    for i in range(n):
        x, y = map(int, input().split())
        go_pos.append((x, y))
    
    for i in range(19):
        for j in range(19):
            if (i+1,j+1) in go_pos:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()

def sol6096():
    go_map = []
    for i in range(19):
        go_map.append(list(map(int, input().split())))
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        for j in range(19):
            go_map[x-1][j] = 0 if go_map[x-1][j]==1 else 1
            go_map[j][y-1] = 0 if go_map[j][y-1]==1 else 1
    for line in go_map:
        for num in line:
            print(num, end=' ')
        print()

def sol6097():
    h, w = map(int, input().split())
    n = int(input())
    board = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(n):
        l, d, x, y = map(int, input().split())
        if(d==0):
            for j in range(y-1, y-1+l):
                board[x-1][j] = 1
        else:
            for j in range(x-1, x-1+l):
                board[j][y-1] = 1
    for line in board:
        for num in line:
            print(num, end=' ')
        print()

def sol6098():
    labyrinth = []
    for i in range(10):
        labyrinth.append(list(map(int, input().split())))
    x = 1  # 초기 x좌표
    y = 1  # 초기 y좌표
    while True:
        # 먹이를 찾거나 움직일 수 없는 경우
        if (labyrinth[x][y] == 2 or (labyrinth[x + 1][y] == 1 and labyrinth[x][y + 1] == 1)):
            labyrinth[x][y] = 9
            break
        labyrinth[x][y] = 9
        # 오른쪽으로 갈 수 있는 경우
        if (labyrinth[x][y + 1] != 1):
            y += 1

        # 갈 수 없는 경우
        else:
            x += 1

    for line in labyrinth:
        for num in line:
            print(num, end=' ')
        print()