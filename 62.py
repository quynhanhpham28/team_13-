print("Price | Discount | New price")
ori=4.95
while (ori<=24.95):
    dis=ori*0.60
    np=ori-dis
    print("$","{:.2f}".format(ori) ," |","$","{:.2f}".format(dis),"  |","$","{:.2f}".format(np))
    ori=ori+5
    