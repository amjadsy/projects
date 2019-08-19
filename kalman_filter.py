import numpy as np
from math import *
import matplotlib.pyplot as plt


#Gaussian Function
def gauss_fun(mu, sigma_sq, x):
	numerator = (-((x-mu)**2))/(2*sigma_sq)
	f_out = (1/(np.sqrt(2*np.pi*sigma_sq)))*(np.exp(numerator))
	return f_out

#Update function
def update_fun(mu1, sigma_sq1, mu2, sigma_sq2):
	mu_prime = ((sigma_sq2*mu1)+(sigma_sq1*mu2))/(sigma_sq1+sigma_sq2)
	sigma_sq_prime = 1/((1/(sigma_sq1))+(1/(sigma_sq2)))
	return mu_prime,sigma_sq_prime

#Motion prediction function
def predict_fun(mu1, sigma_sq1, mu2, sigma_sq2):
	return (mu1+mu2),(sigma_sq1+sigma_sq2)


#Sample measurement and motion values
test_meas = [4,8,1,5,7]
test_motion = [1,2,1,2,1]

meas_var2 = 3
motion_var2 = 2
mu = 0
var2 = 10000

# Run for loop through all measurements and motions, updating along the way
for i in range(0, len(test_meas)):
	mu, var2 = update_fun(mu, var2, test_meas[i],meas_var2)
	print('Update: ' + str(mu) + ',' +str(var2))
	mu, var2 = predict_fun(mu, var2, test_motion[i],motion_var2)
	print('Prediction: ' + str(mu) + ',' +str(var2))

print('Final Values: ' + str(mu) + ',' +str(var2))


