# 내풀이
# 학생 수 N 입력받기
n = int(input())
# 학생의 이름과 성적 입력받기
dict = {}
for i in range(n):
    name, score = input().split(' ')
    dict[name] = int(score)

# value값을 기준으로 정렬한 key "리스트"를 반환
sorted_dict = sorted(dict, key=lambda x :dict[x])

for i in range(len(sorted_dict)):
    print(sorted_dict[i], end=' ')


# 교재 풀이
# N 을 입력받기
n = int ( input ())
# N 명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range ( n ):
    input_data = input (). split () # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[ 0 ], int( input_data [ 1 ])))

# 키( Key )를 이용하여, 점수를 기준으로 정렬
array = sorted ( array , key = lambda student : student [ 1 ])

# 정렬이 수행된 결과를 출력
for student in array :
    print( student [ 0 ], end = ' ')