import datetime
today = datetime.datetime.now()
output = "RPS"[((today - datetime.datetime(today.year, 1, 1)).days + 1) % 3]