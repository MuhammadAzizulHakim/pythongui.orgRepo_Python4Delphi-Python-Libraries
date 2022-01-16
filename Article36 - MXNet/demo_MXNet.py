# Create neural networks in Gluon
# Import the neural network nn package from gluon
from mxnet import nd
from mxnet.gluon import nn

# Create your neural network’s first layer
layer = nn.Dense(2)
print(layer)
# Initialize its weights with the default initialization method
layer.initialize()
# Do a forward pass with random data
x = nd.random.uniform(-1,1,(3,4))
print(layer(x))
# Access the weight after the first forward pass:
layer.weight.data()

# Chain layers into a neural network
# The following code implements a famous network called LeNet through nn.Sequential:
net = nn.Sequential()
# Add a sequence of layers.
net.add(# Similar to Dense, it is not necessary to specify the input channels
        # by the argument `in_channels`, which will be  automatically inferred
        # in the first forward pass. Also, we apply a relu activation on the
        # output. In addition, we can use a tuple to specify a  non-square
        # kernel size, such as `kernel_size=(2,4)`
        nn.Conv2D(channels=6, kernel_size=5, activation='relu'),
        # One can also use a tuple to specify non-symmetric pool and stride sizes
        nn.MaxPool2D(pool_size=2, strides=2),
        nn.Conv2D(channels=16, kernel_size=3, activation='relu'),
        nn.MaxPool2D(pool_size=2, strides=2),
        # The dense layer will automatically reshape the 4-D output of last
        # max pooling layer into the 2-D shape: (x.shape[0], x.size/x.shape[0])
        nn.Dense(120, activation="relu"),
        nn.Dense(84, activation="relu"),
        nn.Dense(10))
print(net)

# The following codes show how to initialize the weights and run the forward pass:
net.initialize()
# Input shape is (batch_size, color_channels, height, width)
x = nd.random.uniform(shape=(4,1,28,28))
y = net(x)
print(y.shape)
# Example of accessing the 1st layer’s weight and 6th layer’s bias:
print(net[0].weight.data().shape, net[5].bias.data().shape)

# Create a neural network flexibly
class MixMLP(nn.Block):
    def __init__(self, **kwargs):
        # Run `nn.Block`'s init method
        super(MixMLP, self).__init__(**kwargs)
        self.blk = nn.Sequential()
        self.blk.add(nn.Dense(3, activation='relu'),
                     nn.Dense(4, activation='relu'))
        self.dense = nn.Dense(5)
    def forward(self, x):
        y = nd.relu(self.blk(x))
        print(y)
        return self.dense(y)

net = MixMLP()
print(net)
# The usage of net is similar as before.
net.initialize()
x = nd.random.uniform(shape=(2,2))
print(net(x))
# Finally, let’s access a particular layer’s weight
print(net.blk[1].weight.data())
