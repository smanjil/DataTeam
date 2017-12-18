
from sqlalchemy import create_engine

# engine = create_engine('postgresql://postgres:12345@localhost/datateamdb')

# for heroku
engine = create_engine(
    'postgres://gngassqimzfoym:3efdfd1d8962443e14f90f59cc8078194ca3a665dedb2bec6013483c08e8f566@ec2-54-235-244-185.compute-1.amazonaws.com:5432/dfomhnli2c3cc5'
)