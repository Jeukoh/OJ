import sys; readline= sys.stdin.readline

N, K = map(int,readline().split())

words = [((set(readline().rstrip())-set(['a','n','t','i','c']))) for _ in range(N)]

def countbit(num):
    cnt = 0
    while num > 0:
        num &= num-1
        cnt +=1
    return cnt

if K < 5:
    print(0)
else:
    K -= 5

    #print(words)

    total_words = set()
    for word in words:
        total_words |= word


    #print(total_words)
    #print(words)

    words = list(map(list,words))

    if K >= len(total_words):
        print(N)
    else:
        #print(K)
        bin_map = {}
        for idx,v in enumerate(total_words):
            bin_map[v] = 1<<idx
        bin_words = []
        for i in words:
            tmp = 0
            for j in i:
                tmp += bin_map[j]
            bin_words.append(tmp)

        #print(bin_words)
        #print(bin_map)
        max_cnt = 0
        cnt = 0
        #max_chose = 0
        for i in range(1<<len(total_words)): # 모든 조합
            if countbit(i) == K:
                cnt = 0
                flag = True
                for value in bin_words:
                    if i&value == value:
                        cnt += 1

                if cnt > max_cnt:
                    max_cnt = cnt
                    max_chose = i

        print(max_cnt)
        #print(max_chose)
