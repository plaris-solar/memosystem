import os

# LDAP settings. If LDAP_HOST is not specified, ldap lookups will be skipped.
# os.environ["LDAP_HOST"] = "ldap.com" # host name of LDAP server without schema or port
# os.environ["LDAP_PORT"] = "389" # 389 or 636
# os.environ["LDAP_SCHEMA"] = "ldap" # ldap or ldaps
# os.environ['LDAP_USER'] =  'service_acct' # Sevice account to authenticate to ldap server
# os.environ['LDAP_PASSWORD'] = 'passwd' # password for service account
# os.environ["LDAP_USERNAME"] = "CN={},OU=Users,OU=Company,DC=Company,DC=local".format(os.getenv('LDAP_USER')) # Full ldap locator of service account
# os.environ["LDAP_BASE_DN"] = "OU=Company,DC=Company,DC=local" # Base OU to search for accounts in
# os.environ["LDAP_USER_OBJECT_FILTER"] = "(&(objectclass=Person)(mail=%s))" # ldap lookup condition
# os.environ["LDAP_USER_NAME"] = "sAMAccountName" # field to map to user id
# os.environ["LDAP_EMAIL"] = "mail"  # field to map to email
# os.environ["LDAP_ADMIN_GRP"] = "CN=A-GRP;CN=A2-GRP"  # Group name designating admin role (semicolon separated list)
# os.environ["LDAP_READ_GRP"] = "CN=R-Grp"  # Group name designating read all role (semicolon separated list)
# os.environ["PYTHON_LDAP_TRACE_LEVEL"] = "0"

os.environ['FLASK_APP'] = "app.py"
os.environ['FLASK_DEBUG'] = 'True'
os.environ['FLASK_ENV'] = 'development'

#os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@test.local/MEMOS'
os.environ['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://memosystem:memopw@mysql/memos'
#os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
# set this to 'SQLALCHEMY_ECHO' to 'True' or 'False' to print (or not) the SQL
os.environ['SQLALCHEMY_ECHO'] = 'True'

os.environ['MEMOS_SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

os.environ['MEMOS_EMAIL_SERVER'] = 'smtp.google.com'
os.environ['MEMOS_EMAIL_PORT'] = '587'
os.environ['MEMOS_EMAIL_USER'] = ''
os.environ['MEMOS_EMAIL_PASS'] = ''

# if you want to turn on registration and your are not using LDAP
os.environ['ENABLE_REGISTER']='true'