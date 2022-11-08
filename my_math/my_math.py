import combinatorics
import areas
a = input('комбинаторика или геометрия?')
if a == 'комбинаторика':
    b = int(input('1 - факториал\количество перестановок;2 - количество сочетаний; 3 - количество размещений'))
    if b == 1:
        n = int(input(''))
        print(combinatorics.fact(n))
    elif b == 2:
        n = int(input('число'))
        m = int(input('число'))
        print(combinatorics.sochetanie(m,n))
    elif b == 3:
        n = int(input('число'))
        m = int(input('число'))
        print(combinatorics.razm(m,n))
elif a == 'геометрия':
    print('площади: 1 - шара; 2 - квадрата; 3 - прямоугольника; 4 - треугольника')
    b = int(input())
    if b == 1:
        R = int(input('радиус'))
        print(areas.Sshar(R))
    elif b == 2:
        A = int(input('сорона квадрата'))
        print(areas.Skvadrat(A))
    elif b == 3:
        A = int(input('сторона прямоугольника'))
        B = int(input('сторона прямоугольника'))
        print(areas.Spr(A,B))
    elif b == 4:
        A = int(input('сторона треугольника'))
        h = int(input('высота'))
        print(areas.Streugolnik(A,h))
