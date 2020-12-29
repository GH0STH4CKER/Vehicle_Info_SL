import requests , socket , time 
from colorama import Fore , init
init()
Lred = Fore.LIGHTRED_EX
Lyel = Fore.LIGHTYELLOW_EX
Lgreen = Fore.LIGHTGREEN_EX
Lcyan = Fore.LIGHTCYAN_EX

ban = "      VEHICLE INFO SL"
cred = "----- [+] Made by GH0STH4CK3R ------"

print(Lgreen + ban)
print(Lyel + cred)


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
    xmldata = str(res.text)
    #print(xmldata)
    
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xmldata)
    for i in root.itertext():
        details.append(i)
    print(Lcyan + "")
    print("***** Vehicle Details *****")
    print(Lgreen + "")
    print("Number Plate      : ",details[2])    
    print("Absolute Owner    : ",details[3])    
    print("Engine No         : ",details[4])    
    print("Vehicle Type      : ",details[5])    
    print("Vehicle Make      : ",details[6])    
    print("Vehicle Model     : ",details[7])    
    print("Manufactured Year : ",details[8])    
    print("Special Condition : ",details[9])    

else :
    print("Http Error !",rc)    

print(Lcyan + "")
input("Exit >")    