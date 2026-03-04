import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

class StochasticProcess:
    def __init__(self, init_value=0.0, dt=None, title=None):
        self.init_value = init_value
        self.dt = dt
        self.paths = None
        self.time_index = None

    def simulate(self, n_periods, n_sims=1, seed=None):
        if seed is not None:
            np.random.seed(seed)
        dt = self.dt
        # Time index
        if dt is None:  # Discrete process
            self.time_index = np.arange(n_periods + 1)
        else:           # Continuous process
            n_steps = int(n_periods / dt)
            self.time_index = np.linspace(0, n_periods, n_steps + 1)
        self.paths = self._simulate_paths(self.time_index, n_sims)
        return self.paths

    def _simulate_paths(self, time_index, n_sims):
         raise NotImplementedError

    def show_paths(self, alpha=0.5):
        if self.paths is None:
            raise ValueError("Run simulate() first")
        fig, ax = plt.subplots()
        ax.plot(self.time_index, self.paths, alpha=alpha)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.show()


class BernoulliProcess(StochasticProcess):
    def __init__(self, p=0.5, init_value=0.0, dt=None):
        super().__init__(init_value, dt)
        self.p=p

    def _simulate_paths(self, time_index, n_sims):
        n_periods = len(time_index)
        x_t = (np.random.uniform(size=(n_periods, n_sims)) > (1 - self.p)) * 1
        return x_t

    # Yet to be implemented
    def get_distributions(self):
        # Get:
        # Binomial: The number of successes in the first n trials
        # Negative binomial: The number of failures needed to get r successes
        # Geometric: The number of failures needed to get one success
        pass


class RandomWalk(StochasticProcess):
    def __init__(self, init_value=0.0, dt=None):
        super().__init__(init_value, dt)
        self.init_value=init_value

    def _simulate_paths(self, time_index, n_sims):
        n_periods = len(time_index)
        noise = np.random.choice([1, -1], size=(n_periods, n_sims))
        noise[0, :] = 0
        noise = noise.cumsum(axis=0)
        x_t = np.zeros(shape=(n_periods, n_sims)) + self.init_value
        x_t += noise
        return x_t


class BrownianMotion(StochasticProcess):
    def __init__(self, mu=0.0, sigma=1.0, dt=0.01, init_value=0.0):
        super().__init__(init_value, dt)
        self.mu = mu
        self.sigma = sigma

    def _simulate_paths(self, time_index, n_sims):
        n_steps = len(time_index) - 1
        drift = self.mu * self.dt
        diffusion = self.sigma * np.sqrt(self.dt) * np.random.normal(size=(n_steps, n_sims))
        increments = drift + diffusion
        increments = np.vstack([np.zeros(n_sims), increments])
        return self.init_value + np.cumsum(increments, axis=0)


class OUProcess(StochasticProcess):
    def __init__(self, mu=0.0, theta=1.0, sigma=1.0, dt=0.01, init_value=0.0):
        super().__init__(init_value)
        self.mu = mu
        self.theta = theta
        self.sigma = sigma
        self.dt = dt

    def _simulate_paths(self, time_index, n_sims):
        n_steps = len(time_index) - 1
        X = np.zeros((n_steps + 1, n_sims))
        X[0, :] = self.init_value

        for step in range(n_steps):
            dW = np.random.normal(size=n_sims) * np.sqrt(self.dt)
            X[step+1, :] = X[step, :] + self.theta * (self.mu - X[step, :]) * self.dt + self.sigma * dW
        return X


class GeometricBM(StochasticProcess):
    def __init__(self, mu=0.0, sigma=1.0, dt=0.01, init_value=1.0):
        super().__init__(init_value, dt)
        self.mu = mu
        self.sigma = sigma

    def _simulate_paths(self, time_index, n_sims):
        n_steps = len(time_index) - 1
        drift = (self.mu - 0.5 * self.sigma**2) * self.dt
        diffusion = self.sigma * np.sqrt(self.dt) * np.random.normal(size=(n_steps, n_sims))
        log_increments = drift + diffusion
        increments = np.exp(np.vstack([np.zeros(n_sims), log_increments]))
        S = self.init_value * np.cumprod(increments, axis=0)
        return S


class BrownianBridge(StochasticProcess):
    def __init__(self, a=0.0, b=0.0, dt=0.01):
        super().__init__(a, dt)
        self.a = a
        self.b = b

    def _simulate_paths(self, time_index, n_sims):
        n_steps = len(time_index)
        n_periods = n_steps * self.dt
        noise = np.sqrt(1 * self.dt) * np.random.normal(loc=0, scale=1, size=(n_steps, n_sims))
        noise[0, :] = 0
        noise = noise.cumsum(axis=0)
        times = np.linspace(0, n_periods, n_steps).reshape(n_steps, 1) * np.ones(shape=(n_steps, n_sims))
        x_t = self.a * (1 - times) / n_periods + self.b * (times / n_periods) + noise - (times / n_periods) * noise[-1:,]
        return x_t


# ADD
class PoissonProcess:
    pass

# ADD
class MarkovChain:
    pass