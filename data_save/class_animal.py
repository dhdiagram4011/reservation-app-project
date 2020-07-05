class Animal:
    name = ""

    def __init__(self, name): ##함수
        self.name = name

    def bark(self):
        print('...')


class Box:
    inside = None

    def __str__(self):
        if self.inside is None:
            return 'What would you place in Box'
        else:
            return f'Contents of Box: {self.inside}'

    def pretty(self):
        box =  Box(self)
        print(box.inside)

    def __init__(self, name, inside=None):
        self.name = name
        self.insde = inside

    def query(self):
        self.inside = input('인사이드를 입력하세요')

    def put(self, something):
       self.inside = something


    def retrive(self):
        return self.inside


#self 를 통해서 내가 어떠한 인스턴스에 속해 있는지 알 수 있음 - 인스턴스안에서 내가 어떠한 인스턴스에 속해 있는지 구븐하기 위해서필요

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(self.name, '왈왈')

dog = Dog('a')
print(dog.name)
dog.bark()


class Cat(Dog):

    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        print(self.name, '야옹')

cat = Cat('a')
print(cat.name)
cat.bark()


#@property - 변수에 접근하기 위한 함수의 모임들
## 내부에 있는 변수를 참조하기 위한 모임, getter, setter
# 직접적으로 변수에 접근을 하지 못하게 함

#optional arg = 있어도 되고 없더도 되는 파라미터 
# def test(a,b,c d='', e='' --> d/e = optional , a,b,c = positional)


#python에서 private은 실제로 동작하지 않음

#[1:-1] = 문자열에서 값을 앞뒤로 하나씩 뺌

"""
hasattr = dir 에서 나오는 것들이 있는지 없는지 보여줌
리스트 = mutable 한 객체 - 변경이 가능함
mutable = 기존 메모리를 이용
emutable  = 새로운 메모리에 값을 할당함
string , int ..  = emutable
0 ~ 255 까지는 값이 미리 지장되어 있기 때문에 메모리 값이 바뀌지 않음 (0 ~ 255 사이의 값에 대한 + 를 하면)


추가적인 내용을 함수에 덮어 쓰고 싶을때 데코레이터를 이용 - 의존성 주입목적

# log , 인증 ... 데코레이터는 함수
# 함수 , 클레스 모두 가능
# 
# def first_decorator(func): - 데코리아터가 ㅇㅇ
#   print("call function")
    def wrapper(*arg, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

def test(name):
    print(name)

test('test')

데코레이터  - 함수를 감싸는 함수

함수를 변경히지 않고 기능을 추가히고 싶을때 --> 데코레이터 이용

@wraps

OOP - Object Oriented Programing

면접
절차지향 - 구조지향

"""
