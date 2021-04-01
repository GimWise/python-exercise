# 연습문제 - 제어문, 반복문
# 1) shirt

# 2)
# num=1
# sum=0;
# while num<=100:
#     if num%4==0:
#         sum+=num;
#     num+=1 
# print(sum)        

# 3)
# sum=0
# for i in range(101):
#     if i%5==0:
#         sum+=i;
# print(sum)        

# 4)
# py_score = [20,55,67,82,45,33,90,87,100,25]
# sum=0
# std_num=0;

# for py_score in py_score :
#     if py_score >=60:
#         sum+=py_score
#         std_num+=1
# print(sum/std_num)        

# 5)
# for i in range(2,10):
#     for j in range(1,10):
#         print(i,"*", j,"=",i*j)

# 6)
# def Wordcount(sentence):
#     word = sentence.split(' ')
#     dic = {}

#     for i in word:
#         wordCnt = word.count(i);
#         dic[i] = wordCnt

#     for j in dic:
#         print(j," : ",dic[j])

#     return    

# sentence = '다들 파이썬은 어떠신가요 파이썬은 나중에 다른 곳에서도 많이 쓰인답니다 파이썬은 다른 언어보다 코딩 하기 쉬워요 멋사 멋사 화이팅'
# Wordcount(sentence)

# 연습문제 - 함수
# 1)
# def is_odd(num):
#     if num%2==0:
#         print(num,"은 짝수")
#     else :
#         print(num,"은 홀수")
#     return 

# is_odd(1)

# 2)
num_list = [1,3,5,7,9]

def avg(num_list):
    avg = 0
    for i in num_list:
        avg +=i
    return avg / len(num_list)

print(avg(num_list))        