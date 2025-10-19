def SearchLinear(T:list,taille:int,x:int) -> int:
    for i in range(taille):
        if T[i] == x: return i
    return -1

def SearchBinary(T:list,x:int,left:int,right:int) -> int:
    mid = (left+right)//2
    while left <= right:
        if T[mid] == x: return mid
        elif T[mid] < x: left = mid + 1
        else: right = mid - 1
    return -1


def main():
    T = [1,2,3,4,5]
    taille = len(T)
    x = 5
    left = 0
    right = len(T) - 1
    print(SearchLinear(T,taille,x))
    print(SearchBinary(T,x,left,right))

main()