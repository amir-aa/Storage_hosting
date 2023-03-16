from peewee import *
from flask_login import UserMixin
from hashlib import pbkdf2_hmac
db=SqliteDatabase('localdb.db')
class Users(Model,UserMixin):
    Email=CharField(max_length=100,primary_key=True)
    Password=CharField()
    LastLogin=DateTimeField(null=True)
    is_active=BooleanField(default=True)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.Email

    class Meta:
        database=db

class UserServices(Model):
    ServiceName=CharField()
    User=ForeignKeyField(Users)
    class Meta:
        database=db
class Invoice(Model):
    ID=AutoField(primary_key=True)
    Service=CharField()
    Amount=IntegerField()
    User=ForeignKeyField(Users)
    class Meta:
        database=db
class Transaction(Model):
    ID=PrimaryKeyField()
    Invoice=ForeignKeyField(Invoice)
    class Meta:
        database=db

def initialize():
    db.create_tables([Users,UserServices,Invoice,Transaction],safe=True)
initialize()
#Users.insert(Email='aainfoira@gmail.com',Password=pbkdf2_hmac('sha256',b'020202',b'S@lT1',9000).hex()).execute()

#user=Users().select().where(Users.Email=='aainfoira@gmail.com')

#print(user[0].Password)

