import sys
import telnetlib
from ftplib import FTP
import time
import cv2

# cognex's config
ip = "169.254.89.210"
user = 'admin'
password = ''

#out = cv2.VideoWriter('output.mp4', -1, 20.0, (640,480))

while True:

    start_time = time.time()
    tn = telnetlib.Telnet(ip)
    telnet_user = user+'\r\n'
    tn.write(telnet_user.encode('ascii'))
    tn.write("\r\n".encode('ascii'))

    #time.sleep(0.1)
    tn.write(b"SE8\r\n")
    #time.sleep(0.1)


    ftp = FTP(ip)
    ftp.login(user)

    #ftp.sendcmd('get image.bmp\r\n')
    #print("--- %s seconds ---" % (time.time() - start_time))

    filename = 'image.bmp'
    rename = 'image_get.bmp'
    lf = open(rename, "wb")
    ftp.retrbinary("RETR " + filename, lf.write)
    lf.close()

    image = cv2.imread(rename)
    cv2.imshow('Image', image)
    print("--- %s seconds ---" % (time.time() - start_time))
    #out.write(image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
