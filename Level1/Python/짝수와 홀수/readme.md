# [Level1] 짝수와 홀수 (Python)

### 문제 설명
정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

### 제한사항
- num은 int 범위의 정수입니다.
- 0은 짝수입니다.

### 입출력 예
|num|return|
|---|---|
|3|"Odd"|
|4|"Even"|

## Solution
```python
def solution(num):

    return "Even" if num % 2 == 0 else "Odd"
```

### 코드 설명
- 삼항연산자(ternary operator): `true_value` if `condition` else `false_value`