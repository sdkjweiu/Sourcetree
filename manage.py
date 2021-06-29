from app import create_app      #from app --> __init__ : __init__.py가 속해있는 폴더 이름으로 불러올 수 있다, app폴더 = __init__, *파이썬 약속---manage.py

app = create_app('default')

if __name__ == '__main__':
    app.run()

# __name__ ==> d:\sourcetree\manage.py
# __main__ ==> cmd 직접 실행할때 디렉토리