# 문자열 방식
def solution(n):
    
    return sum([int(i) for i in str(n)])


# 재귀 방식
# def solution(n):
#     if number < 10:
#         return number;
#     return (number % 10) + solution(number // 10)