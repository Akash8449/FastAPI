from sqlalchemy  import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

# sqlite
# SQLALCHEMY_DATABASE_URL="sqlite:///./todosapp.db"


# postgres
# SQLALCHEMY_DATABASE_URL= 'postgresql://postgres:test1234!@localhost/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL='postgres://bfovexyo:GW8hVQN9eTfAbomk_MCqeUuYNE51wcZz@drona.db.elephantsql.com/bfovexyo'

# mysql
# SQLALCHEMY_DATABASE_URL="mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoApplicationDatabase"

# sqlite
# engine= create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

# mysql and postgres
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base= declarative_base()