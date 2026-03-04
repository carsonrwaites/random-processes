from randomprocesses.randomProcesses import *

#proc = OUProcess(mu=5.0, theta=0.5, sigma=1.0, init_value=0.0, dt=0.01)
#proc = BrownianMotion(mu=0.0, sigma=1.0, init_value=0.0, dt=0.01)
#proc = RandomWalk(init_value=0.0)
#proc = BernoulliProcess(p=0.5, init_value=0.0)
proc = BrownianBridge(a=0, b=0, dt=0.01)
#proc = GeometricBM(mu=0.5, sigma=1.0, init_value=1.0, dt=0.01)

## Simulate paths
paths = proc.simulate(n_periods=2, n_sims=5)

## Plot paths
proc.show_paths()

## Export GIF of paths
proc.export_animated_gif('bb_sample_1.gif')
