#A씨는 게시판 프로그램을 작성하고 있다.
#A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때, 총 페이지수를
#리턴하는 프로그램이 필요하다고 한다.

def calcNumberOfPages(m, n):
    if (m % n) > 0:
        return m // n +1
    else:
        return m // n

print(calcNumberOfPages(0, 1))
print(calcNumberOfPages(1, 1))
print(calcNumberOfPages(2, 1))
print(calcNumberOfPages(1, 10))
print(calcNumberOfPages(10, 10))
print(calcNumberOfPages(10, 11))
