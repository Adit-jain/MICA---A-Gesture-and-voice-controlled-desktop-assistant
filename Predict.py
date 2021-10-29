import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np


class predict:
    
    def __init__(self):
    
        self.word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}
        self.brain = tf.keras.models.load_model("improved_model")
    
    def prep_image(self,mouse):
        
        
        img = cv2.imread('pred.jpg')
        img_copy = img.copy()
        if not mouse:
            img_copy = cv2.flip(img_copy,1)
        img_copy = cv2.GaussianBlur(img_copy, (7,7), 0)
        img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
        _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
        img_final = cv2.resize(img_thresh, (28,28))
        plt.imshow(img_final,cmap='Greys')
        plt.show()
        img_final =np.reshape(img_final, (1,28,28,1))
        return img_final
    
    
    def predict_image(self,img_final):
        
        prediction = self.brain.predict(img_final)
        prediction = np.argmax(prediction)
        return prediction
    
    
    def driver(self,mouse):
        img = self.prep_image(mouse)
        pred = self.word_dict[self.predict_image(img)]
        # print("The prediction is : ",pred)
        return pred
    
    
if __name__ == '__main__':
    predictor = predict()
    predictor.driver()
        
        
        






