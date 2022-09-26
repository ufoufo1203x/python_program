import pings

p = pings.Ping()
res = p.ping("www.enat.org")
if res.is_reached():
    #接続が出来た
    print("reached")
else:
    print("Not reached")