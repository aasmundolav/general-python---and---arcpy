import smtplib, os.path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def SendEmail(text, subject, to, attachment):

    try:
        htmltext = "<html>%s</html>" % text        
        msg = MIMEMultipart()
        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = subject
        msg['From'] = 'no-reply@statoil.com'
        msg['To'] = ", ".join(to)
        msg.preamble = htmltext

        if os.path.isfile(attachment):
            fp = open(attachment, 'rb')
            att = MIMEBase("application","pdf")
            att.set_payload(fp.read())
            fp.close()
            # Encode the payload using Base64
            encoders.encode_base64(att)
            att.add_header('Content-Disposition', 'attachment', filename=os.path.split(attachment)[1])
            msg.attach(att)
            
        
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('mailserver.domain.net')
        s.sendmail(msg['From'], to, msg.as_string())
        s.quit()

    except Exception as e:
        print e.args[0]

SendEmail("this is the text","this is the subject", ["email@domain.net"], r"C:\temp\Output.pdf")
