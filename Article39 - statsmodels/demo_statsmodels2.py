import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

# Sunspots Dataset Metadata
print(sm.datasets.sunspots.NOTE)
# Load Data
dta = sm.datasets.sunspots.load_pandas().data
# Plotting Sun Activity
dta.index = pd.Index(pd.date_range("1700", end="2009", freq="A-DEC"))
del dta["YEAR"]
dta.plot(figsize=(12,4));

# Plotting Autocorrelation and Partial Correlation
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta, lags=40, ax=ax2)

# Print Model Parameters
arma_mod20 = sm.tsa.statespace.SARIMAX(dta, order=(2,0,0), trend='c').fit(disp=False)
print(arma_mod20.aic, arma_mod20.bic, arma_mod20.hqic)
print(arma_mod20.params)

# Print Model Parameters
arma_mod30 = sm.tsa.statespace.SARIMAX(dta, order=(3,0,0), trend='c').fit(disp=False)
print(arma_mod30.aic, arma_mod30.bic, arma_mod30.hqic)
print(arma_mod30.params)

# Does our Model Obey the Theory?
## Calculate and Plot the Residuals
print(sm.stats.durbin_watson(arma_mod30.resid))

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(111)
ax = plt.plot(arma_mod30.resid)

resid = arma_mod30.resid
print(stats.normaltest(resid))

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)

# Show Plots
plt.show()

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid, lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)

# Show Plots
plt.show()

r,q,p = sm.tsa.acf(resid, fft=True, qstat=True)
data = np.c_[r[1:], q, p]
index = pd.Index(range(1,q.shape[0]+1), name="lag")
table = pd.DataFrame(data, columns=["AC", "Q", "Prob(>Q)"], index=index)
print(table)

# Create predictions
predict_sunspots = arma_mod30.predict(start='1990', end='2012', dynamic=True)

fig, ax = plt.subplots(figsize=(12, 8))
dta.loc['1950':].plot(ax=ax)
predict_sunspots.plot(ax=ax, style='r');

# Show Plots
plt.show()

# Calculate Mean Forecast Error
def mean_forecast_err(y, yhat):
    return y.sub(yhat).mean()

# Mean Forecast Error
print(mean_forecast_err(dta.SUNACTIVITY, predict_sunspots))
