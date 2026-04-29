# kalman-filter-1d
1D Kalman filter implemented from scratch in Python with real-time visualization.


## How to Run
Install dependencies:
pip install numpy matplotlib

Run:
python kalman_1d.py

## Tuning
- **Q** (process noise) — higher values make the filter trust measurements more and follow changes aggressively. Lower values make the estimate smoother but slower to respond.
- **R** (measurement noise variance) — set to the square of your sensor's standard deviation. Higher values tell the filter the sensor is noisy and to trust it less.

## What I Learned
This was my first attempt at implementing a 1d kalman filter in Python. A static value plus noise was used as the measurements. 
I learned a handful of useful things:
1. How to create plots usning matplotlib, as well as labels, titles, and legends.
2. Using the random.normal() function to generate random numbers with a given mean and standard deviation.
3. The correlation between how Q and R interact. The example of a gyroscope vs. an accelerometer were helpful to me. The gyro will drift overtime, but produces not a lot of noise. Having a higher Q vs R in this case will allow the filter to follow the measurement tightly. Whereas the accelerometer will produce a lot of noise, but not drift overtime, so having a lower Q vs R will allow the filter to ignore the noise better and follow the measurement more closely.
4. A slightly better understanding of the Kalman filter and how it works than I had previously.

This was just a first step in learning about Kalman filters.