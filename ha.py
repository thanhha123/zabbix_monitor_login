txt = open("/var/log/auth.log")

fail_ssh_last = []
cut_fail_ssh_last = []

fail_direct_login_last = []
cut_fail_direct_login_last = []

success_ssh_last = []
cut_success_ssh_last = []

success_direct_login_last = []
cut_success_direct_login_last = []

docfile = txt.readlines()

tukhoa1 = ": Failed password"
tukhoa11 = "invalid"

tukhoa2 = ": FAILED LOGIN"
tukhoa22 = "UNKNOWN"

tukhoa3 = "pam_unix(login:session): session opened"

tukhoa4 = ": Accepted password"


for i in range(0,len(docfile)):
    if tukhoa1 in docfile[i]:
        fail_ssh_last.append(docfile[i])

cut_fail_ssh_last=fail_ssh_last[len(fail_ssh_last)-1].split(" ")
if tukhoa11 in cut_fail_ssh_last:
    print "{\n"
    print '\t"data":[\n\n'
    print "\t{\n"
    print '\t\t"{#LOGIN1}":"FAIL SSH",' +   '\t\t"{#USER}":\"Khong ton tai user '+str(cut_fail_ssh_last[11])+"\","+'\t\t"{#IP}":\"from '+str(cut_fail_ssh_last[13])+" port "+str(cut_fail_ssh_last[15])+"\""
    print "\t},\n"

else:
    print "{\n"
    print '\t"data":[\n\n'
    print "\t{\n"
    print '\t\t"{#LOGIN1}":"FAIL SSH",' +  '\t\t"{#USER}":\"'+"User "+str(cut_fail_ssh_last[9])+"\","+ '\t\t"{#IP}":\" from'+str(cut_fail_ssh_last[11])+" port "+str(cut_fail_ssh_last[13])+"\""
    print "\t},\n"





for i in range(0,len(docfile)):
    if tukhoa2 in docfile[i]:
        fail_direct_login_last.append(docfile[i])

cut_fail_direct_login_last=fail_direct_login_last[len(fail_direct_login_last)-1].split(" ")
if tukhoa22 in cut_fail_direct_login_last:
    print "\t{\n"
    
    print '\t\t"{#LOGIN2}":"FAIL DIRECT LOGIN",' +   '\t\t"{#USER}":\"Khong ton tai user '+"\","+'\t\t"{#IP}":\"'+" Authentication failure "+"\""
    print "\t},\n"

else:
    print "\t{\n"
    print '\t\t"{#LOGIN2}":"FAIL DIRECT LOGIN",' +  '\t\t"{#USER}":\"'+"User "+str(cut_fail_direct_login_last[12])+"\","+ '\t\t"{#IP}":\"'+" Authentication failure "+"\""
    print "\t},\n"



for i in range(0,len(docfile)):
    if tukhoa3 in docfile[i]:
        success_direct_login_last.append(docfile[i])

cut_success_direct_login_last = success_direct_login_last[len(success_direct_login_last)-1].split(" ")

print "\t{\n"
    
print '\t\t"{#LOGIN3}":"SUCCESS DIRECT LOGIN",' +  '\t\t"{#USER}":\"'+"User "+str(cut_success_direct_login_last[11])+"\","+ '\t\t"{#IP}":\"'+" by "+str(cut_success_direct_login_last[13]).sit("\n")[0]+"\""
print "\t},\n"



for i in range(0,len(docfile)):
    if tukhoa4 in docfile[i]:
        success_ssh_last.append(docfile[i])
cut_success_ssh_last=success_ssh_last[len(success_ssh_last)-1].split(" ")

print "\t{\n"
print '\t\t"{#LOGIN4}":"SUCCESS SSH",' +  '\t\t"{#USER}":\"'+"User "+str(cut_success_ssh_last[9])+"\","+ '\t\t"{#IP}":\"from '+str(cut_success_ssh_last[11])+" port "+str(cut_success_ssh_last[13])+"\""
print "\t}\n"
print "\n\t]\n"
print "}\n"
