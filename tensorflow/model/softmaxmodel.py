from model import Model
import tensorflow as tf

class Config(object):
  batch_size = 64
  n_samples = 1024
  n_features = 100
  n_classes = 5
  # You may adjust the max_epochs to ensure convergence.
  max_epochs = 50
  # You may adjust this learning rate to ensure convergence.
  lr = 1e-4 

class SoftmaxModel(Model):
	def __init__(self, dataset, labels, config):
		self.config = config
		self.input_data = dataset
		self.labels = labels
		self.input_dim = dataset.shape[1]
		self.n_classes = labels.shape[1]

	def add_placeholders(self):
		self.input_placeholder = tf.placeholder(tf.float64, shape=(self.config.batch_size, self.input_dim))
		self.label_placeholder = tf.placeholder(tf.int32, shape=(self.config.batch_size, self.n_classes)) 

	def create_feed_dict(self, input_batch, label_batch):
		feed_dict = {
			self.input_placeholder = input_batch,
			self.label_placeholder = label_batch,
		}
		return feed_dict

	def train_batch(self, input_batch):
		weights = tf.Variable(tf.truncated_normal([self.input_dim, self.n_classes]))
		biases = tf.Variable(tf.zeros([self.n_classes]))
		logist = tf.matmul(input_batch, weights) + biases
		loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(self.label_placeholder, logist))
		optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(loss)


	def fit(self, sess, input_data, input_labels):
		raise NotImplementedError("Each Model must re-implement this method.")

	def predict(self, sess, input_data, input_labels=None):
		raise NotImplementedError("Each Model must re-implement this method.")