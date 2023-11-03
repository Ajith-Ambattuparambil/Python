def sum_total(req):
    if len(req)==1:
        return req[0]
    else:
        return req[0]+sum_total(req[1:])
l=input("Enter numbers: ")
l=list(map(int,l.split(',')))
print('sum of elements: ',sum_total(l))
