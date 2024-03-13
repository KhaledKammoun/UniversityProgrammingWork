from scipy.stats import norm

def calc_cdf(condition, x, mu, sigma):
    
    if (condition == '<') :
        return norm.cdf(x, mu, sigma)
    else :
        return 1 - norm.cdf(x, mu, sigma)

print(calc_cdf('>', 365, 300, 50))

