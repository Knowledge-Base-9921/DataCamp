# [Project: Building an E-Commerce Clothing Classifier Model](https://app.datacamp.com/learn/projects/2059)

## Credits

Datacamp

## Description

Automate e-commerce processes with image classification.

### Project Details

Transform the retail industry with cutting-edge AI: develop an innovative clothing classification system to create a smarter, more efficient shopping experience.

Leveraging machine learning, you’ll make it easier to find the perfect outfit among a variety of choices, opening up new possibilities in the rapidly evolving digital fashion world.

### Project Instructions

Automate product tagging for the e-commerce store using CNNs.

* Once trained (keeping the epochs to 1 or 2 to keep the run time down), store your predictions on the test set in a list named ``predictions``.
* Calculate the ``accuracy``, and per-class ``precision`` and ``recall`` for your classifier based on the predictions obtained. Store your metrics in variables named ``accuracy``, ``precision``, and ``recall``. Use lists of the appropriate length for the precision and recall.

### Guides

#### 1. Defining the CNN (Convolutional Neural Network)

Define a class containing all the appropriate layers, and a method to perform the forward pass of a batch of images.

* Creating a class to contain the layers of a CNN
    * You could define a class that inherits from PyTorch's nn.module class.
* Adding a convolutional layer
    * You could use PyTorch's nn.Conv2D() class to define the convolutional layer.
    * Create an instance of it in your CNN class's constructor and assign it to an instance variable such as self.conv.
* Adding a Rectilinear Unit
    * You could use PyTorch's nn.ReLU() class.
    * Create an instance of it in your CNN class's constructor and assign it to an instance variable such as self.relu.
* Adding a pooling layer
    *  You could use PyTorch's nn.MaxPool2D() class.
    * Create an instance of it in your CNN class's constructor and assign it to an instance variable such as self.maxpool.
* Adding a fully connected layer
    * You could use PyTorch's nn.Linear() class.
    * Create an instance of it in your CNN class's constructor and assign it to an instance variable such as self.fc.
    * You will also need to flatten the input first, which could be done with an instance of nn.Flatten
* Defining a .forward() method
    * Finally, you'll need to define a .forward() method that passes the input through each layer and returns the output.

#### 2. Training the CNN

Define a training loop that loops over the dataset, calculating the loss and propagating it backwards through the network.

* Define a suitable loss criterion
    * PyTorch's nn.CrossEntropyLoss() could be used here, since this is a multi-class classification problem.
* Define an optimizer
    * You could use PyTorch's optim.Adam() optimizer here.

#### 3. Testing the CNN

Use your trained model to classify the images in the test set, and calculate the appropriate metrics.

* Predict the category of each image in the test data.
    * You'll need to use the .forward() method on your CNN class to pass the test images through the network.
    * You could use torch.argmax() to find the category with the highest predicted probability.
* Calculate the performance metrics
    * You could use Accuracy(), Precision(), and Recall() from torchmetrics to calculate the metrics.