from models.domain import users, posts, database

session = database.SessionLocal()


def seed():
    user = users.User(
        name="kshina", email="example@gmail.com", hashed_password="password"
    )

    session.add(user)
    session.commit()


if __name__ == "__main__":
    seed()
