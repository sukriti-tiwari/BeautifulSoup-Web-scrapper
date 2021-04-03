import requests,re
from bs4 import BeautifulSoup


print("Fetch mail id of all faculty of:")
print("1.MATHEMATICS")
print("2.MECHANICAL")
print("3.SOFTWARE")
print("Enter your choice:")
k=input()
emails=[]
def GetEmail(fac_info):
    email=[]
    for i in fac_info.keys():
        html = requests.get(fac_info[i])
        soup = BeautifulSoup(html.content, "html.parser")
        mail = soup.find('tbody')
        if (mail != None and mail.find('a') != None):
            em = re.findall('.+@', mail.find('a').text)
            if (len(em) > 0):
                email.append(em[0] + 'ktr.srmuniv.ac.in')
    return email

if k=='1':
#mathematics
 print("hello")
 html=requests.get("http://www.srmuniv.ac.in/engineering/school-of-basicsciences/department-of-mathematics/faculty")
 soup=BeautifulSoup(html.content,"html.parser")
 linkname=soup.findAll('a',{"target":"_self"})
 fac_info={}
 for i in linkname:
    fac_info[i.text]=i['href']
    print(i['href'])
 emails=GetEmail(fac_info)
 print(emails)

#mechanical
elif k=='2':
    html=requests.get("http://www.srmuniv.ac.in/mech-engg/faculty-list")
    soup=BeautifulSoup(html.content,"html.parser")
    linkname=soup.findAll('a',{"target":"_self"})
    fac_info={}
    for i in linkname:
       fac_info[i.text]=i['href']
       print(i['href'])
    emails=GetEmail(fac_info)
    print(emails)

#software
if k=='3':
  html=requests.get("http://www.srmuniv.ac.in/engineering/department-of-software-engineering/faculty")
  soup=BeautifulSoup(html.content,"html.parser")
  linkname=soup.findAll('a',{"class":"contentlink"})
  fac_info={}
  for i in linkname:
      fac_info[i.text]='http://www.srmuniv.ac.in'+i['href']
      print('http://www.srmuniv.ac.in'+i['href'])
  emails=GetEmail(fac_info)
  print(emails)


print("Do you want to send mail to all these faculty:")
print("Y/N")
j=input()
if(j=='Y'):
    print("ENTER YOUR MESSAGE TO BE SENT ON MAIL ID:")
    j=input()

    import smtplib
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login("sukritit24@gmail.com", "bleh@456bleh")
    msg = j
    for i in emails:
      server.sendmail("sukritit24@gmail.com",i,msg)
    server.quit()
