def model(img):

  import pickle
  import numpy as np 
  import cv2
  import tensorflow as tf
  import matplotlib.pyplot as plt

  model = pickle.load(open("model.pkl", "rb"))
  img = cv2.imread(img)
  img = cv2.resize(img, (224,224))
  img = np.array(img)
  img = img / 225

  #prediction for just one image
  p = model.predict(img[None,:,:])
  #to get the index of the most possible class
  index =np.argmax(p,axis=1)
  

  def show_the_class(no):

    label_dic ={
      'circle':0,
      'square':1,
      'tringle':2
      } 
  
    no=list(no)
    for i in range(len(no)):
        for key,value in label_dic.items():
          if no[i] == value:
            global final 
            final = key
            if final == 'tringle':
              global info
              info = 'Tringles can be found widely in natural forms from leaf forms to vegetables on your dinner plate, a natural triangle is probably seen everyday.'
            elif final == 'square':
              info = 'There are many squares in nature, from inorganic structures like the salt crystal to biological forms ranging from the amorphous but roughly square box jelly, many different species of plankton, and even each and every plant cell.'
            else:
              info = 'Circles found in planets, stars, celestial bodies, tree rings, rain drops — or they can be man-made — such as traffic roundabouts, buttons, volleyballs, pizza'
  show_the_class(index)          
  return final, info   
      