from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email==email).first()

    # def get_one(self, uid):
    #     return self.session.query(User).get(uid)

    def get_by_id(self, id):
        return self.session.query(User).filter(User.id==id).first()

    # def get_by_username(self, username):
    #     return self.session.query(User).filter(User.username == username).one()
    #
    # def get_all(self):
    #     return self.session.query(User).all()

    def create(self, **kwargs):
        ent = User(**kwargs)
        self.session.add(ent)
        self.session.commit()
        return ent

    # def delete(self, uid):
    #     user = self.get_one(uid)
    #     self.session.delete(user)
    #     self.session.commit()
    #
    # def update(self, user_data):
    #     user = self.get_one(user_data.get("id"))
    #     user.username = user_data.get("username")
    #     user.password = user_data.get("password")
    #     user_role = user_data.get("role")
    #
    #     self.session.add(user)
    #     self.session.commit()
