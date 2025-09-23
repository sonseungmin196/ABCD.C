# NumPy 완전 학습 가이드

## 📚 목차
1. [NumPy 소개](#numpy-소개)
2. [환경 설정](#환경-설정)
3. [배열 생성과 기본 속성](#배열-생성과-기본-속성)
4. [다양한 배열 생성 방법](#다양한-배열-생성-방법)
5. [배열 인덱싱과 슬라이싱](#배열-인덱싱과-슬라이싱)
6. [배열 연산](#배열-연산)
7. [집계 함수와 축(Axis) 개념](#집계-함수와-축axis-개념)
8. [실습 코드 분석](#실습-코드-분석)
9. [핵심 개념 정리](#핵심-개념-정리)
10. [추가 학습 방향](#추가-학습-방향)

---

## NumPy 소개

### NumPy란?
**NumPy**(Numerical Python)는 파이썬에서 과학 컴퓨팅을 위한 기본 패키지입니다.

#### 주요 특징:
- **다차원 배열 객체(ndarray)**: 효율적인 메모리 사용과 빠른 연산
- **브로드캐스팅**: 다른 크기의 배열 간 연산 지원
- **벡터화 연산**: 반복문 없이 전체 배열에 대한 연산
- **선형대수, 푸리에 변환** 등 수학 함수 제공
- **C/C++, Fortran과의 통합** 가능

#### 왜 NumPy를 사용하나요?
```python
# Python 리스트 vs NumPy 배열 비교

# Python 리스트 (느림)
python_list = [1, 2, 3, 4, 5]
result = [x * 2 for x in python_list]  # 반복문 필요

# NumPy 배열 (빠름)
import numpy as np
numpy_array = np.array([1, 2, 3, 4, 5])
result = numpy_array * 2  # 벡터화 연산
```

---

## 환경 설정

### 설치
```bash
pip install numpy
```

### Import 관례
```python
import numpy as np  # 관례적으로 np로 별칭 사용
```

---

## 배열 생성과 기본 속성

### 3.1 리스트에서 배열 생성

#### 기본 생성
```python
# 1차원 배열
a = [1, 2, 3, 4, 5]
arr1d = np.array(a)
print(f"1차원 배열: {arr1d}")
print(f"타입: {type(arr1d)}")

# 2차원 배열 (행렬)
a = [[1, 2, 3], [4, 5, 6]]  # 2×3 행렬
arr2d = np.array(a)
print(f"2차원 배열:\n{arr2d}")
```

#### 출력 결과:
```
1차원 배열: [1 2 3 4 5]
타입: <class 'numpy.ndarray'>
2차원 배열:
[[1 2 3]
 [4 5 6]]
```

### 3.2 배열의 기본 속성

```python
a = [[1, 2, 3], [4, 5, 6]]
b = np.array(a)

print(f"원본 리스트: {a}")
print(f"원본 리스트 타입: {type(a)}")
print(f"NumPy 배열: {b}")
print(f"NumPy 배열 타입: {type(b)}")
print(f"배열 차원 수: {b.ndim}")
print(f"배열 모양: {b.shape}")
print(f"배열 크기: {b.size}")
print(f"데이터 타입: {b.dtype}")
```

#### 출력 결과:
```
원본 리스트: [[1, 2, 3], [4, 5, 6]]
원본 리스트 타입: <class 'list'>
NumPy 배열: [[1 2 3]
 [4 5 6]]
NumPy 배열 타입: <class 'numpy.ndarray'>
배열 차원 수: 2
배열 모양: (2, 3)
배열 크기: 6
데이터 타입: int64
```

#### 주요 속성 설명:
- **`ndim`**: 배열의 차원 수
- **`shape`**: 각 차원의 크기를 튜플로 표현
- **`size`**: 배열의 전체 원소 개수
- **`dtype`**: 배열 원소의 데이터 타입

---

## 다양한 배열 생성 방법

### 4.1 특수 배열 생성

#### 영(0) 배열
```python
# 2×2 영행렬
c = np.zeros([2, 2])
print("2×2 영행렬:")
print(c)

# 1차원 영배열 (길이 5)
d = np.zeros([5])
print("1차원 영배열:")
print(d)
```

#### 일(1) 배열
```python
# 2×2 일행렬
e = np.ones([2, 2])
print("2×2 일행렬:")
print(e)

# 3×3 일행렬
f = np.ones([3, 3])
print("3×3 일행렬:")
print(f)
```

#### 특정 값으로 채운 배열
```python
# 2×3 배열을 5로 채움
g = np.full([2, 3], 5)
print("2×3 배열 (값: 5):")
print(g)

# 4×4 배열을 3.14로 채움
h = np.full([4, 4], 3.14)
print("4×4 배열 (값: 3.14):")
print(h)
```

### 4.2 기타 유용한 생성 함수

#### 단위 행렬
```python
# 3×3 단위행렬
identity = np.eye(3)
print("3×3 단위행렬:")
print(identity)
```

#### 연속된 값 배열
```python
# 0부터 9까지
range_arr = np.arange(10)
print("0부터 9까지:", range_arr)

# 1부터 20까지 2씩 증가
range_arr2 = np.arange(1, 21, 2)
print("1부터 20까지 2씩:", range_arr2)

# 균등하게 나눈 배열
linear = np.linspace(0, 10, 5)
print("0부터 10까지 5개:", linear)
```

---

## 배열 인덱싱과 슬라이싱

### 5.1 기본 인덱싱

```python
# 2차원 배열에서 요소 접근
b = np.array([[1, 2, 3], [4, 5, 6]])

print(f"b[0, 0] = {b[0, 0]}")  # 첫 번째 행, 첫 번째 열
print(f"b[0, 1] = {b[0, 1]}")  # 첫 번째 행, 두 번째 열
print(f"b[1, 2] = {b[1, 2]}")  # 두 번째 행, 세 번째 열
```

### 5.2 고급 슬라이싱

```python
lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)
print("원본 3×3 배열:")
print(arr)
```

#### 부분 배열 추출
```python
# 첫 2행, 첫 2열 추출
a = arr[0:2, 0:2]
print("arr[0:2, 0:2]:")
print(a)
# 결과: [[1, 2], [4, 5]]

# 2행부터 끝까지, 2열부터 끝까지
b = arr[1:, 1:]
print("arr[1:, 1:]:")
print(b)
# 결과: [[5, 6], [8, 9]]

# 모든 행, 마지막 열만
c = arr[:, -1]
print("arr[:, -1]:")
print(c)
# 결과: [3, 6, 9]

# 첫 번째 행 전체
d = arr[0, :]
print("arr[0, :]:")
print(d)
# 결과: [1, 2, 3]
```

### 5.3 슬라이싱 규칙 정리

| 표현식 | 의미 |
|--------|------|
| `arr[i, j]` | i행 j열의 원소 |
| `arr[i, :]` | i행의 모든 열 |
| `arr[:, j]` | 모든 행의 j열 |
| `arr[i:j, :]` | i행부터 (j-1)행까지 |
| `arr[:, i:j]` | i열부터 (j-1)열까지 |
| `arr[i:j, k:l]` | i~(j-1)행, k~(l-1)열 |

---

## 배열 연산

### 6.1 기본 산술 연산 (요소별 연산)

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(f"a = {a}")
print(f"b = {b}")
```

#### 사칙연산
```python
# 요소별 덧셈
add_result = a + b  # 또는 np.add(a, b)
print(f"a + b = {add_result}")  # [5, 7, 9]

# 요소별 뺄셈
sub_result = a - b  # 또는 np.subtract(a, b)
print(f"a - b = {sub_result}")  # [-3, -3, -3]

# 요소별 곱셈
mul_result = a * b  # 또는 np.multiply(a, b)
print(f"a * b = {mul_result}")  # [4, 10, 18]

# 요소별 나눗셈
div_result = a / b  # 또는 np.divide(a, b)
print(f"a / b = {div_result}")  # [0.25, 0.4, 0.5]
```

### 6.2 행렬 연산

#### 행렬 곱셈 (내적)
```python
# 2×2 행렬 곱셈 예제
arr1 = [[1, 2], [3, 4]]
arr2 = [[5, 6], [7, 8]]

a = np.array(arr1)
b = np.array(arr2)

print("행렬 A:")
print(a)
print("행렬 B:")
print(b)

# 행렬의 내적 (점곱)
c = np.dot(a, b)
print("A × B (행렬 곱셈):")
print(c)

# 또는 @ 연산자 사용 (Python 3.5+)
c2 = a @ b
print("A @ B (행렬 곱셈):")
print(c2)
```

#### 계산 과정:
```
A × B = [[1×5 + 2×7, 1×6 + 2×8],
         [3×5 + 4×7, 3×6 + 4×8]]
      = [[19, 22],
         [43, 50]]
```

### 6.3 요소별 연산 vs 행렬 연산 비교

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 요소별 곱셈 (Hadamard product)
element_wise = a * b
print("요소별 곱셈 (a * b):")
print(element_wise)
# 결과: [[5, 12], [21, 32]]

# 행렬 곱셈 (Matrix multiplication)
matrix_mult = np.dot(a, b)
print("행렬 곱셈 (np.dot(a, b)):")
print(matrix_mult)
# 결과: [[19, 22], [43, 50]]
```

---

## 집계 함수와 축(Axis) 개념

### 7.1 기본 집계 함수

```python
a = np.array([[-1, 2, 3], [3, 4, 8]])
print("원본 배열:")
print(a)
```

#### 전체 배열에 대한 집계
```python
# 전체 합계
total_sum = np.sum(a)  # 또는 a.sum()
print(f"전체 합계: {total_sum}")  # 19

# 기타 집계 함수들
print(f"평균: {np.mean(a)}")      # 3.1666...
print(f"최대값: {np.max(a)}")      # 8
print(f"최소값: {np.min(a)}")      # -1
print(f"표준편차: {np.std(a)}")     # 2.9277...
```

### 7.2 축(Axis) 개념 이해

NumPy에서 **axis**는 배열의 차원을 나타냅니다.

#### 2차원 배열에서의 축:
```
배열: [[-1,  2,  3],
       [ 3,  4,  8]]

axis=0 (행 방향): ↓
axis=1 (열 방향): →
```

#### 축별 집계 연산
```python
a = np.array([[-1, 2, 3], [3, 4, 8]])

# axis=0: 행 방향으로 집계 (각 열의 합)
sum_by_col = a.sum(axis=0)
print(f"각 열의 합 (axis=0): {sum_by_col}")  # [2, 6, 11]

# axis=1: 열 방향으로 집계 (각 행의 합)
sum_by_row = a.sum(axis=1)
print(f"각 행의 합 (axis=1): {sum_by_row}")  # [4, 15]
```

#### 시각적 이해:
```python
# axis=0 계산 과정:
# 열 0: -1 + 3 = 2
# 열 1:  2 + 4 = 6
# 열 2:  3 + 8 = 11
# 결과: [2, 6, 11]

# axis=1 계산 과정:
# 행 0: -1 + 2 + 3 = 4
# 행 1:  3 + 4 + 8 = 15
# 결과: [4, 15]
```

### 7.3 다양한 집계 함수들

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 다양한 축별 집계
print("원본 배열:")
print(a)

print("\n각 함수별 결과:")
print(f"합계 (전체): {np.sum(a)}")
print(f"합계 (axis=0): {np.sum(a, axis=0)}")
print(f"합계 (axis=1): {np.sum(a, axis=1)}")

print(f"\n평균 (전체): {np.mean(a)}")
print(f"평균 (axis=0): {np.mean(a, axis=0)}")
print(f"평균 (axis=1): {np.mean(a, axis=1)}")

print(f"\n최대값 (axis=0): {np.max(a, axis=0)}")
print(f"최대값 (axis=1): {np.max(a, axis=1)}")

print(f"\n최소값 (axis=0): {np.min(a, axis=0)}")
print(f"최소값 (axis=1): {np.min(a, axis=1)}")
```

---

## 실습 코드 분석

### 8.1 numpy study1.py 분석

```python
# -*- coding: utf-8 -*-
import numpy as np  # numpy 패키지 로드하여 np로 사용

# 리스트에서 행렬 생성
a = [[1, 2, 3], [4, 5, 6]]  # 2차 행렬
b = np.array(a)

# 타입 비교
print(a)          # [[1, 2, 3], [4, 5, 6]]
print(type(a))    # <class 'list'>
print(b)          # [[1 2 3] [4 5 6]]
print(type(b))    # <class 'numpy.ndarray'>

# 배열 속성 확인
print(b.ndim)     # 2 (차원 수)
print(b.shape)    # (2, 3) (행, 열)

# 요소 접근
print(b[0, 0])    # 1
print(b[0, 1])    # 2

# 다양한 배열 생성
c = np.zeros([2, 2])    # 2×2 영행렬
d = np.zeros([5])       # 길이 5인 1차원 영배열
e = np.ones([2, 2])     # 2×2 일행렬
f = np.full([2, 3], 5)  # 2×3 배열을 5로 채움
```

### 8.2 numpy study2.py 분석 (슬라이싱)

```python
# 3×3 배열 생성
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(lst)

# 부분 배열 추출
a = arr[0:2, 0:2]  # 첫 2행, 첫 2열
print(a)           # [[1 2] [4 5]]

b = arr[1:, 1:]    # 2행부터 끝, 2열부터 끝
print(b)           # [[5 6] [8 9]]
```

### 8.3 numpy study3.py 분석 (연산)

```python
# 1차원 배열 연산
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 요소별 덧셈
c = a + b          # [5 7 9]
# c = np.add(a, b)  # 동일한 결과

# 요소별 나눗셈
c = np.divide(a, b)  # [0.25 0.4 0.5]

# 2차원 배열 행렬 곱셈
arr1 = [[1, 2], [3, 4]]
arr2 = [[5, 6], [7, 8]]
a = np.array(arr1)
b = np.array(arr2)

c = np.dot(a, b)   # [[19 22] [43 50]]
print(c)
```

### 8.4 numpy matrix.py 분석 (집계)

```python
# 집계 함수 사용
a = np.array([[-1, 2, 3], [3, 4, 8]])

# 전체 합계
s = np.sum(a)
print('sum=', a.sum())  # sum= 19

# 축별 합계 (주의: 원본 코드에 오타가 있었음)
print('sum by row=', a.sum(axis=0))  # 각 열의 합: [2 6 11]
print('sum by col=', a.sum(axis=1))  # 각 행의 합: [4 15]
```

---

## 핵심 개념 정리

### 9.1 배열 vs 리스트

| 구분 | Python 리스트 | NumPy 배열 |
|------|---------------|------------|
| **타입** | `<class 'list'>` | `<class 'numpy.ndarray'>` |
| **메모리** | 비효율적 | 효율적 |
| **연산** | 반복문 필요 | 벡터화 연산 |
| **타입 혼합** | 가능 | 단일 타입만 |
| **수학 연산** | 제한적 | 풍부한 함수 |

### 9.2 배열 생성 방법 요약

| 함수 | 용도 | 예시 |
|------|------|------|
| `np.array()` | 기존 데이터 변환 | `np.array([1,2,3])` |
| `np.zeros()` | 영배열 생성 | `np.zeros([3,3])` |
| `np.ones()` | 일배열 생성 | `np.ones([2,4])` |
| `np.full()` | 특정값 배열 | `np.full([2,2], 7)` |
| `np.eye()` | 단위행렬 | `np.eye(3)` |
| `np.arange()` | 연속값 배열 | `np.arange(0,10,2)` |

### 9.3 연산 종류

#### 요소별 연산 (Element-wise)
- `+`, `-`, `*`, `/`: 같은 위치의 원소끼리 연산
- 배열의 크기가 같아야 함 (브로드캐스팅 제외)

#### 행렬 연산 (Linear Algebra)
- `np.dot(a, b)` 또는 `a @ b`: 행렬 곱셈
- 첫 번째 행렬의 열 수 = 두 번째 행렬의 행 수

#### 집계 연산 (Aggregation)
- `sum`, `mean`, `max`, `min`, `std` 등
- `axis` 매개변수로 축 지정 가능

### 9.4 축(Axis) 개념 마스터

```python
# 2D 배열에서
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# axis=0: "행을 따라" = 세로 방향 = 각 열에 대해
arr.sum(axis=0)  # [5, 7, 9] (각 열의 합)

# axis=1: "열을 따라" = 가로 방향 = 각 행에 대해  
arr.sum(axis=1)  # [6, 15] (각 행의 합)
```

#### 기억법:
- **axis=0**: 행 인덱스가 변하는 방향 (세로 ↓)
- **axis=1**: 열 인덱스가 변하는 방향 (가로 →)

---

## 추가 학습 방향

### 10.1 다음 단계 NumPy 기능들

#### 브로드캐스팅 (Broadcasting)
```python
# 크기가 다른 배열 간 연산
a = np.array([[1, 2, 3],
              [4, 5, 6]])  # (2, 3)
b = np.array([10, 20, 30])  # (3,)

result = a + b  # 브로드캐스팅 발생
# 결과: [[11, 22, 33],
#        [14, 25, 36]]
```

#### 배열 형태 변환
```python
# reshape: 배열 모양 변경
a = np.arange(12)
b = a.reshape(3, 4)  # 1D → 2D

# flatten: 다차원 → 1차원
c = b.flatten()

# transpose: 전치
d = b.T
```

#### 조건부 선택
```python
# 불린 인덱싱
a = np.array([1, 2, 3, 4, 5])
mask = a > 3
result = a[mask]  # [4, 5]

# where 함수
result = np.where(a > 3, a, 0)  # [0, 0, 0, 4, 5]
```

### 10.2 실무 활용 예시

#### 데이터 분석
```python
# 통계 분석
data = np.random.normal(100, 15, 1000)  # 평균100, 표준편차15
print(f"평균: {np.mean(data):.2f}")
print(f"표준편차: {np.std(data):.2f}")
print(f"중앙값: {np.median(data):.2f}")
```

#### 이미지 처리
```python
# 이미지는 3D 배열 (높이, 너비, 채널)
# 예: (224, 224, 3) = 224×224 픽셀, RGB 3채널
image = np.random.randint(0, 256, (224, 224, 3))
```

#### 머신러닝
```python
# 특성 정규화
features = np.array([[1, 2], [3, 4], [5, 6]])
normalized = (features - np.mean(features, axis=0)) / np.std(features, axis=0)
```

### 10.3 성능 최적화 팁

1. **벡터화 사용**: 반복문 대신 NumPy 함수 활용
2. **메모리 효율성**: 적절한 dtype 선택
3. **브로드캐스팅 활용**: 크기가 다른 배열 간 연산
4. **인플레이스 연산**: `+=`, `*=` 등으로 메모리 절약

---

## 📝 연습 문제

### 문제 1: 기본 배열 조작
1. 1부터 12까지의 수로 3×4 배열을 만드세요
2. 이 배열의 두 번째 행을 추출하세요
3. 마지막 열을 추출하세요

### 문제 2: 배열 연산
1. 두 개의 2×2 행렬을 만들고 요소별 곱셈을 하세요
2. 같은 행렬들의 행렬 곱셈을 하세요
3. 결과의 차이를 설명하세요

### 문제 3: 집계 함수
1. 4×3 랜덤 배열을 생성하세요
2. 각 행의 평균을 구하세요
3. 각 열의 최대값을 구하세요

---

이 문서는 NumPy의 기초부터 실전 활용까지 체계적으로 정리한 완전한 학습 가이드입니다. 각 개념을 단계별로 학습하고 실습을 통해 익히시면 NumPy를 효과적으로 활용할 수 있을 것입니다!