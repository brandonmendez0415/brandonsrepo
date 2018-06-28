import numpy as np
import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization

def alexnet(width, height, lr):
    network = input_data(shape=[None, width, height, 1], name='input')
    network = conv_2d(network, 96, 11, strides=4, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 256, 5, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 384, 3, activation='relu')
    network = conv_2d(network, 256, 3, activation='relu')
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 16, activation='softmax')
    network = regression(network, optimizer='momentum',
	                         loss='categorical_crossentropy',
	                         learning_rate=lr, name='targets')
    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
	                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model


# WIDTH = 80
# HEIGHT = 60
# LR = 1e-3
# EPOCHS = 8
# MODEL_NAME = 'smash4-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2',EPOCHS)
# config = tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)
# sess = tf.Session(config = config)


# model = alexnet(WIDTH, HEIGHT, LR)

# train_data = np.load('training_data.npy')

# train = train_data

# X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
# Y = [i[1] for i in train]

# model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, 
#     snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# # tensorboard --logdir=foo:C:/Users/H/Desktop/ai-gaming/log

# model.save(MODEL_NAME)