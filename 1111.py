for n in range(50):
    r = bin(n)[2:]
    r += str(r.count('1')%2)
    r += str(r.count('1')%2)
    
