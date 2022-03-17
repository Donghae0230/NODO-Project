# Book_recommendation
알라딘 베스트 셀러 데이터를 활용한 책 추천 웹 어플리케이션 개발

(❕자세한 프로젝트 내용과 결과, 회고는 [블로그](https://donghae0230.tistory.com/127)에 작성해두었습니다.)

### 🙋‍♂️사용 데이터
---
온라인 서점 사이트 알라딘의 상품 데이터 [Open API](https://docs.google.com/document/d/1mX-WxuoGs8Hy-QalhHcvuV17n50uGI2Sg_GHofgiePE/edit) 활용
- 약 1만 건의 베스트셀러 도서 
- 국제 표준 도서번호 ISBN, 제목, 지은이, 세부 카테고리, 가격, 출간일, 상품설명, 책 표지 URL, 상품 URL, 세일즈포인트 사용
- 전처리 후 PostgreSQL DB에 저장

👉 **데이터 시각화 및 해석**은 [ipynb 파일](https://github.com/Donghae0230/Book_recommendation/blob/master/CodeStates_project1.ipynb)에서 확인
> 시대별 도서 카테고리(대분류)의 트렌드가 있을까?
>
> 2000년대 이후 카테고리(대분류) 별 출시량 대비 salepoint 추이는 어떨까?
> 
> 소설/시/희곡(대분류)에서 시대별로 가장 사랑받은 카테고리(중분류)는 무엇일까?
> 
> 경제경영(대분류)의 중분류 출판량은 시대별로 어떻게 변화했을까?
> 
> 소설/시/희곡에서 시대별로 가장 사랑받은 출판사는 어디일까?

### 🙋‍♂️결과물
---
- Gensim 패키지의 word2vec모델을 사용한 컨텐츠 기반 추천 시스템 구현
- 사용자 데이터(이름, 나이, 성별, 좋아하는 책)을 입력하면 6권의 책 추천
- 입력된 사용자 데이터는 DB에 저장되도록 구현 
- 파이썬 웹 프레임워크 Flask를 사용해 웹 앱 개발 및 Heroku를 사용해 배포

[당신을 위한 여섯 권의 📚 확인하기](http://sixbooks.herokuapp.com/)

![image](https://user-images.githubusercontent.com/53463067/158841263-1bedf1a9-cf23-4944-8ca3-29be4a078c49.png)
