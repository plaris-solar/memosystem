import os
import shutil
try:
    import settings_local
except ImportError:
    pass
from memos import db,create_app
from memos.models.User import User
from flask import current_app


def create_db():
    app = create_app()
    app.app_context().push()
    db.init_app(app)
    db.create_all()

    if "LDAP_HOST" not in os.environ:
        user =  User(username=current_app.config['ADMIN_USER'], password=User.create_hash_pw(current_app.config['ADMIN_PASSWORD']),email=current_app.config['ADMIN_EMAIL'], admin=True)
        db.session.add(user)
        db.session.commit()


def copy_static():
    
    src = os.path.join("memos","template_static_files")
    dst = os.path.join("memos","static")
    
    if not os.path.exists(dst):
        os.makedirs(dst)
    shutil.copytree(src,dst,dirs_exist_ok=True)
    

if __name__ == "__main__":
    create_db()
    copy_static()
    
    