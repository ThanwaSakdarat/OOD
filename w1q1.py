print('*** Converting hh.mm.ss to seconds ***')
h,m,s = (input("Enter hh mm ss : ").split())
if int(m)>60 or int(m)<0 or int(m)==60 :
    print("mm("+m+") is invalid!")
elif int(h)<10 and int(m)>9 and int(s)>9:
    x=(int(h)*3600)+(int(m)*60)+(int(s))
    print("0"+h+":"+m+":"+s+" = "+f"{x:,}"+" seconds")
elif int(h)<10 and int(m)<10 and int(s)<10 :
    x=(int(h)*3600)+(int(m)*60)+(int(s))
    print("0"+h+":"+"0"+m+":"+"0"+s+" = "+f"{x:,}"+" seconds")
else:
    x=(int(h)*3600)+(int(m)*60)+(int(s))
    print(h+":"+m+":"+s+" = "+f"{x:,}"+" seconds")