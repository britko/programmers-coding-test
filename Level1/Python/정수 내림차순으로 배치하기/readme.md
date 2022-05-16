# [Level1] 정수 내림차순으로 배치하기 (Python)

### 문제 설명
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.



### 제한사항
- `n`은 1이상 8000000000 이하인 자연수입니다.

### 입출력 예
|n|return|
|---|---|
|118372|873211|

## Solution
```python
def solution(n):
    list_n = list(str(n))
    list_n.sort(reverse=True)
    
    return int(''.join(list_n))
```

### 코드 설명
1. n을 문자열로 만들고 리스트로 쪼갠다.
2. `sort`함수를 사용해 내림차순 옵션`(reverse=True)`으로 정렬한다.
3. 공백없이 정렬된 리스트를 join하고 int형으로 변환한다.