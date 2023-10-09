def TOH(n,src,aux,dest):
    if n<=1:
        print(src+"->"+dest)
        return
    TOH(n-1, 'src', 'dest', 'aux') #recursive call so n-1
    print(src + "->" + dest)
    TOH(n-1, 'aux', 'src', 'dest')
n=3
TOH(n,'src','aux','dest')
r=(2**n)-1
print('moves=',r)