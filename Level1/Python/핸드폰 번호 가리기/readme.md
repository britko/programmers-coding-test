# [Level1] 핸드폰 번호 가리기 (Python)

### 문제 설명
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 `*`으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

### 제한 조건
phone_number는 길이 4 이상, 20이하인 문자열입니다.

### 입축력 예
|phone_number|return|
|---|---|
|"01033334444"|"*******4444"|
|"027778888"|"*****8888"|

## Solution
```python
def solution(phone_number):
    
    answer = '*' * len(phone_number[:-4]) + phone_number[-4:]
    
    return answer
```

### Explanation
- 음수 인덱스를 지정해 뒤에서 4번쩨 요소를 제외한 나머지를 *로 변환
![slice](https://github.com/britko/programmers-coding-test/blob/master/Level1/Python/%ED%95%B8%EB%93%9C%ED%8F%B0%20%EB%B2%88%ED%98%B8%20%EA%B0%80%EB%A6%AC%EA%B8%B0/images/1.png)