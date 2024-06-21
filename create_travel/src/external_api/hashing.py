import hashlib
value="agency=7626&password=$2y$10$YVRr9Fjh0LKKT3TpmraN1OPBWCmkaL/KW7qm94/ywvaaOWakrrWKe&time=2024-06-14T09:40:16+05:00&user=10659"
def md5_time_hashing(agency, password,time, user):
    value=f"agency={agency}&password={password}&time={time}&user={user}"
    return hashlib.md5(value.encode('utf-8')).hexdigest()