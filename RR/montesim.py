
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from scipy.stats import gamma
from scipy.stats import poisson
from scipy.stats import lognorm
from scipy.stats import norm
from scipy.stats import bernoulli
import numpy as np
import numpy as np
import random
from numpy.random import binomial
import tempfile
from sklearn.manifold import Isomap
from sklearn.neighbors import KNeighborsTransformer
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression


# NEEDS METHODS AND CLASSES !
# NEEDS METHODS AND CLASSES !
# NEEDS METHODS AND CLASSED !

cache_path = tempfile.gettempdir()  # we use a temporary folder here
X, _ = make_regression(n_samples=50, n_features=25, random_state=0)
estimator = make_pipeline(
    KNeighborsTransformer(mode='distance'),
    Isomap(n_components=3, metric='precomputed'),
    memory=cache_path)
X_embedded = estimator.fit_transform(X)
X_embedded.shape

def bernoulli_probability(p: float, x: int) -> float:
    """
    Compute the probability of success (1) or failure (0) for a Bernoulli trial
    with success probability p.
    """
    return bernoulli.pmf(x, p)
# import libraries


# initialize variables
n_simulations = 100000
n_points_circle = 0
n_points_square = 0

# create lists to store x and y values
l_xs = []
l_ys = []

# loop n_simulations times
for _ in range(n_simulations):
    
    # x is randomly drawn from a continuous uniform distritbuion
    x = np.random.uniform(-1, 1)
    # store x in the list
    l_xs.append(x)
    
    # y is randomly drawn from a continuous uniform distribution
    y = np.random.uniform(-1, 1)
    # store y in the list
    l_ys.append(y)
    
# loop n_simulations times
for i in range(n_simulations):
    
    # calculate the distance between the point and the origin
    dist_from_origin = l_xs[i] ** 2 + l_ys[i] ** 2
    
    # if the distance is smaller than or equal to 1, the point is in the circle
    if dist_from_origin <= 1:
        n_points_circle += 1
    
    # by definition of the uniform distribution, the point is in the square
    n_points_square += 1
    
# estimate the value of pi
pi = 4 * n_points_circle / n_points_square
print(pi)


def monte_carlo_pi_binomial_fast(n_trials: int) -> float:
    # p(success) ≈ π/4, but we estimate it via simulation
    x = np.random.uniform(-1, 1, n_trials)
    y = np.random.uniform(-1, 1, n_trials)
    successes = np.sum(x**2 + y**2 <= 1)
    return 4 * successes / n_trials

def monte_carlo_pi_binomial(n_trials: int) -> float:
    # Generate n_trials (x, y) coordinates in [-1, 1]
    x = np.random.uniform(-1, 1, n_trials)
    y = np.random.uniform(-1, 1, n_trials)
    
    # Compute the number of successes (points inside the circle)
    inside_circle = np.sum(x**2 + y**2 <= 1)

    # Binomial distribution: number of successes out of n_trials
    # Estimate of Pi using ratio of circle area to square area (π/4)
    return 4 * (inside_circle / n_trials)

if __name__ == "__main__":
    samples = 100000
    estimate = monte_carlo_pi_binomial(samples)
    print(f"Estimated value of Pi using binomial model with {samples} samples: {estimate}")






def monte_carlo_pi(num_samples: int) -> float:
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if x*x + y*y <= 1:
            inside_circle += 1
    return (inside_circle / num_samples) * 4

if __name__ == "__main__":
    samples = 100000
    estimate = monte_carlo_pi(samples)
    print(f"Estimated value of Pi using {samples} samples: {estimate}")


# Poisson probability function
def poisson_probability(mu: float, k: int) -> float:
    """
    Compute the probability of k events occurring in a fixed interval
    given an average rate (mu) using the Poisson distribution.
    """
    return poisson.pmf(k, mu)



def gamma_density(alpha: float, x: float, beta: float = 1.0) -> float:
    """
    Compute the probability density of the Gamma distribution
    for a given shape (alpha), scale (beta), and input x.
    """
    return gamma.pdf(x, a=alpha, scale=beta)

def lognormal_density(sigma: float, x: float, scale: float = 1.0) -> float:
    """
    Compute the probability density of the Log-normal distribution
    for a given shape (sigma), scale (exp(mu)), and input x.
    """
    return lognorm.pdf(x, s=sigma, scale=scale)


# Normal distribution density function
def normal_density(mu: float, sigma: float, x: float) -> float:
    """
    Compute the probability density of the Normal distribution
    for a given mean (mu), standard deviation (sigma), and input x.
    """
    return norm.pdf(x, loc=mu, scale=sigma)

if __name__ == "__main__":
    mu = 5  # average events per interval
    k = 3   # desired number of events
    prob = poisson_probability(mu, k)
    print(f"Poisson probability of {k} events with average rate {mu}: {prob}")

    alpha = 2.0  # shape parameter
    beta = 2.0   # scale parameter
    x_val = 3.0  # value at which to evaluate the density
    density = gamma_density(alpha, x_val, beta)
    print(f"Gamma density at x={x_val} with alpha={alpha} and beta={beta}: {density}")

    sigma = 0.5  # shape parameter (std dev of underlying normal distribution)
    scale = np.exp(0.0)  # e^mu, where mu = 0
    x_ln = 1.0  # value at which to evaluate the density
    ln_density = lognormal_density(sigma, x_ln, scale)
    print(f"Log-normal density at x={x_ln} with sigma={sigma} and scale={scale}: {ln_density}")

    mu_norm = 0.0   # mean
    sigma_norm = 1.0  # standard deviation
    x_norm = 1.0    # value at which to evaluate the density
    norm_density = normal_density(mu_norm, sigma_norm, x_norm)
    print(f"Normal density at x={x_norm} with mu={mu_norm} and sigma={sigma_norm}: {norm_density}")

    p_success = 0.7  # probability of success
    x_outcome = 1    # evaluate for outcome (1 = success)
    bern_prob = bernoulli_probability(p_success, x_outcome)
    print(f"Bernoulli probability of outcome {x_outcome} with p={p_success}: {bern_prob}")

scaler = StandardScaler()
scaler.fit(X_train)  # Don't cheat - fit only on training data
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)  # apply same transformation to test data

# Or better yet: use a pipeline!
est = make_pipeline(StandardScaler(), SGDClassifier())
est.fit(X_train)
est.predict(X_test)
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
Y = np.array([1, 1, 2, 2])
# Always scale the input. The most convenient way is to use a pipeline.
clf = make_pipeline(StandardScaler(),
                    SGDClassifier(max_iter=1000, tol=1e-3))
clf.fit(X, Y)
print(clf.predict([[-0.8, -1]]))