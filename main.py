teksts = input("ievadīt tekstu: ")
def deleteE(teksts):
  if teksts.count("e") > 0:
    teksts = teksts.replace("e", " ")
    teksts = teksts.upper ()
    print(teksts)
  else:
    teksts = "TESKST NESATUR VAJADZĪGO CIPARU"
    print(teksts)
    return teksts
deleteE(teksts)