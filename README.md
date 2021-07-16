# teamJava



pip install django
pip install pymysql
pip install boto3
pip install django-storages

#WorkBench 실행 완료 및  Setting host, name 작성후
python manage.py migrate

#WorkBench 데이터 들어감
python manage.py createsuperuser

#Setting aws 관련 설정
#STATICFILES_DIRS = (os.path.join('static'), )
python manage.py collectstatic

#Setting 설정
#-app storages 입력
#-DEFAULT_FILE_STORAGE = 'config.asset_storage.MediaStorage' 입력
#asset_storage.py 생성

#startapp taste 생성
#setting 설정

#모델 입력 후
pip install pillow

python manage.py makemigrations taste
python manage.py migrate

#setting base template 입력
#template 폴더 생성 및 입력


