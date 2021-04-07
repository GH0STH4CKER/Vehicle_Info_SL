import requests , socket , time , re,sys
from colorama import Fore , init
init()
Lred = Fore.LIGHTRED_EX
Lyel = Fore.LIGHTYELLOW_EX
Lgreen = Fore.LIGHTGREEN_EX
Lcyan = Fore.LIGHTCYAN_EX

def slowprint(str):
   for c in str :
     sys.stdout.write(Lyel + c)
     sys.stdout.flush()
     time.sleep(0.07)

ban = """
 â âââââââ âââââââââ  âââââ âââââ ââââââââââ âââââ  
 ââââââââââââââââââââââââââ ââââ âââââ âââââ âââââââ"""
cred = "------------ [+] Made by GH0STH4CK3R ---------------\n"

print(Lgreen + ban)
slowprint(cred)

try:
    ip = socket.gethostbyname("www.google.com")
    ip = socket.gethostbyname("www.facebook.com")
    ip = socket.gethostbyname("www.yahoo.com") 
    print(Lgreen + "\n[+] Internet : Active")   
except Exception as e:
    print(Lred + "[-] Internet : Not Available ")  
    time.sleep(5)
    exit()
print(Lcyan + "")
url = "http://api.lankagate.gov.lk:8280/GetVehicleLimitedInfoDMT/1.0"

nbp = input("Enter Vehicle No (Number-Plate) : ")

xml = """<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v1="http://schemas.conversesolutions.com/xsd/dmticta/v1"><soapenv:Body><v1:GetVehicleLimitedInfo><v1:vehicleNo>{}</v1:vehicleNo><v1:phoneNo>94000000000</v1:phoneNo></v1:GetVehicleLimitedInfo></soapenv:Body></soapenv:Envelope>""".format(nbp)

headers = {"Content-Type": "text/xml; charset=utf-8","Authorization": "Bearer  798f7fb2-ecce-3c76-a675-143038467dd6"} 

res = requests.post(url, data=xml, headers=headers)
rc = res.status_code
details =[]

if rc == 200 :
    xmldata = res.text 
    #print(xmldata)
    #  Find tags

    xml2 = xmldata

    xml2 = xml2.replace("><", ">\n<")

    xml_filter_ptn = r'<(\w|>|/|<|-| )*>'
    match = re.finditer(xml_filter_ptn, xml2, re.MULTILINE)

    xml_detail = []
    full_details = {}

    for i in match:
        xml_detail.append(i.group())

    detail_filter_ptn = r">(\w| |-)*<"
    name_filter_ptn = r"<(\w| |-)*>"

    for i in xml_detail:
        value = re.search(detail_filter_ptn, i)
        name = re.search(name_filter_ptn, i)
        if value:
            # value
            value = value.group().strip(">")
            value = value.strip("<")
            value = value.strip()

            # name
            name = name.group().strip(">")
            name = name.strip("<")
            name = name.strip()

            full_details[name] = value      
    
    fdts = full_details
    spc = ""
    print(" ")
    for k, e in fdts.items():
    
        if len(k) < 21 :
        	stm = 21 - len(k) 
        	spc = " " * stm
        else :
        	spc = ""

        if k == "RequestId" or k == "TransactionCharge" :
            pass
        else :
            print (k + spc + ' : ' + str(e))
  

else :
    print("Http Error !",rc)    

print(Lcyan + "")
input("Exit >")  
