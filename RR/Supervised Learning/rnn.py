import numpy as np

# Linear model: f(x) = w * x + b
class LinearNeuron:
    def __init__(self, input_dim):
        self.w = np.random.randn(input_dim)
        self.b = np.random.randn()

    def forward(self, x):
        return np.dot(x, self.w) + self.b

    def loss(self, x, y):
        preds = self.forward(x)
        return np.mean((preds - y) ** 2)

    def train(self, x, y, lr=0.01, epochs=100):
        for epoch in range(epochs):
            preds = self.forward(x)
            error = preds - y
            grad_w = np.dot(x.T, error) / len(x)
            grad_b = np.mean(error)
            self.w -= lr * grad_w
            self.b -= lr * grad_b
            if epoch % 10 == 0:
                print(f"Epoch {epoch}, Loss: {self.loss(x, y):.4f}")

# Training data
x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])  # Target: y = 2 * x


model = LinearNeuron(input_dim=1)
model.train(x, y, lr=0.1, epochs=50)


# ActivatedNeuron class with activation functions
class ActivatedNeuron:
    def __init__(self, input_dim, activation='relu'):
        self.w = np.random.randn(input_dim)
        self.b = np.random.randn()
        self.activation = activation

    def forward(self, x):
        z = np.dot(x, self.w) + self.b
        return self.activate(z)

    def activate(self, z):
        if self.activation == 'sigmoid':
            return self.sigmoid(z)
        elif self.activation == 'tanh':
            return self.tanh(z)
        elif self.activation == 'relu':
            return self.relu(z)
        else:
            raise ValueError("Unsupported activation function")

    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    @staticmethod
    def tanh(z):
        return np.tanh(z)

    @staticmethod
    def relu(z):
        return np.maximum(0, z)

    def loss(self, x, y):
        preds = self.forward(x)
        return np.mean((preds - y) ** 2)

    def train(self, x, y, lr=0.01, epochs=100):
        for epoch in range(epochs):
            z = np.dot(x, self.w) + self.b
            a = self.activate(z)
            error = a - y
            grad_w = np.dot(x.T, error) / len(x)
            grad_b = np.mean(error)
            self.w -= lr * grad_w
            self.b -= lr * grad_b
            if epoch % 10 == 0:
                print(f"[{self.activation}] Epoch {epoch}, Loss: {self.loss(x, y):.4f}")

# Two-input example
x_multi = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])  # shape (4, 2)
y_multi = np.array([5, 8, 11, 14])  # Target: y = 2*x1 + x2 + b (roughly)

multi_model = ActivatedNeuron(input_dim=2, activation='sigmoid')
multi_model.train(x_multi, y_multi, lr=0.1, epochs=50)


# Two-layer neural network with one hidden layer
class TwoLayerNN:
    def __init__(self, input_dim, hidden_dim, activation='relu'):
        self.W1 = np.random.randn(input_dim, hidden_dim)
        self.b1 = np.random.randn(hidden_dim)
        self.W2 = np.random.randn(hidden_dim)
        self.b2 = np.random.randn()
        self.activation = activation

    def activate(self, z):
        if self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-z))
        elif self.activation == 'tanh':
            return np.tanh(z)
        elif self.activation == 'relu':
            return np.maximum(0, z)
        else:
            raise ValueError("Unsupported activation function")

    def forward(self, x):
        self.z1 = np.dot(x, self.W1) + self.b1
        self.a1 = self.activate(self.z1)
        output = np.dot(self.a1, self.W2) + self.b2
        return output

    def loss(self, x, y):
        preds = self.forward(x)
        return np.mean((preds - y) ** 2)

    def train(self, x, y, lr=0.01, epochs=100):
        for epoch in range(epochs):
            preds = self.forward(x)
            error = preds - y
            grad_W2 = np.dot(self.a1.T, error) / len(x)
            grad_b2 = np.mean(error)

            if self.activation == 'sigmoid':
                d_activation = self.a1 * (1 - self.a1)
            elif self.activation == 'tanh':
                d_activation = 1 - self.a1 ** 2
            elif self.activation == 'relu':
                d_activation = (self.z1 > 0).astype(float)

            delta1 = np.dot(error[:, np.newaxis], self.W2[np.newaxis, :]) * d_activation
            grad_W1 = np.dot(x.T, delta1) / len(x)
            grad_b1 = np.mean(delta1, axis=0)

            self.W2 -= lr * grad_W2
            self.b2 -= lr * grad_b2
            self.W1 -= lr * grad_W1
            self.b1 -= lr * grad_b1

            if epoch % 10 == 0:
                print(f"[2-layer {self.activation}] Epoch {epoch}, Loss: {self.loss(x, y):.4f}")


# Example: TwoLayerNN with hidden layer
x_example = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_example = np.array([5, 8, 11, 14])
net = TwoLayerNN(input_dim=2, hidden_dim=4, activation='tanh')
net.train(x_example, y_example, lr=0.1, epochs=50)

#
# Autoencoder with encoding and decoding
class Autoencoder:
    def __init__(self, input_dim, hidden_dim):
        self.W_enc = np.random.randn(input_dim, hidden_dim)
        self.b_enc = np.random.randn(hidden_dim)
        self.W_dec = np.random.randn(hidden_dim, input_dim)
        self.b_dec = np.random.randn(input_dim)

    def activate(self, z):
        return np.tanh(z)

    def forward(self, x):
        self.z_enc = np.dot(x, self.W_enc) + self.b_enc
        self.a_enc = self.activate(self.z_enc)
        self.z_dec = np.dot(self.a_enc, self.W_dec) + self.b_dec
        return self.z_dec  # output is reconstruction

    def loss(self, x):
        preds = self.forward(x)
        return np.mean((preds - x) ** 2)

    def train(self, x, lr=0.01, epochs=100, save_path=None):
        for epoch in range(epochs):
            # Forward pass
            preds = self.forward(x)
            error = preds - x

            # Backpropagation
            grad_W_dec = np.dot(self.a_enc.T, error) / len(x)
            grad_b_dec = np.mean(error, axis=0)

            delta_enc = np.dot(error, self.W_dec.T) * (1 - self.a_enc ** 2)
            grad_W_enc = np.dot(x.T, delta_enc) / len(x)
            grad_b_enc = np.mean(delta_enc, axis=0)

            # Gradient descent step
            self.W_dec -= lr * grad_W_dec
            self.b_dec -= lr * grad_b_dec
            self.W_enc -= lr * grad_W_enc
            self.b_enc -= lr * grad_b_enc

            if epoch % 10 == 0:
                print(f"[Autoencoder][Epoch {epoch}] Loss: {self.loss(x):.4f}")
                if save_path:
                    self.save(save_path)

    def save(self, filepath):
        np.savez(filepath, W_enc=self.W_enc, b_enc=self.b_enc, W_dec=self.W_dec, b_dec=self.b_dec)
        print(f"[Autoencoder] Model saved to {filepath}")

    def load(self, filepath):
        data = np.load(filepath)
        self.W_enc = data['W_enc']
        self.b_enc = data['b_enc']
        self.W_dec = data['W_dec']
        self.b_dec = data['b_dec']
        print(f"[Autoencoder] Model loaded from {filepath}")

    def test(self, x):
        preds = self.forward(x)
        print("Reconstruction error:", np.mean((preds - x) ** 2))
        return preds

# Example usage
x_auto = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
auto = Autoencoder(input_dim=2, hidden_dim=1)
auto.train(x_auto, lr=0.1, epochs=50, save_path="auto_model.npz")
auto.load("auto_model.npz")
auto.test(x_auto)