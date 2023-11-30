import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def seird_model(y, t, N, beta, sigma, gamma, delta):
    S, E, I, R, D = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I - delta * I
    dRdt = gamma * I
    dDdt = delta * I
    return dSdt, dEdt, dIdt, dRdt, dDdt

N = 1000
beta = 0.2
sigma = 0.1
gamma = 0.05
delta = 0.01
y0 = N-1, 1, 0, 0, 0

t = np.linspace(0, 100, 1000)

result = odeint(seird_model, y0, t, args=(N, beta, sigma, gamma, delta))
S, E, I, R, D = result.T

plt.figure(figsize=(10,6))
plt.plot(t, S, 'b', label='Susceptible')
plt.plot(t, E, 'y', label='Exposed')
plt.plot(t, I, 'r', label='Infected')
plt.plot(t, R, 'g', label='Recovered')
plt.plot(t, D, 'k', label='Dead')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()