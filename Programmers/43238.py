import sys;
sys.setrecursionlimit(10 ** 6)
def solution(n, times):
    def possible(t):
        number = 0
        for v in times:
            number += t // v
        if number >= n:
            return True
        else:
            return False

    times.sort()

    def partition(low, high):
        if low >= high:
            return low

        mid = (low + high) // 2
        K = possible(mid)

        if K:
            return partition(low, mid)
        else:
            return partition(mid+1, high)

    print(partition(0, times[-1] * n))

    return



if __name__ == '__main__':
    solution(6,[7,10])