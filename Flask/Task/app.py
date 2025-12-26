from flask import Flask
from flask_smorest import Api
from flask_mysqldb import MySQL

'''
# import pymysql  # flask-mysqldb 설치 오류
# pymysql.install_as_MySQLdb() # 현재 개발환경 윈도우 / error: failed-wheel-build-for-install
× Failed to build installable wheels for some pyproject.toml based projects
╰─> mysqlclient
There are no Python 3.12 Windows binary wheels for mysqlclient yet. The latest one is mysqlclient-2.2.0-cp311-cp311-win_amd64.whl:
https://pypi.org/project/mysqlclient/#files
You should either downgrade your Python to 3.11, or try installing from source (as you did above):
To build from source, download the MariaDB C Connector and install it. It must be installed in the default location (usually "C:\Program Files\MariaDB\MariaDB Connector C" or "C:\Program Files (x86)\MariaDB\MariaDB Connector C" for 32-bit). If you build the connector yourself or install it in a different location, set the environment variable MYSQLCLIENT_CONNECTOR before installing.
Note that building from source is not supported by the mysqlclient developers:
1. python v 3.12 이하로
2. C++ Build Tools 컴파일러 인스톨 (용량 크고 시간 오래걸림)
기타, django 할 때 mysql connector 문제생길수도??
'''

import yaml
from posts_routes import create_post_blueprint

app = Flask(__name__)

db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

app.config["MYSQL_HOST"] = db_info['mysql_host']
app.config["MYSQL_USER"] = db_info['mysql_user']
app.config["MYSQL_PASSWORD"] = db_info['mysql_password']
app.config["MYSQL_DB"] = db_info['mysql_db']

mysql = MySQL(app)

# 블루프린트 설정
app.config['API_TITLE'] = 'Blog API List'
app.config['API_VERSION'] = 'v1.0'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'

api = Api(app)      # Api 초기화
posts_blp = create_posts_blueprint(mysql)   #
api.register_blueprint(posts_blp)

from flask import render_template
@app.route('/blogs')
def manage_blogs():
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)
