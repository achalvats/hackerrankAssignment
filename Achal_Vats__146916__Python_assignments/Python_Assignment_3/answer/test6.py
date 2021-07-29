import imaplib
import re
import config
import email
import xlwt

#print("0i")
dataF=open("data8.txt","r+")
wb=xlwt.Workbook()
sheet1=wb.add_sheet('Sheet1')
sheet1.write(0,0,'Mail-date')
sheet1.write(0,1,'Mail-Links')
counter=1
con = imaplib.IMAP4_SSL("imap.gmail.com",993)
#print("1i")
con.login(config.EMAIL_ADDRESS2,config.PASSWORD)
#print("2i")
con.select("INBOX")
result, data = con.uid('search', None, 'ALL')
mail_ids=data[0]
id_list=mail_ids.split()
for ids in id_list:
    result2, data2 = con.uid('fetch', ids, 'RFC822')
    raw_data = data2[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_data)
    subject= email_message['Subject']
    mail_date=email_message['Date']
    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
# =============================================================================
#         filename =part.get_filename()
#         if not filename:
#             ext = '.html'
#             filename ='msg-part-%08d%s' %(counter, ext)        
# =============================================================================
        content_type = part.get_content_type()
        if content_type=='text/plain':
            print("##############################################")
            dataF.write("\n##############################################\n")
            plain_text = part.get_payload()
# =============================================================================
#             link_pattern = re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
#             search = link_pattern.search("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
# =============================================================================
            urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', plain_text)
            print("NEXT MAIL:")
            dataF.write("NEXT MAIL:\n")
            print("SUBJECT:",subject)
            print("date:",mail_date)
            dataF.write("SUBJECT:")
            dataF.write(str(subject))
            if len(urls) != 0:
                print("Link found! -> ")
                dataF.write("\nLink found! -> \n")
                for u in urls:
                    #if u is None:
                      #  continue
                    #else:
                    print(counter)
                    print(u)
                    dataF.write(u)
                    dataF.write("\n")
                    sheet1.write(counter,0,mail_date)
                    sheet1.write(counter,1,u)
                    counter=counter+1                   
                #print(filename)
            else:
                print("No links were found.")
                dataF.write("\nNo links were found.")
            print("##############################################\n\n\n\n")
            dataF.write("\n##############################################\n\n\n\n")
            wb.save('email-links.xls')
print("SAVED IN TEXT AND EXCEL FILE")
        
           

        
        
        
        
        
            


#for i in range(latest_email_id,first_email_id, -1):
 #   typ, data = con.fetch(i, '(RFC822)' )

#for response_part in data:
 #   if isinstance(response_part, tuple):
  #      msg = email.message_from_string(response_part[1])
   #     email_s = msg['subject']
    #    email_f = msg['from']
     #   print(email_s,email_f)
        

    

#for num in data[0].split():
 #   typ, data = con.fetch(num, '(RFC822)')
  #  print('Message %s\n%s\n' % (num, data[0][1]))