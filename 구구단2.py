
for 수 in range(2,10):
    for 정수  in range(1,수 +1):
        if 수 % 2 == 0:
            print("")
            break
        else:
         print("{}X{}={}".format(수,정수,수 * 정수))