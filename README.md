<img src="https://user-images.githubusercontent.com/59287328/73450168-33274600-43a8-11ea-8c05-f699a73f562f.png" width="100%">

# Cambridge-Dictionary-Miner
Cambridge Dictionary 영어 사전 웹 크롤링 라이브러리

* 캠브리지 영어 사전 크롤링
* 캡챠 우회 없음

### 예시)
```
"miner" 라고 검색하였을 때 (검색 결과 1개)
[
  { 
    'origin': 'miner', 
    'word': 'miner', 
    'pos': 'noun', 
    'mean': '광부',
    'UKpron': 'ˈmaɪ·nər', 
    'USpron': 'ˈmɑɪ·nər'
  }
]
```

```
"can" 라고 검색하였을 때 (검색 결과 2개)
[
{
  'origin': 'can',
  'word': 'can', 
  'pos': 'modal verb',
  'mean': '(능력)-할 수 있다,(부탁)-해도 괜찮습니까?,(공손하게 도움을 요청할때)-해 줄 수 있으십니까?,(허락)-해도 된다', 
  'UKpron': 'kæn', 
  'USpron': 'kæn'
}, 
{
    'origin': 'can',
    'word': 'can', 
    'pos': 'noun', 
    'mean': '통조림,캔', 
    'UKpron': 'kæn', 
    'USpron': 'kæn'
  }
]
```
### JSON 설명서 
* origin: 원래의 단어
* word: 검색된 단어
* pos: 형태소
* mean: 의미
* UKpron: 영국식 발음
* USpron: 미국식 발음

### 개발 라이브러리
* 파이썬

### 활용 예시
* 영어 단어장 웹 서비스의 일부 영어 단어 해석에 사용
* JSON 파일로 DB에 저장

### 패키지 리스트
![PackgeList](https://user-images.githubusercontent.com/59287328/73455986-67a0ff00-43b4-11ea-8233-8d6ee7c58de8.png)
