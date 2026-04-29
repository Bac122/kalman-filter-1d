import numpy as np
import matplotlib.pyplot as plt


true_value = 0
noise = np.random.normal(0, 0.1, 100)
measurement = true_value + noise

# Kalman Filter
x_est = 0  # initial estimate
P = 1  # initial covariance
Q = 0.001  # Process noise
R = 0.01  # Measurement noise variance, standard deviation squared

estimates = []
covariances = []

for m in measurement:
    # prediction
    x_pred = x_est
    P_pred = P + Q

    # update
    K = P_pred / (P_pred + R)
    x_est = x_pred + K * (m - x_pred)
    P = (1 - K) * P_pred

    estimates.append(x_est)
    covariances.append(P)


x = np.arange(100)

plt.plot(x, measurement, label='Measurement')
plt.plot(x, estimates, label='Estimate')
plt.axhline(y=true_value, color='r', label='True Value')

plt.xlabel('Sample')
plt.ylabel('Measurement')
plt.title('Noisy Measurement')
plt.legend()
plt.savefig('kalman_output.png', dpi=150, bbox_inches='tight')
plt.show()
