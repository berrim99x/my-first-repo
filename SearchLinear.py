def SearchLinear(T:list,taille:int,x:int) -> int:
    for i in range(taille):
        if T[i] == x: return i
    return -1

def main():
    T = [1,2,3,4,5]
    taille = len(T)
    x = 5
    print(SearchLinear(T,taille,x))
