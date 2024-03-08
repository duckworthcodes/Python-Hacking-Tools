import requests
import numpy as np
import cv2

while True:
    try:
       
        images = requests.get("https://100.115.82.78:8080/shot.jpg")
        
      
        video = np.array(bytearray(images.content), dtype=np.uint8)
        
        
        render = cv2.imdecode(video, -1)
        
        
        cv2.imshow('frame', render)
        
       
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
            
    except Exception as e:
        print("An error occurred:", e)
        break


cv2.destroyAllWindows()

    