# [Level1] 행렬의 덧셈 (python)

### 문제 설명
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

### 제한 조건
행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

### 입출력 예
|arr1|arr2|answer|
|---|---|---|
|[[1,2],[2,3]]|[[3,4],[5,6]]|[[4,6],[7,9]]|
|[[1],[2]]|[[3],[4]]|[[4],[6]]|

## Solution
```python
import numpy as np

def solution(arr1, arr2):
    
    return (np.array(arr1) + np.array(arr2)).tolist()
```

### 코드 설명
- `numpy`: 행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
- `np.array(리스트)`: array 함수에 리스트를 넣으면 ndarray 클래스 객체로 변환해 준다.
- `tolist()`: ndarray 객체를 리스트로 변환