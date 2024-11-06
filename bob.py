import os

bad_hash = os.getenv("BAD_HASH")
good_hash = os.getenv("GOOD_HASH")

os.system(f"git bisect start {bad_hash} {good_hash}")
os.system("git bisect run python manage.py test")