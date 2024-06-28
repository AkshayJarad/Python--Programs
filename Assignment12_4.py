from sys import *
import os
import psutil
import schedule
import time
import smtplib
import urllib.request
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import logging
import socket
import socks

logging.basicConfig(filename='process_log_script.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

http_proxy = os.environ.get('http_proxy')
https_proxy = os.environ.get('https_proxy')
if http_proxy and https_proxy:
    proxy = urllib.request.ProxyHandler({'http': http_proxy, 'https': https_proxy})
    opener = urllib.request.build_opener(proxy)
    urllib.request.install_opener(opener)
    print("Proxy settings applied")

def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib.request.URLError as err:
        logging.error("No internet connection: %s", err)
        return False
    
def MailSender(filename,timestamp):
    try:
        fromaddr = "jaradakshaay@gmail.com"
        toaddr = "jaradrupali96@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to Marvellous Infosystems.
        Please find attached document which contains Log of Running process.
        Log file is created at : %s
        
        This is auto generated mail.
        
        Thanks & Regards,
        Piyush Manohar Khairnar
        """%(toaddr,timestamp)

        Subject = """
        Marvellous Infosystems Process Log generated at : %s
        """%(timestamp)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))

        attachment = open(filename,"rb")

        p = MIMEBase('application','octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment; filename = %s"%filename)

        msg.attach(p)

        if http_proxy:
            socks.set_default_proxy(socks.HTTP, http_proxy, int(os.environ.get('http_proxy_port', 8080)))
            socket.socket = socks.socksocket

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.starttls()
        s.login(fromaddr,"zhai ymcc pgiu wacj")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log File successfully sent through Mail")

    except Exception as E:
        print("Unable to send mail.",E)

def ProcessLog(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except Exception as e:
            print("Error Occured : ",e)

    seperator = "-"*80
    timestamp = time.ctime().replace(' ', '_').replace(':', '-')
    log_path = os.path.join(log_dir,f"MarvellousLog {timestamp}.log")
    f = open(log_path, "w")
    f.write(seperator + "\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime()+ "\n")
    f.write(seperator + "\n")
    f.write("\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms/ (1024 *1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)
    print("Log file is successfully generated at location %s"%log_path)

    connected = is_connected()

    if connected:
        startTime = time.time()
        MailSender(log_path,time.ctime())
        endTime = time.time()

        print("Took %s seconds to send mail"%(endTime - startTime))
    else:
        print("There is no internet connection")     
        with open("error_log.txt", "a") as error_log:
            error_log.write(f"Failed to send email with log {log_path} at {time.ctime()}\n")

def main():
    print("------Marvellous Infosystems by Piyush Khairnar------")

    print("Application name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Invalid Number of Arguements")
        exit()

    if(argv[1] == "h") or (argv[1] == "H"):
        print("This script is used to store log record of running processes")
        exit()

    if(argv[1] == "u") or (argv[1] == "U"):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).seconds.do(ProcessLog)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()