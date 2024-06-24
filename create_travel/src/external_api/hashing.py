import hashlib

def md5_time_hashing(agency, password,time, user):
    value=f"agency={agency}&password={password}&time={time}&user={user}"
    return hashlib.md5(value.encode('utf-8')).hexdigest()