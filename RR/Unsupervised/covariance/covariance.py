from sklearn.covariance import empirical_covariance
from sklearn.covariance import GraphicalLassoCV
import numpy as np
from sklearn.covariance import ShrunkCovariance
from sklearn.datasets import make_gaussian_quantiles
from sklearn.covariance import MinCovDet

# Example with synthetic data containing outliers
X_outlier = np.vstack([
    rng.multivariate_normal(mean=[0, 0], cov=real_cov, size=490),  # inliers
    rng.uniform(low=-10, high=10, size=(10, 2))                    # outliers
])

# Fit robust covariance estimator
mcd = MinCovDet().fit(X_outlier)

print("Robust location estimate (center):")
print(mcd.location_)

print("Robust covariance estimate:")
print(mcd.covariance_)

print("Raw location estimate (pre-reweighting):")
print(mcd.raw_location_)

print("Raw covariance estimate (pre-reweighting):")
print(mcd.raw_covariance_)
# Example of using ShrunkCovariance
# Generate some random data
real_cov = np.array([[.8, .3],
                     [.3, .4]])
rng = np.random.RandomState(0)
X = rng.multivariate_normal(mean=[0, 0],
                                  cov=real_cov,
                                  size=500)
cov = ShrunkCovariance().fit(X)
cov.covariance_
cov.location_

# Example of using empirical covariance
# Generate some random data
X = [[1,1,1],[1,1,1],[1,1,1],
     [0,0,0],[0,0,0],[0,0,0]]
empirical_covariance(X)


# Estimate sparse inverse covariance using GraphicalLassoCV
sparse_model = GraphicalLassoCV()
sparse_model.fit(X)  # Using the multivariate X

print("Estimated sparse precision matrix (inverse covariance):")
print(sparse_model.precision_)

print("Estimated sparse covariance matrix:")
print(sparse_model.covariance_)

print("Optimal alpha selected by cross-validation:")
print(sparse_model.alpha_)
