# Main - Pytorch optimization experiments

if __name__ == '__main__':
    #Imports
    import torch
    from torch.autograd import Variable
    import Network_Class
    import numpy as np

    x_data = Variable(torch.Tensor([[1.0], [2.0], [3.0]]))
    y_data = Variable(torch.Tensor([[2.0], [4.0], [6.0]]))

    # our model - reference the class file by using "network class.Model()"
    model = Network_Class.Model()
    print("Model Instantiated", model)

    # Construct our loss function and an Optimizer. The call to model.parameters()
    # in the SGD constructor will contain the learnable parameters of the two
    # nn.Linear modules which are members of the model.
    criterion = torch.nn.MSELoss(size_average=False)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    print("Criterion: MSE")
    print("Optimizer: SGD")

    # Training loop
    for epoch in range(500):
            # Forward pass: Compute predicted y by passing x to the model
        y_pred = model(x_data)

        # Compute and print loss
        loss = criterion(y_pred, y_data)
        #print(epoch, loss)

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # After training
    #Declare a new input for testing - network should double its inputs, so the output should be 8
    hour_var = Variable(torch.Tensor([[4.0], [10.0]]))
    #We can look at the second prediction by indexing into it using the [1][0] below
    y_pred = (model(hour_var).data[1][0])

    print("Y prediction:", y_pred)

    pred_loss = criterion(y_pred, hour_var)
    print("Prediction Loss:", pred_loss)
