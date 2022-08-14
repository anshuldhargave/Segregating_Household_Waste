import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model


def getPrediction(filename):

	IMAGE_DIMS = (224, 224)
	target_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic']

	model = load_model('sample_images/v003_resnet_RN01_last_epoch.h5')

	ori_image = Image.open('sample_images/'+filename)

	# Pre-processing the image

	image = ori_image.convert('RGB')
	image = image.resize(IMAGE_DIMS)
	image = np.expand_dims(image, axis=0)
	image = np.asarray(image)

	# Predicting using the model

	pred = model.predict([image])[0]
	pred_percentage = np.max(pred)
	pred_index = np.argmax(pred)
 
	return target_names[pred_index], pred_percentage*100
