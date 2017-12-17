
from sqlalchemy import create_engine

# engine = create_engine('postgresql://postgres:12345@localhost/datateamdb')

# for heroku
engine = create_engine(
    'postgresql://xagwigpblkwwea:92ecc654ddcd68cb81210e9e17bb6a8b814e44fc76218e620508f2d10dee5dce@ec2-54-235-244-185.compute-1.amazonaws.com/ddkpiqcv67e0au'
)