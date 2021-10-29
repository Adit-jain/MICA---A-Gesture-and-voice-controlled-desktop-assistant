import cv2
import mediapipe as mp
import time
import math



class HandDetector():
    def __init__(self,mode=False,num_hands=2,detection_con=0.5,tracking_con=0.5):
        self.mode = mode
        self.num_hands = num_hands
        self.detection_con = detection_con
        self.tracking_con = tracking_con
        
        
        ##Initialize mediapipe
        self.mpHands = mp.solutions.hands
        #Default Value
        self.hands = self.mpHands.Hands()
        ##Initialize drawer between hands
        self.mpDraw = mp.solutions.drawing_utils
        
        
        
        
        
    def findHands(self,frame):
        
       ## Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        ## Give converted img to the module
        self.results = self.hands.process(frame_rgb)
        
        # ## Record shape of Image
        # h,w,c = frame.shape
        
        ## If landmarks are detected
        if self.results.multi_hand_landmarks:
            ## For each hand detected
            for hand_lms in self.results.multi_hand_landmarks:
                #Draw landmarks
                self.mpDraw.draw_landmarks(frame, hand_lms, self.mpHands.HAND_CONNECTIONS)
                    
        return frame
    
    
    def findPosition(self,frame,handNo=0,point_no=[]):
        
        lmList = []
        h,w,c = frame.shape
        if self.results.multi_hand_landmarks:
            hand_lms = self.results.multi_hand_landmarks[handNo]
            
            ## Get locations of landmarks
            for index,lm in enumerate(hand_lms.landmark):
                
                if index in point_no:
                    # Convert locations to pixels
                    cx, cy = int(w*lm.x),int(h*lm.y)
                    #Append to list
                    lmList.append([index,cx,cy])
                    cv2.circle(frame, (cx,cy), 10, (255,0,0),cv2.FILLED)
        
        return lmList



    

def main():
    

    
    ## For fps, time initializers
    pTime =0
    cTime =0
    drawing=[]
    start=False
    cap = cv2.VideoCapture(0)
    
    ##If camera not opened, quit
    if not cap.isOpened():
        print("Cannot open Camera")
        exit()
        
    detector = HandDetector()
    

    while True:
        ret, frame = cap.read()
        
        frame = detector.findHands(frame)
        lmList = detector.findPosition(frame,point_no=[4,8])
        

        
        if len(lmList)>0:
            x1,y1 = lmList[0][1],lmList[0][2]
            x2,y2 = lmList[1][1],lmList[1][2]
            cx,cy = int((x1+x2)/2),int((y1+y2)/2)
            
            cv2.line(frame, (x1,y1), (x2,y2), (255,0,0),2)
            cv2.circle(frame, (cx,cy), 5, (255,255,0), cv2.FILLED)
            
            length = math.hypot(x2-x1,y2-y1)
            
            if length<50:
                cv2.circle(frame, (cx,cy), 5, (0,255,255), cv2.FILLED)
                drawing.append([x2,y2])
        
        
        # if cv2.waitKey(1) == ord('s'):
        #     start=True
        # if cv2.waitKey(1) == ord('e'):
        #     start = False
        
        # if len(lmList)>0 and start:
        #     x2,y2 = lmList[1][1],lmList[1][2]
        #     drawing.append([x2,y2])
            
            
        
        
        
        
        ##Display the fps
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        ## Put fps on the screen
        cv2.putText(frame, str(int(fps)), (10,30), cv2.FONT_HERSHEY_COMPLEX, 1 ,(255,0,0),3)
        
        
        if not ret:
            print("Can't recieve Frame. Exiting.....")
            break
        
        cv2.imshow('frame', frame)
        
        
        
        if cv2.waitKey(1) == ord('q'):
            break
        
        
        
        
    cap.release()
    cv2.destroyAllWindows()
    return drawing

if __name__=='__main__':
    main()
        

