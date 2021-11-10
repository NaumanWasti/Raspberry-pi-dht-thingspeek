# import httplib
import http.client as httplib
import urllib
import time
import RPi.GPIO as GPIO
import time
import DHTlibrary as DHT
DHTPin = 11
key = "DIC64BM4Y5Y611ZD"  # Put your API Key here
temp = 20
def thermometer():
    
    dht = DHT.DHT(DHTPin)   #create a DHT class object
    sumCnt = 0
    sumCnt += 1         #counting number of reading times
    chk = dht.readDHT11()     #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
    print ("The sumCnt is : %d, \t chk    : %d"%(sumCnt,chk))
    if (chk is dht.DHTLIB_OK):      #read DHT11 and get a return value. Then determine whether data read is normal according to the return value.
        print("DHT11,OK!")
    elif(chk is dht.DHTLIB_ERROR_CHECKSUM): #data check has errors
        print("DHTLIB_ERROR_CHECKSUM!!")
    elif(chk is dht.DHTLIB_ERROR_TIMEOUT):  #reading DHT times out
        print("DHTLIB_ERROR_TIMEOUT!")
    else:               #other errors
        print("Other error!")
            
    print("Humidity : %.2f, \t Temperature : %.2f \n"%(dht.humidity,dht.temperature))
    time.sleep(2)

    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        # temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        
        params = urllib.parse.urlencode({'field1': dht.temperature,'field2': dht.humidity, 'key':key })
         

        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (dht.humidity)
            print (response.status, response.reason)
            # data = response.read()
            # print(data)
            conn.close()
            
        except:
            print ("connection failed")

        
        break

#if _name_ == "_main_":
while True:
    
    thermometer()
 
    