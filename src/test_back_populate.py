from sqlalchemy import Column, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    purchases = relationship("Purchase", back_populates="user")


class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="purchases")


engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

if __name__ == "__main__":
    Session = sessionmaker(bind=engine)
    session = Session()

    user1 = User(name="Alice")
    user2 = User(name="Bob")
    purchase1 = Purchase(item_name="laptop", amount="1000", user=user1)
    purchase2 = Purchase(item_name="mouse", amount="10", user=user1)
    purchase3 = Purchase(item_name="house", amount="1000000", user=user2)

    session.add(user1)
    session.add(user2)
    session.add(purchase1)
    session.add(purchase2)
    session.add(purchase3)
    session.commit()

    # Query results
    engine.execute("select * from users").all()
    engine.execute("select * from purchases").all()

    print("done")
