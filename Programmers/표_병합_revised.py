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
    global cell,parent
    parent_x = find_parent(x)
    parent_y = find_parent(y)
    if cell[parent_x]:
        cell[parent_y] = cell[parent_x]
        parent[parent_y] = parent_x
    else:
        cell[parent_x] = cell[parent_y]
        parent[parent_x] = parent_y    

def find_location(r,c):
    r -= 1
    c -= 1
    return 50*r+c
    
def solution(commands):
    global n,cell,parent
    answer = []
    n = len(cell)
    for command in commands:
        command = command.split()
        if command[0] == 'UPDATE':
            if len(command) == 4 :
                # UPDATE r c value
                _,r,c,value = command
                r,c = int(r),int(c)
                loc = find_location(r,c)
                root = find_parent(loc)
                cell[root] = value
            else:
                # UPDATE value1 value2
                _,value1,value2 = command
                for node in range(n):
                    if cell[node] == value1:
                        cell[node] = value2
                    
        elif command[0] == 'MERGE':
            r1,c1,r2,c2 = map(lambda x: int(x), command[1:])
            loc_1,loc_2 = find_location(r1,c1),find_location(r2,c2)
            # 선택한 두 위치의 셀이 같은 셀일 경우 무시
            if parent[loc_1] == parent[loc_2]:
                continue
            union(loc_1,loc_2)
                
        elif command[0] == 'UNMERGE':
            _,r,c = command
            r,c = int(r),int(c)
            loc = find_location(r,c)
            root = find_parent(loc)
            value_root = cell[root]
            nodes = []
            for node in range(n):
                if find_parent(node) == root:
                    nodes.append(node)
            for node in nodes:
                cell[node] = ''
                parent[node] = node
            cell[loc] = value_root
            
        else:
            _,r,c = command
            r,c = int(r),int(c)
            loc = find_location(r,c)
            root = find_parent(loc)
            value_root = cell[root]
            if not value_root:
                answer.append("EMPTY")
            else:
                answer.append(value_root)
    return answer
