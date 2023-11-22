n = 0
cell = [0 for _ in range(50*50)]
parent = [i for i in range(50*50)]

def find_parent(node):
    '''
    최상단의 노드를 찾는 함수
    '''
    global parent
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]
    
def union(x,y):
    '''
    합치기
    '''
    global parent
    parent_x = find_parent(x)
    parent_y = find_parent(y)
    if parent_x != parent_y:
        if parent_x < parent_y :
            parent[parent_y] = parent_x
        else:
            parent[parent_x] = parent_y

def find_location(r,c):
    r -= 1
    c -= 1
    return 50*r+c

def replace(loc,value):
    '''
    연결되어있는 셀들까지 한꺼번에 값 변경하기
    '''
    global cell
    for i in range(n):
        if parent[i] == parent[loc]:
            cell[i] = value
    
def solution(commands):
    global n,cell,parent
    answer = []
    cell = [0 for _ in range(50*50)]
    n = len(cell)
    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            if len(command) == 4 :
                # UPDATE r c value
                _,r,c,value = command
                r,c = int(r),int(c)
                loc = find_location(r,c)
                # 연동되어있는 곳의 값도 한꺼번에 바꿔주어야 함!
                replace(loc,value)
            else:
                # UPDATE value1 value2
                _,value1,value2 = command
                for i in range(n):
                    if cell[i] == value1:
                        cell[i] = value2
                    
        elif command[0] == 'MERGE':
            cmd = [int(command[i]) for i in range(len(command)) if i != 0]
            r1,c1,r2,c2 = cmd
            loc_1,loc_2 = find_location(r1,c1),find_location(r2,c2)
            # 선택한 두 위치의 셀이 같은 셀일 경우 무시
            if parent[loc_1] == parent[loc_2]:
                continue 
            # union - find
            union(loc_1,loc_2) 
            for node in range(n):
                find_parent(node)
            if cell[loc_1] != 0:
                # 모두 값을 갖고 있는 경우 또는 loc_1만 값을 갖는 경우
                replace(loc_1,cell[loc_1])
            elif cell[loc_2]!= 0 :
                # loc_2만 값을 갖는 경우
                replace(loc_1,cell[loc_2])
                
        elif command[0] == 'UNMERGE':
            _,r,c = command
            r,c = int(r),int(c)
            loc = find_location(r,c)
            value = cell[loc]
            # 이미 Merge 되어있는 구역 다시 원래 셀 상태로
            parent_loc = parent[loc] 
            for i in range(n):
                if parent[i] == parent_loc: # 연결 되어있는 칸에 대해 
                    parent[i] = i
                    cell[i] = 0
            cell[loc] = value
            
        else:
            _,r,c = command
            r,c = int(r),int(c)
            loc = find_location(r,c)
            if cell[loc] == 0 :
                answer.append("EMPTY")
            else:
                answer.append(cell[loc])
    return answer