# coding:utf-8

from app import db, User
if __name__ == '__main__':
    db.create_all()
    print db.metadata.tables
    u = User('flask','flask', 'flask@admin.com')
    db.session.add(u)
    db.session.commit()
    u = db.session.query(User).all()
    print u[0].username
    print 'done.'