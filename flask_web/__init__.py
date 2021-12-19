# __init__.py

from flask import Flask, render_template
from flask_web.routes import user_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_routes.bp)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    #main이라는 폴더에 'main.html' 파일이 존재한다면 이렇게 작성
    @app.route('/main')
    def main():
      return render_template('main/main.html')

    @app.route('/read')
    def index():
        return '''
            <html>
            <head>
                <title>
                HTML Page
                </title>
            </head>
            <body>
                <h1>Writing HTML...</h1>
            </body>
            </html>
            '''
    #templates이라는 폴더에 index.html이라는 파일을 사용하고 싶다면
    @app.route('/render')
    def index_part():
        return render_template('index.html')
    
    @app.route('/fruit')
    def hear():
        apple = 'red'
        apple_count = 10
        # return render_template('jinja.html', fruit_color=apple)
        return render_template('jinja.html', fruit_color=apple, number=apple_count)
    
    @app.route('/nav')
    def no_matter():
        apple = 'red'
        apple_count = 10
        # return render_template('jinja.html', fruit_color=apple)
        return render_template('navbar.html', fruit_color=apple, number=apple_count)
    
    @app.route('/boot')
    def matter():
        return render_template('source.html')

    return app
#------------------------------------------------------------------
# def create_app():
#     app = Flask(__name__)

#     from yourapplication.views.admin import admin
#     from yourapplication.views.frontend import frontend
#     app.register_blueprint(admin)
#     app.register_blueprint(frontend)

#     return app

# if __name__ == "__main__":
#   app = create_app()
#   app.run()