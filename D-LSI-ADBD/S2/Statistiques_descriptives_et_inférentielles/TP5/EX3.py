from scipy.stats import norm

def calc_cdf(x_left, x_right, mu, sigma):
    return norm.cdf(x_right, mu, sigma) - norm.cdf(x_left, mu, sigma)

print(calc_cdf(90, 120, 100, 10))
