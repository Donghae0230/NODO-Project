#  NODO PROJECT🌊

(2022.02.14 - 2022.02.25)

베스트셀러는 시대를 반영한다고 합니다. 코로나 19 속에서 사람들은 어떤 책을 집어들었을까요? 또 오랜 '집콕생활'을 통해 독서라는 취미를 가지게된 사람들에게 우리는 어떤 책을 추천해줄 수 있을까요? ***NODO PROJECT*** 에서는

  

1) 책에 대한 애정을 담아 데이터를 분석하고

2) 데이터를 사용해 책 추천 서비스 NODO를 만들었습니다.

  

❕자세한 프로젝트 내용과 결과, 회고는 [블로그](https://donghae0230.tistory.com/127)에 작성해두었습니다.
<br/>

  

###  🙋‍♂️사용 데이터

---

온라인 서점 사이트 알라딘의 상품 데이터 [Open API](https://docs.google.com/document/d/1mX-WxuoGs8Hy-QalhHcvuV17n50uGI2Sg_GHofgiePE/edit) 활용

- 약 1만 건의 베스트셀러 도서

- 국제 표준 도서번호 ISBN, 제목, 지은이, 세부 카테고리, 가격, 출간일, 상품설명, 책 표지 URL, 상품 URL, 세일즈포인트 사용

- 데이터 전처리 후 PostgreSQL DB에 저장
<br/>

  
  

##  🙋‍♂️ 1) 데이터 시각화 및 분석

<a href="https://ibb.co/xFWdwB8"><img src="https://i.ibb.co/3R2QVjY/image.png" alt="image" border="0"></a>

<br/>

##  🙋‍♂️ 2) 책 추천 서비스 NODO

- Gensim 패키지의 word2vec모델을 사용한 컨텐츠 기반 추천 시스템 구현

- 사용자 데이터와 도서 명을 입력하면 6권의 책 추천

<br/> 

## 🛠 기능 개선
- `2022.04.28 사용자 입력 나이 제한 추가(0-100세)` 
- `2022.04.29 제목 입력시 데이터 베이스 검색에서 알라딘 API 검색으로 변경`
<br/>

[NODO에서 책 추천받기](https://nodobooks.herokuapp.com/)
  
<a href="https://ibb.co/rk01rqZ"><img src="https://i.ibb.co/7vC6mBG/image.png" alt="image" border="0"></a>