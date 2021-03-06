from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls')),
]

'''
URL은 정규표현식을 이용하여 등록한다 

파이썬에서 정규 표현식을 작성할 때는 항상 문자열 앞에 (r)을 붙입니다. 이는 파이썬에게는 별 의미가 없지만, 파이썬에게 문자열에 특수 문자를 있다는 것을 알려줍니다.

^: 문자열(정규표현식) 시작
$: 문자열(정규표현식) 끝
\d : 숫자 
\D : 숫자가 아님을 뜻하며 [^0-9]와 동일 
\w : 밑줄 문자를 포함한 영숫자 문자에 일치 [^A-Za-z0-9_]와 동일
[xyz] : 문자셋 
        문자셋
        이 패턴 타입은 괄호 안의 이스케이프 시퀀스를 포함한 어떤 한 문자에 일치
        이 안에서는 점(.) 이나 별표 (*) 같은 문자가 특별한 효과를 지니지 않음
        하이픈을 이용한 범위 지정
        예제 :
        [ᄀ-힣] : 한글 한 글자
        [1-9] : 숫자 1에서 9까지 한 글자
        [012] : 0 또는 1 또는 2 한 글자
        [acd] : a 또는 c 또는 d 한 글자
        [a-zA-Z] : 알파벳 대소문자 한글자
        
[^xyz] 괄호안에 포함되지 않는 문자
{n} : 앞문자가 n번 나타나면 일치
예제 :
\d{5} : 숫자 5번 나타나면 일치
010[1-9]\d{7} : 휴대폰 번호

{min, max} :
min과 max는 양의 정수
min < max
앞의 문자가 최소 min개, 최대 max개
max가 생략될 시 무한으로 취급
예제 :
\d{1,5} : 숫자가 최소 1개에서 최대 5개
[ᄀ-힣]{1,3} : 한글 최소 1글자에서 최대 3글
* : 0회 이상 연속으로 반복되는 앞선 문자에 일치합니다. {0,} 와 동일합니다.
+ : 1회 이상 연속으로 반복되는 앞선 문자에 일치합니다. {1,} 와 동일합니다.
? : 0 또는 1회 반복되는 앞선 문자에 일치합니다. {0,1}와 동일합니다.
. : (소수점) 다음 줄 문자(개행 문자)를 제외한 어떤 하나의 문자에 일치합니다.

2. 주요 정규표현식
정수 : \d+
이메일 : [0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}
휴대폰 : 010[1-9]\d{7}
전화번호: \d{3}-\d{3,4}-\d{4}        
        
       참고 url : https://suwoni-codelab.com/django/2018/03/24/Django-Regular-expression/
        
'''
