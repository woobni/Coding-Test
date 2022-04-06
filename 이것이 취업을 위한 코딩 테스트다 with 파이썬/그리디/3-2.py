# key point
# 주어진 수들을 더해서 가장 큰 수를 만들 때 연속적으로 나오는 수의 제한이 있음 
# 따라서 반복되는 수열이 나올 것

def solution()-> int:
    result = 0

    # Input N, M, K seperated by space.
    n, m, k = map(int, input().split())
    # Input N numbers seperated by space.
    data = list(map(int, input().split()))

    # Sort the number of inputs.
    data.sort()
    first = data[n-1] # the largest number
    second = data[n-2] # the second largest number

    # Caculate the number of times the largest number is added.
    count = m//(k+1) * k
    count += m%(k+1)

    result += count * first # Add the largest number
    result += (m-count) * second # Add the second largest number

    return result