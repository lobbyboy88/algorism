#알고리즘 첫번째 공부입니다.
#1000미만의 정수중 3의 배수와 5의 배수의 합을 구하라.

print(list(i for i in range(1000) if i % 3 == 0 or i % 5 == 0 ))