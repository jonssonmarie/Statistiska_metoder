import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from statsmodels.graphics.gofplots import qqplot
import statsmodels.api as sm

# Exercise 1.1
rnd_sample = np.random.randint(4, 8,
                               5)  # Creates a random sample, consisting of five observations (with the values 4, 5, 6, and/or 7)
rnd_sample_mean = rnd_sample.mean()  # Calculates the mean of the sample

print(rnd_sample)
print(rnd_sample_mean)


# Exercise 1.2
def expected_value_discrete(data, probability):
    """Calculates the expected value for a discrete random variable,
    where all values have the same probability."""

    exp_value = 0

    for value in data:
        exp_value += value * probability

    return exp_value


def standard_deviation_discrete(data, probability):
    """Calculates the standard deviation for a discrete random variable,
    where all values have the same probability."""

    sd = 0

    for value in data:
        sd += (value ** 2) * probability

    sd = np.sqrt(sd - (expected_value_discrete(data, probability) ** 2))

    return sd


# Creates population and calculates mean and standard deviation (SD)
population = np.array([4, 5, 6, 7])

pop_mean = expected_value_discrete(population, 0.25)
pop_SD = standard_deviation_discrete(population, 0.25)

print(f"The expected value for the population is: {pop_mean}")
print(f"The standard deviation for the population is: {pop_SD:.1f}")


def create_z_distribution(sample_size):
    """
    Creates 1000 samples with specified sample size and discrete values 4-7.
     Calculates sample means and converts to z-scores.
    """

    z_scores = np.zeros(1000)  # Creates a numpy array with zeros

    for z in range(1000):
        sample = np.random.randint(4, 8, sample_size)
        sample_mean = sample.mean()
        z_scores[z] = ((sample_mean - pop_mean) / (pop_SD / np.sqrt(
            sample_size)))  # Using the known values for the population mean and SD (as specified above)

    return z_scores


def plot_z_scores(
        sample_size):  # Reference: https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
    """
    Creates and plots a z-distribution, with the specified sample size.
    """

    z_scores = create_z_distribution(sample_size)
    plt.hist(z_scores, bins=20,
             density=True)  # density is set to True so that the normal distribution line will follow the data
    mu, std = st.norm.fit(z_scores)  # Calculates the mean and SD
    xmin, xmax = plt.xlim()  # Calculates the data limits
    x = np.linspace(xmin, xmax, 1000)
    p = st.norm.pdf(x, mu, std)  # Probability density function, given the mean and SD
    plt.plot(x, p, 'k', linewidth=2)
    plt.xlabel("z-scores", fontsize=10)
    plt.ylabel("Density")
    plt.title(f"Proof of CLT with Sample Size {sample_size}")
    plt.show()


plot_z_scores(2)
plot_z_scores(10)
plot_z_scores(20)
plot_z_scores(30)
plot_z_scores(50)

"""
Above we can see that the curve for the sample means looks more normal, the higher the sample size. 
Just for fun, we also tested this with a qq-plot. 
For sample size 2 the data does not look normal, but for sample size 50 we can see that the data points nicely 
lines up the way they should if the data is normally distributed. 
We also did a numerical test, using the normaltest from scipy.stats. 
For sample size 2 the test was significant ( 𝑝  < .001), i.e. the data was not normally distributed. 
However, for the 50 observations samples, the null hypothesis could not be rejected ( 𝑝  > .05), 
indicating that the data was normally distributed.
"""


def plot_quantile_quantile(sample_size):
    z_scores = create_z_distribution(sample_size)
    print(st.normaltest(z_scores))
    sm.qqplot(z_scores, line='s')  # Quantile-Quantile Plot
    plt.show()


plot_quantile_quantile(2)
# plot_quantile_quantile(10)
# plot_quantile_quantile(20)
# plot_quantile_quantile(30)
plot_quantile_quantile(50)

# Exercise 1.3 and 1.4 see picture CLT_exercise_1_3_to_1_4.png

"""
Exercise 1.5
If we increase the sample size, the distribution of the sample means will be better approximated to the normal 
distribution. This is in accordance with the central limit theorem. A relatively conservative limit for approximation 
is that n should be  ≥  30. Where this limit should be drawn also depends on how different the original distribution 
is from the normal distribution. For example, a uniform distribution can be approximated to the normal one at 
smaller sample sizes than an exponential distribution (Lantz, 2020).
"""


# Exercise 1.6
def mean_within_CI(sample_size=50):
    """
    Calculates the number of times (out of 1000),
    the population mean (5.5) can be found within a 95% CI,
    based on the specified sample size (default 50)
    and a sample of randomised discrete values between 4 and 7.
    """

    count = 0
    pop_mean = 5.5

    for i in range(1000):
        sample = np.random.randint(4, 8, sample_size)
        sample_mean = sample.mean()

        CI_min = sample_mean - (st.norm.ppf(0.975) * (pop_SD / np.sqrt(sample_size)))  # Calculates the lower CI limit
        CI_max = sample_mean + (st.norm.ppf(0.975) * (pop_SD / np.sqrt(sample_size)))  # Calculates the higher CI limit

        if CI_min < pop_mean < CI_max:  # If the population mean can be found within the CI limits, increase the count
            count += 1

    return count


print(f"Out of 1000 observations, the mean was within the 95 % CI {mean_within_CI(50)} times.")

"""
948 out of 1000 observations were inside the confidence interval (CI). This was close to what was expected, 
since we would expect that 950 out 1000 observations would be inside the CI, since our confidence level is 95%.
"""


# Exercise 1.7
def power_analysis(sample_size=50):
    """
    Generates 1000 samples with the specified sample size (default 50).
    Returns the proportion of significant results, where the null hypothesis is rejected.
    Using a one-tailed test with .05 as the alpha level.
    """

    count = 0

    for i in range(1000):
        sample = np.random.randint(4, 8, sample_size)
        sample_mean = sample.mean()

        z = (sample_mean - 5.1) / (pop_SD / np.sqrt(sample_size))

        if z > st.norm.ppf(0.95):  # If the z score is larger than the critical z score, increase the count
            count += 1

    return count / 1000  # Return the proportion of significant tests


print(f"The proportion of significant tests were {power_analysis()}.")


# Exercise 2.8 and 2.9
def create_uniform_distribution(sample_size):
    """
    Creates a uniform distribution, with the range 7-11.
    Creates an array with 200 samples for the specified sample size.
    Calculates and standardises the mean values for each sample.
    """

    pop_mean_uni = (7 + 11) / 2  # (min + max) / 2 is the expected value for the uniform distribution generated below
    pop_SD_uni = (11 - 7) / np.sqrt(
        12)  # (max - min) / sqrt(12) is the expected SD for the uniform distribution generated below

    samples = np.zeros((200, sample_size))  # Creates an array to store the samples in
    sample_z_scores = np.zeros(200)  # Creates an array to store the standardised means in

    for x in range(200):
        temp_sample = np.random.uniform(7, 11, sample_size)  # Stores the sample in a temporary variable
        samples[x,] = temp_sample  # Stores the sample in the samples array
        sample_z_scores[x] = (temp_sample.mean() - pop_mean_uni) / (
                    pop_SD_uni / np.sqrt(sample_size))  # Calculates and standardises the sample means

    return samples, sample_z_scores


def plot_uniform(data, sample_size):
    """
    Creates a histogram of the given data.
    The parameter sample_size is used for setting the title.
    """

    plt.hist(data, bins=20, color=['#1f77b4' for i in range(sample_size)])
    plt.xlabel("Value", fontsize=10)
    plt.ylabel("Count")
    plt.title(f"Uniform Distribution, Consisting of {sample_size * 200} Observations")
    plt.tight_layout()
    plt.show()


def plot_uniform_mean_value(data,
                            sample_size):  # Reference: https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
    """
    Creates a histogram of the given data.
    The parameter sample_size is used for setting the title.
    """

    plt.hist(data, bins=20, density=True)  # density is set to True so that the normal distribution line will follow the data
    mu, std = st.norm.fit(data)  # Calculates the mean and SD
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)  # Calculates the data limits
    p = st.norm.pdf(x, mu, std)  # Probability density function, given the mean and SD
    plt.plot(x, p, 'k', linewidth=2)
    plt.xlabel("z-score", fontsize=10)
    plt.ylabel("Density")
    plt.title(f"Sample Means from Uniform Distribution (n = {sample_size})")
    plt.show()


# Plots of sample size 5
samples_uni_5, z_values_uni_5 = create_uniform_distribution(5)
plot_uniform(samples_uni_5, 5)
plot_uniform_mean_value(z_values_uni_5, 5)

"""In the first plot, the data is not normally distributed, but follow a uniform distribution. 
Once we have calculated and plotted sample means, the data starts to follow a normal distribution."""

# Exercise 2.10 and 2_11, see CLT_excerise_2_10_to_2_11.png

# Exercise 2.12 and 2.13

# Plots of sample size 20
samples_uni_20, z_values_uni_20 = create_uniform_distribution(20)
plot_uniform(samples_uni_20, 20)
plot_uniform_mean_value(z_values_uni_20, 20)
"""
In the first plot the data is not normally distributed, but follow a uniform distribution. 
Once we have calculated and plotted sample means, the data starts to follow a normal distribution.
"""

# Exercise 2.14 and 2.15
# Plots of sample size 50
samples_uni_50, z_values_uni_50 = create_uniform_distribution(50)
plot_uniform(samples_uni_50, 50)
plot_uniform_mean_value(z_values_uni_50, 50)

"""
In the first plot the data is not normally distributed, but follow a uniform distribution. 
Once we have calculated and plotted sample means, the data starts to follow a normal distribution.
"""

"""
Exercise 2.16
The conclusion is that if we create samples with enough observations in each sample, 
the mean values of the samples will be normally distributed. The answer is d).
"""

"""
How to create a pdf from colab:
!wget -nc https://raw.githubusercontent.com/brpy/colab-pdf/master/colab_pdf.py
from colab_pdf import colab_pdf
colab_pdf('Lab.ipynb')
"""
