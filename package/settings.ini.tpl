[application]
name = $package
log_level = DEBUG
log_stdout = True
use_forwarded = False
default_theme = default
timezone = local

[identity]
url = http://localhost/infinitystone
interface = public
region = Region1
verify = False
connect_timeout = 2
read_timeout = 8
# Endpoint Client credentials.
# username = radius
# password = radius

#[redis]
#host=localhost
#db=0

#[database]
type=sqlite3
#type=mysql
#host=localhost
#username=tachyon
#password=puma
#database=tachyon
