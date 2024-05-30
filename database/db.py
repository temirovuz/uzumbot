from .database import Session, User, Shops


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


# ------------------------------------------------------------------------------------------------------------------ #
def add_shops(name):
    db = Session()
    shop = Shops(name=name)
    db.add(shop)
    db.commit()
    db.refresh(shop)
    return shop


def get_shops():
    db = Session()
    shops = db.query(Shops).all()
    return shops


if __name__ == '__main__':

    shops = get_shops()
    print(shops)
