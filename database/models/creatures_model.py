from sqlalchemy import Column, ARRAY, SmallInteger
from app.data.session import Base


class Creatures(Base):
    __tablename__ = 'creatures'

    cr_id = Column(SmallInteger, nullable=False, primary_key=True)
    cr_type = Column(ARRAY(SmallInteger), nullable=False)
    cr_home = Column(ARRAY(SmallInteger), nullable=False)
    cr_social = Column(ARRAY(SmallInteger), nullable=False)
    cr_skills = Column(ARRAY(SmallInteger), nullable=False)
    cr_size = Column(ARRAY(SmallInteger), nullable=False)
    cr_weight = Column(ARRAY(SmallInteger), nullable=False)
    cr_phylum = Column(SmallInteger, nullable=False)
    cr_class = Column(SmallInteger, nullable=False)
    cr_order = Column(SmallInteger, nullable=False)
    cr_family = Column(SmallInteger, nullable=False)
