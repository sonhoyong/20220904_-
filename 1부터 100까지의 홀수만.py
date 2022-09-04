전체합 = 0
홀수합 = 0
짝수합 = 0

for i in range(1,101):
    전체합 = 전체합 + 1
    if i % 2 ==1:
        홀수합 = 홀수합 +1
    else:
        짝수합 = 짝수합 + 1
print(짝수합)
print(홀수합)
print(전체합)