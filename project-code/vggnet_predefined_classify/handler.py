from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import os

def predict_img(model, imgPath):  
  
    img = image.load_img(imgPath, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    print('Predicted:', decode_predictions(preds, top=3)[0])

	
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    model = ResNet50(weights='imagenet')

	#dirname = os.path.dirname(__file__)
    dirname = os.getcwd()
    path = os.path.join(dirname, 'data', 'zebra.jpg')
	
    print('img file path: ' + path)

    ouput = predict_img(model, path)
	
    return ouput
    
handle(None)