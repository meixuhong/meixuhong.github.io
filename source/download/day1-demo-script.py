# 学习笔记
# 1) 安装Flask-Script模块后，可以在终端命令行中启动flask。  $ python demo.py runserver -h 0.0.0.0 -p 5000 -d  # -d表示debug
# 2) $ python demo.py shell   # 进入交互式python环境,并且自动导入demo.py中的内容。
# 3) 使用manager = Manager(app)来定义一个管理对象管理Flask的对象app，在主函数中app.run()要改为manager.run(),因为以前是flask对象现在是Manager对象
from flask import Flask
# 导入Flask命令行扩展模块Manager,需要pip install Flask-Script
from flask_script import Manager

# 当调用app = Flask(_name_)的时候，创建了Flask程序应用对象app
app = Flask(__name__)

# 定义一个Manager对象manager,传入参数app，即manager具备使用对Flask对象直接管理功能
manager = Manager(app)

# 使用装饰器，设置app的路由
@app.route('/')
def homepage():
    return 'This is the homepage.'

@app.route('/test/<int:id>')
def test(id):
    return 'test number is %d' %id

# __name__ 是当前模块名，当模块被直接运行时模块名为 __main__, 即是说，当运行该demo.py模块时，执行下面的命令
if __name__ == '__main__':
    # 需要改为manager来管理，而不是app本身管理
    # app.run(debug=True)
    manager.run()