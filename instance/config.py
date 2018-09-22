import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'p9Bv<qeqqwqwfsdgs#%$#$%T%$i01'
'''SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')'''

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
			'mysql+pymysql://root:root@localhost:3306/db_nobroker'


#mysqldump.exe -e -u root -p root -h localhost:5000 nobroker > C:\nobroker.sql