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
    - Jenkins를 이용한 어플리케이션 배포 스크립트 
    """
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
    """


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

