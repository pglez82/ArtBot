from PIL import Image
from collections import namedtuple
import numpy as np
import mxnet as mx

#last_epoch=10
last_epoch=5

class PictureClassifier:

	def __init__(self):
		self.Batch = namedtuple('Batch', ['data'])
		ctx = mx.cpu()
		sym, arg_params, aux_params = mx.model.load_checkpoint('../../../../imgclassifier/models/finetuned/resnet-18-ft/resnet-18-ft',last_epoch)
		self.mod = mx.mod.Module(symbol=sym, context=ctx, label_names=None)
		self.mod.bind(for_training=False, data_shapes=[('data', (1,3,224,224))], label_shapes=self.mod._label_shapes)
		self.mod.set_params(arg_params, aux_params, allow_missing=True)
		with open('../../../../imgclassifier/labels.txt', 'r') as f:
			self.labels = [l.rstrip().split()[0] for l in f]

	def _get_image(self, path):
		# download and show the image
		img = mx.image.imread(path)
		# convert into format (batch, RGB, width, height)
		img = mx.image.imresize(img, 224, 224) # resize
		img = img.transpose((2, 0, 1)) # Channel first
		img = img.expand_dims(axis=0) # batchify
		return img

	def predict(self, path):
		img = self._get_image(path)
		# compute the predict probabilities
		self.mod.forward(self.Batch([img]))
		prob = self.mod.get_outputs()[0].asnumpy()
		# print the top-5
		prob = np.squeeze(prob)
		a = np.argsort(prob)[::-1]
		res = []
		for i in a[0:5]:
			#print('probability=%f, class=%s' %(prob[i], self.labels[i]))
			res.append((prob[i],self.labels[i]))
		return res
