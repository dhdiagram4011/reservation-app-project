# 항공권 예약 사이트 

## 프로젝트 정보


### 설치 및 실행 방법
    
    git clone ${git url}
    cd reservation_project
    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser : superadmin 계정 생성
    python3 manage.py runserver 0.0.0.0:80
       


### 사용법
    - 관리자페이지 : /admin - 아이디, 패스워드로 접근 가능
    - 회원가입 : /auth/register/
    - 로그인 : /auth/login/
    - 회원정보보기 : /auth/myinfo/
    - 회원탈퇴 : /auth/unregister/
    - 항공권 예매 : /reservation/revstart/
    - 항공권 검색결과 조회 : /reservation/course_search/    
    - 출발일 기준 항공권 조회 : /reservation/date_search/
    - 출발일 기준 항공권 조회 결과 : /reservation/date_search_result/


### 관리자 페이지 이용방법(관리자가 비행기 티켓 일정을 추가)
    Step1) http://localhost/admin 접속
    Step2) createsuperuser 로 생성한 아이디 / 패스워드로 로그인
    Step3) http://localhost/admin/reservation/flightsection/ 주소로 접근
    Step4) 우측상단의 "FLIGHT SECTIONS 추가 +" 버튼 클릭하여 조건에 맞게 데이터 입력 


### 관리자 페이지 이용방법(관리자가 티켓 가격을 추가)
    Step1) http://localhost/admin 접속
    Step2) createsuperuser 로 생성한 아이디 / 패스워드로 로그인
    Step3) http://localhost/admin/reservation/price/add 주소로 접근
    Step4) 우측상단의 "PRICE 추가 +" 버튼 클릭하여 조건에 맞게 데이터 입력(Peak Season Price, Low Season Price로 구분하여 가격입력 가능)



## Contribute


## License

MIT lisence(dhdiagram@gmail.com)

## 개발자 정보

    김도형(dohyoung Kim)<br/>
    Email : dhdiagram@gmail.com<br/>
    DemoSite : ing ...<br/>

