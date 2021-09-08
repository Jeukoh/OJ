def solution(key, lock):
    # lock을 가득 채워야한다. lock 사이즈와 0의 개수를 확인
    def lockcheck(lock):
        N = len(lock)
        min_x = min_y = N
        max_x = max_y = 0
        cnt = 0
        home = []
        for x in range(N):
            for y in range(N):
                if not lock[x][y]:
                    cnt += 1
                    min_x = x if min_x > x else min_x
                    max_x = x if max_x < x else max_x
                    min_y = y if min_y > y else min_y
                    max_y = y if max_y < y else max_y

        holl = [[1-lock[r][c] for c in range(min_y,max_y+1)] for r in range(min_x,max_x+1)]

        return cnt, holl

    def rotate(cand_key):
        N = len(cand_key)
        M = len(cand_key[0])
        ret_key = [[0]*N for _ in range(M)]
        for x in range(M):
            for y in range(N):
                ret_key[x][y] = cand_key[N-y-1][x]

        return ret_key



    cnt0, holl = lockcheck(lock)
    holl_list = [holl]

    if not cnt0:
        return True

    for _ in range(4):
        new_holl = rotate(holl)
        if new_holl in holl_list:
            break
        holl_list.append(new_holl)
        holl = new_holl

    N = len(key)
    for holl in holl_list:
        lx = len(holl)
        ly = len(holl[0])
        for sx in range(N-lx+1):
            for sy in range(N-ly+1):
                cand_key = [[key[x][y] for y in range(sy,sy+ly)] for x in range(sx,sx+lx)]
                if holl == cand_key:
                    return True


    return False


if __name__ == '__main__':
    print(solution([[0,0,0],[1,0,1],[0,1,0]],[[1,1,1],[1,1,1],[1,1,1]]),True)