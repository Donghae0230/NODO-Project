from flask import Flask

def create_app():
    
    app = Flask(__name__)   # 플라스크 애플리케이션 생성
    app.config["SECRET_KEY"] = "SECRET_KEY"
    
    from .views import main_views
    app.register_blueprint(main_views.bp)
        
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
    