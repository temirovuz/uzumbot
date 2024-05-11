from .database import Base, Session, User


# ------------------------------------->  User <-------------------------------------------#
def add_user(user_id):
    db = Session()
    user = User(user_id=user_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user(user_id):
    db = Session()
    user = db.query(User).filter(User.user_id == user_id).first()
    return user if user else False


# -----------------------> Location <----------------------------#
def add_location(user_id, lat, lon):
    db = Session()
    user = get_user(user_id)
    if user:
        user.latitude = lat
        user.longitude = lon
        db.commit()
    else:
        return False


def get_location(user_id):
    db = Session()
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        return user.latitude, user.longitude
    else:
        return False


# -------------------> Language <-----------------------------#
def get_lang(user_id):
    db = Session()
    user = db.query(User).filter(User.user_id == user_id).first()
    return user.lang if user else False


def add_lang(user_id, lang):
    db = Session()
    user = db.query(User).filter(User.user_id == user_id).first()
    if user:
        user.lang = lang
        db.commit()
    else:
        return False

