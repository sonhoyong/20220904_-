정수 = int(input("정수를 입력하세요:"))
정답 = '{}는 3의배수입니다'
정답아님 = '{}는 3의배수가 아닙니다'
  if 정수%3==0:
    print(정답.format(정수))
else:
    print(정답아님.format(정수))