from .database import Base, Session, User


def get_db():
    db = Session()
    try:
        yield db
    except:
        db.close()


# ------------------------------------->  User <-------------------------------------------#
def create_user(user_id, db: get_db()):
    user = User(user_id=user_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(user_id, db: get_db()):
    user = db.query(User).filter(User.user_id == user_id).first()
    return user if user else False


def add_location(user_id, lat, lon, db: get_db()):
    user = get_user(user_id, db)
    if user:
        user.latitude = lat
        user.longitude = lon
        db.commit()

