from scipy.stats import norm, t

x1 = 50
s1 = 10
x2 = 55
s2 = 15
n1 = 80
n2 = 20
std = ((s1**2)/n1 + (s2**2)/n2)**0.5
x = x1 - x2
# find degrees of freedom
df = (s1**2/n1 + s2**2/n2)**2 / ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))
print(f"Degrees of freedom: {df}")
print(f"Standard Deviation: {std}")# standard deviation
print(f"Z-score: {x/std}") # z-score
print(f"Expected Standard t score to reject null hypothesis: {t.ppf(0.05, df=df)}") # critical value for standard normal distribution - left sided hypothesis testing
print(f"Non-standard t score to reject null hypothesis: {t.ppf(0.05, loc=0, scale=std, df=df)}") # critical value
print(f"Given sample: {x}")
print(f"P value of the given sample: {t.cdf(x, loc=0, scale=std, df=df)}")
# print(1 - t.cdf(x, loc=0, scale=std, df=df))
