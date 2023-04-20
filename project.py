def create_permutation(id):
    Nmin,Nmax=500,700
    global seed
    seed=id
    def randint(a,b):
        global seed
        seed=(48271*seed)%(2**31-1)
        return a+seed%(b-a)
    n=randint(Nmin,Nmax+1)
    pi=[]
    for i in range(n):
        pi.insert(randint(0,1+i),i)
    return pi