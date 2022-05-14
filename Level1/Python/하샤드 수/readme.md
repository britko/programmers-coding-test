# [Level1] 하샤드 수 (Python)

### 문제 설명
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

### 제한 조건
x는 1 이상, 10000 이하인 정수입니다.

### 입출력 예
|arr|return|
|---|---|
|10|true|
|12|true|
|11|false|
|13|false|

## Solution
```python
def solution(x):
    
    return x % sum([int(i) for i in str(x)]) == 0
```

### 코드 설명
1. List Comprehesions(리스트 표현식)으로 각 자릿수를 구한다.
2. `sum` 함수로 자릿수를 모두 더한다.
3. 양의 정수 x가 자릿수의 합으로 나눠지면 True, 아니면 False를 반환한다.