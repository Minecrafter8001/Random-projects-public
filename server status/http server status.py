# http server status by Minecrafter


from plyer import notification 
import time
import requests

url = input("enter url:")

while url == "":
 url = input("enter url:")
if url != "": 
 if "https://" not in url and "http://" not in url:
    url = "https://" + url


W


title = 'server checker'
se = False #server error flag
ce = False #client error flag
su = True #server up flag
while True: 
    r = requests.get(url, timeout=5)
    s = r.status_code
    print(r)
    
    if s >= 200 and s < 300:
        # Check if notification has already been sent
        if n:  
         if not su:
            notification.notify(
                title=title,
                message='OK',
                app_icon=None,
                timeout=10,
            )
            ce = False
            se = False
            su = True  # Set flags

            time.sleep(120)
         else:
            time.sleep(120)  # Wait for 2 minutes before checking again

        se = True
        su = False # Set flags
    elif s >= 400 and s < 500:
     su = False
     print("client side error")
    
     if not ce:
        notification.notify(
           title=title ,
           message = 'server down client error',
           app_icon=None,
           timeout=10,
        )
        ce = True
        se = False
        su = False # Set flags
        
        
    
    # If notification hasn't been sent, wait for 30 seconds before checking again
    if not su:
        time.sleep(30)
