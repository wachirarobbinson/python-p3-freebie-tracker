from sqlalchemy import ForeignKey, Column, Integer, String,Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
dev_user= Table(
    'game_users',
    Base.metadata,
    Column('company_id',ForeignKey('companies.id'),primary_key=True),
    Column('dev_id',ForeignKey('devs.id'),primary_key=True),
    extend_existing=True
)
    
class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    dev_user=relationship('Dev',secondary=dev_user,back_populates='companies')
    freebie=relationship('Freebie',backref=backref('companies'))

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    dev_user=relationship('Company',secondary=dev_user,back_populates='devs')
    freebie=relationship('Freebie',backref=backref('devs'))

    def __repr__(self):
        return f'<Dev {self.name}>'

class Freebie(Base):
    __tablename__='freebies'
    id=Column(Integer(),primary_key=True)
    name = Column(String())
    value = Column(Integer())

    dev_id = Column(Integer(), ForeignKey('devs.id'))
    company_id = Column(Integer(), ForeignKey('companies.id'))

    def __repr__(self):
        return f'User(id={self.id}, ' + \
            f'name={self.name})'