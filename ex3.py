I = abs(int(input("digite um numero inteiro positivo: ")))
A = float(input("digite um numero: "))
B = float(input("digite um numero: "))
C = float(input("digite um numero: "))
if I == 1 :
    if A<B and A<C: 
        print(A)
    elif B<A and B<C: 
        print(B)
    if C<A and C<B: 
        print(C)
    if A>B and A<C or A<B and A>C:
        print(A)
    if B>A and B<C or B<A and B>C:
        print(B)
    if C>B and C<A or C<B and C>A:
        print(C)
    if A>B and A>C: 
        print(A)
    elif B>A and B>C: 
        print(B)
    if C>A and C>B: 
        print(C)
if I == 2: 
    if A>B and A>C: 
        print(A)
    elif B>A and B>C: 
        print(B)
    if C>A and C>B: 
        print(C)
    if A>B and A<C or A<B and A>C:
        print(A)
    if B>A and B<C or B<A and B>C:
        print(B)
    if C>B and C<A or C<B and C>A:
        print(C)
    if A<B and A<C: 
        print(A)
    elif B<A and B<C: 
        print(B)
    if C<A and C<B: 
        print(C)
if I == 3:
    if A>B and A<C or A<B and A>C:
        print(A)
    if B>A and B<C or B<A and B>C:
        print(B)
    if C>B and C<A or C<B and C>A:
        print(C)
    if A>B and A>C: 
        print(A)
    elif B>A and B>C: 
        print(B)
    if C>A and C>B: 
        print(C)
    if A<B and A<C: 
        print(A)
    elif B<A and B<C: 
        print(B)
    if C<A and C<B: 
        print(C)
if I != 1 and I != 2 and I!= 3:
    print("nao tem como")

