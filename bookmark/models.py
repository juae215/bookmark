from django.db import models #데어터베이스 관리 중간자역할
from django.urls import reverse
# 데이터베이스를 sql 없이 다루기 위해
# 데이터를 객채화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드(변수) = 테이블의 컬럼
#인스텐스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값

# 데이터베이스에 뭔가를 저장하고 싶다면 모델을 만든다

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100) # 글자, 100글자까지
    url =models.URLField('Site URL')

    # 필드이 종류가 결정하는 것
    # 1. 데이터베이스 컬럼 종류
    # 2. 제약사항 (몇글자까지)
    # 3. Form의 종로
    # 4. Form에서의 제약 사항


    #목록에 출력
    def __str__(self):  #앞뒤로 언더바가 두개씩 있으면 매직메서드 - 용도가 정해져있음
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(Self):
        return reverse('defail',args=[(self.id)])

#모델을 만들었다 -> 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정
#마이그레이션 (migrate)->데이터베이스 모델의 내용을 반영(테이블생성)

#makemigrations -> 모델의 변경사항을 추적해서 기록