import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class BernoulliProcess:
    def __init__(self, p=0.5):
        self.p=p

    def simulate(self, n_trials, n_sims=1):
        self.paths = None
        self.n_trials = n_trials
        self.n_sims = n_sims
        x_t = (np.random.uniform(size=(n_trials, n_sims))>(1-self.p))*1
        self.paths = x_t
        return x_t

    def show_paths(self):
        fig, ax = plt.subplots()
        ax.plot(self.paths,
                c='blue',
                alpha=0.5)
        plt.show()

    def get_distributions(self):
        # Get:
        # Binomial: The number of successes in the first n trials
        # Negative binomial: The number of failures needed to get r successes
        # Geometric: The number of failures needed to get one success
        pass

class RandomWalk:
    def __init__(self, init_value=0):
        self.init_value=init_value
        self.paths = None

    def simulate(self, n_steps, n_sims=1):
        self.paths = None
        self.n_steps = n_steps
        self.n_sims = n_sims
        noise = np.random.choice([1, -1], size=(n_steps, n_sims), replace=True)
        noise[0, :] = 0
        noise = noise.cumsum(axis=0)
        x_t = np.zeros(shape=(n_steps, n_sims)) + self.init_value
        x_t += noise
        self.paths = x_t
        return x_t

    def show_paths(self):
        fig, ax = plt.subplots()
        ax.plot(self.paths,
                c='blue',
                alpha=0.5)
        plt.show()

class BrownianMotion:
    def __init__(self, mu=0.0, sigma=1.0, dt=100, init_value=0.0):
        self.mu=mu
        self.sigma=sigma
        self.dt=dt
        self.init_value = init_value
        self.paths = None

    def simulate(self, n_periods, n_sims=1):
        self.paths = None
        self.n_periods = n_periods
        self.n_sims = n_sims
        n_steps = n_periods * self.dt
        noise = self.sigma * np.sqrt(1/self.dt) * np.random.normal(loc=0, scale=1, size=(n_steps, n_sims))
        noise += self.mu * (1/self.dt)
        noise[0, :] = 0
        noise = noise.cumsum(axis=0)
        x_t = np.zeros(shape=(n_steps, n_sims)) + self.init_value
        x_t += noise
        self.paths = x_t
        return x_t

    def show_paths(self):
        fig, ax = plt.subplots()
        ax.plot(np.linspace(0, self.n_periods, self.n_periods * self.dt),
                self.paths,
                c='blue',
                alpha=0.5)
        plt.show()

class OUProcess:
    def __init__(self, mu=0.0, theta=1.0, sigma=1.0, dt=100, init_value=0.0):
        self.mu=mu
        self.theta=theta
        self.sigma=sigma
        self.dt=dt
        self.init_value = init_value
        self.paths = None

    def simulate(self, n_periods, n_sims=1):
        self.paths = None
        self.n_periods = n_periods
        self.n_sims = n_sims
        n_steps = n_periods * self.dt
        noise = self.sigma * np.sqrt(1/self.dt) * np.random.normal(loc=0, scale=1, size=(n_steps, n_sims))
        x_t = np.zeros(shape=(n_steps, n_sims))
        x_t[0, :] = self.init_value
        for step in range(n_steps-1):
            x_t[step+1, :] = x_t[step, :]*(1-(1/self.dt)*self.theta) + (1/self.dt)*self.theta*self.mu + noise[step, :]
        self.paths = x_t
        return x_t

    def show_paths(self):
        fig, ax = plt.subplots()
        ax.plot(np.linspace(0, self.n_periods, self.n_periods * self.dt),
                self.paths,
                c='blue',
                alpha=0.5)
        plt.show()

class GeometricBM:
    pass

class PoissonProcess:
    pass

class MarkovChain:
    pass