[application]
name = $package
log_level = DEBUG
log_stdout = True
use_forwarded = False
default_theme = default
timezone = local

[restapi]
url = http://infinitystone
interface = public
region = default
verify = False
connect_timeout = 2
read_timeout = 8

[tokens]
expire = 3600

#[redis]
#host=localhost
#db=0

#[database]
#type=sqlite3
#type=mysql
#host=localhost
#username=tachyon
#password=puma
#database=tachyon
