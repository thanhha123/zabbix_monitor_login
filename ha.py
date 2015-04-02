txt = open("/var/log/auth.log")
cuoi = []

cat = []
a = txt.readlines()


for i in range(0,len(a)):
    if ": Failed password"in a[i]:
        solanfail = solanfail+1
        cuoi.append(a[i])
cat=cuoi[len(cuoi)-1].split(" ")
if b in cat:
    print "{\n"
    print '\t"data":[\n\n'
    print "\t{\n"
    
    print '\t\t"{#LOGIN}":"FAIL",' +   '\t\t"{#USER}":\"Khong ton tai user '+str(cat[11])+"\","+'\t\t"{#IP}":\"'+str(cat[11])+" port "+str(cat[15])+"\""
    print "\t}\n"
    print "\n\t]\n"
    print "}\n"
else:
    print "{\n"
    print '\t"data":[\n\n'
    print "\t{\n"
    print '\t\t"{#LOGIN}":"FAIL",' +  '\t\t"{#USER}":\"'+"User "+str(cat[9])+"\","+ '\t\t"{#IP}":\"'+str(cat[11])+" port "+str(cat[13])+"\""
    print "\t}\n"
    print "\n\t]\n"
    print "}\n"


for i in range(0,len(a)):
    if ": Accepted password"in a[i]:
        solansuccess = solansuccess+1
        cuoi2.append(a[i])
cat=cuoi2[len(cuoi2)-1].split(" ")
if b in cat:
    print "{\n"
    print '\t"data":[\n\n'
    print "\t{\n"
    
    print '\t\t"{#LOGIN}":"FAIL",' +   '\t\t"{#USER}":\"Khong ton tai user '+str(cat[11])+"\","+'\t\t"{#IP}":\"'+str(cat[11])+" port "+str(cat[15])+"\""
    print "\t}\n"
    print "\n\t]\n"
    print "}\n"
else:
    print "{\n"
    print '\t"data":[\n\n'
    print "\t{\n"
    print '\t\t"{#LOGIN}":"FAIL",' +  '\t\t"{#USER}":\"'+"User "+str(cat[9])+"\","+ '\t\t"{#IP}":\"'+str(cat[11])+" port "+str(cat[13])+"\""
    print "\t}\n"
    print "\n\t]\n"
    print "}\n"
