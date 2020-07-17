# 항공권 예약 웹 어플리케이션 

### 프로젝트(어플리케이션 구성)
    - Python 3.7
    - Django 2.1.5
    - Nginx
    - Gunicorn
    - SQLite
    - Python Anaconda

### 프로젝트(배포구조)
    - GCP VM Instance
    - Docker Hub: Image Repository (https://hub.docker.com/repository/docker/dhdiagram/ticket-app-develop)
    - Jenkins 


### Source Code Structure
    Django == 2.1.5
    |
    |___reservation_project(프로젝트 명)
        |
        |__reservation(app) - 예약, 예약확인, 예약내역, 예약취소, 날짜별 운항스케쥴 조회
        |__authentication(app) - 회원가입, 회원탈퇴, 회원별 예약정보, 회원리스트


### Application production structure
![Sturcture](https://user-images.githubusercontent.com/50344658/87245571-45da9680-c481-11ea-86cc-39ac2ccc3325.jpg)


### Application production structure Step
    1. 로컬에서 소스코드 github로 업로드
    2. 어플리케이션 이미지 생성을 위한 Dockerfile build 
    3. Image Repository(Docker Hub)로 이미지 push (v0.1 ~)
    4. GCP VM Instance로 배포 (Jenkins)


### 어플리케이션 Preview(미리보기)

##### 1.회원가입,로그인
[![클릭시 유투브로 이동합니다](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/DsrXO8n4UZg)


##### 2.항공권예약하기
[![클릭시 유투브로 이동합니다](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/F0ADVSvMrIY)


##### 3.출발일 기준 항공권 조회
[![클릭시 유투브로 이동합니다](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/-_Rx5qO1N0c)


### DemoSite(제작중)
    - 관리자페이지 : demo.dhdiagram.me/admin - 아이디, 패스워드로 접근 가능 (구현완료)
    - 회원가입 : demo.dhdiagram.me/auth/register/ (구현완료)
    - 로그인 : demo.dhdiagram.me/auth/login/ (구현중 - 90% 진행)
    - 로그아웃 : demo.dhdiagram.me/auth/logout/ (구현중)
    - 회원정보보기 : demo.dhdiagram.me/auth/myinfo/ (구현중 - 90% 진행)
    - 회원정보수정 : demo.dhdiagram.me/auth/edit/ (구현중 - 90% 진행)
    - 회원탈퇴 : demo.dhdiagram.me/auth/unregister/ (구현완료)
    - 항공권 예매 : demo.dhdiagram.me/reservation/revstart/ (구현완료)
    - 항공권 검색결과 조회 : demo.dhdiagram.me/reservation/course_search/ (구현완료)    
    - 출발일 기준 항공권 조회 : demo.dhdiagram.me/reservation/date_search/ (구현완료)
    - 출발일 기준 항공권 조회 결과 : demo.dhdiagram.me/reservation/date_search_result/ (구현완료)
    - 예약내역 조회 : demo.dhdiagram.me/reservation/ticketing_list/ (구현중 - 90% 완료)


### Django 버전
    Django == 2.1.5
    virtualenv : Python Anaconda


### 설치 및 실행 방법
    git clone ${git url}
    cd reservation_project
    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser : superadmin 계정 생성
    python3 manage.py runserver 0.0.0.0:80
       

### 어플리케이션 사용법
    - 관리자페이지 : /admin - 아이디, 패스워드로 접근 가능
    - 회원가입 : /auth/register/
    - 로그인 : /auth/login/
    - 회원정보보기 : /auth/myinfo/
    - 회원정보수정 : /auth/edit/
    - 회원탈퇴 : /auth/unregister/
    - 항공권 예매 : /reservation/revstart/
    - 항공권 검색결과 조회 : /reservation/course_search/    
    - 출발일 기준 항공권 조회 : /reservation/date_search/
    - 출발일 기준 항공권 조회 결과 : /reservation/date_search_result/


### 어플리케이션 배포
    Jenkins를 이용한 어플리케이션 배포 스크립트 
    -
    Jenkins 접속 : localhost:9100
    cd /app
    source ~/.bashrc
    conda activate ticket-app-develop
    rm -rf *
    git clone -b develop https://github.com/dhdiagram4011/reservation-app-project.git
    cd reservation-app-project
    mv * ../
    cd /app
    touch jenkins.initial
    rm -rf reservation-app-project
    pip install pylint
    pip install autopep8
    pip install django==2.1.5
    pip install gunicorn
    pip install mysqlclient
    pip install pymysql
    python manage.py makemigrations
    python manage.py migrate 
    systemctl restart ticketapp
    systemctl restart nginx


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

    김도형(dohyoung Kim)
    Email : dhdiagram@gmail.com
    DemoSite : ing ... 

