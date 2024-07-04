"""
# Object-oriented design in ORMs

Reference:
- https://www.timescale.com/blog/orms-in-production-postgresql-friend-or-foe/
    - "Another benefit is the O in ORM: objects. Objects are flexible, so interfacing
    objects with SQL can allow business logic to be integrated into objects. For
    example, you could pull customer data like purchased items, amount spent,
    shopping time, etc., into a “user” object. The user object could then be equipped
    with functions that allow it to be part of a customer behavior simulation for
    predictive modeling."
"""


from sqlalchemy import Column, Float, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Note this is not a column, so doesn't show up in query results:
    purchases = relationship("Purchase", back_populates="user")

    def total_amount_spent(self):
        """
        Method that demonstrates the advantage of the object orientation of the ORM.
        Object-oriented design allows the data and common operations on the data to
        live close together.
        """
        return sum(purchase.amount for purchase in self.purchases)


class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    amount = Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"))
    # Note this is not a column, so doesn't show up in query results:
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

    # Retrieve User objects:
    users = session.query(User).all()

    # Retrieve total amount spent by each user:
    for user in users:
        print(f"{user.name} spent ${user.total_amount_spent()} in total")

    print("done")
