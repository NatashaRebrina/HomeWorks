def fact(n):
    f = 1
    for i in range (2, n+1):
        f *= i
    return(f)

def sochetanie(m,n):
    s1 = 1
    for i in range (2, n+1):
        s1 *= i
        s2 = 1
    for i in range (2, m+1):
        s2 *= i
        s3 = 1
    for i in range(2, (n-m)+1):
        s3 *= i
        s = s1 / (s2*s3)
    return(s)

def razm(m,n):
    r1 = 1
    for i in range (2, n+1):
        r1 *= i
    r2 = 1
    for i in range (2, m+1):
        r2 *= i
    r3 = 1
    for i in range(2, (n-m)+1):
       r3 *= i
    r = r1*r2 / (r2*r3)
    return(r)