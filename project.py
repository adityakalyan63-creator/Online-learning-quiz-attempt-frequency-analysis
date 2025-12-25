#----------------------------------------------------------------------
#imort libraries
#----------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------
# Example data: number of quiz attempts per student
#-----------------------------------------------------------------------

quiz_attempts = [1, 2, 2, 3, 3, 3, 4, 4, 5, 1, 2, 3, 4, 5, 5, 2, 3]

#-----------------------------------------------------------------------
# Calculate mean and standard deviation
#-----------------------------------------------------------------------

mean_attempts = np.mean(quiz_attempts)                                   # using numpy
std_attempts = np.std(quiz_attempts)

print("Mean quiz attempts:", mean_attempts)
print("Standard deviation:", std_attempts)

#-------------------------------------------------------------------------
# histogram ploting                                                            # using matplotlib
#-------------------------------------------------------------------------

plt.hist(quiz_attempts, bins=5, color='skyblue', edgecolor='black')
plt.title("Quiz Attempt Frequency Histogram")
plt.xlabel("Number of Attempts")
plt.ylabel("Frequency")
plt.axvline(mean_attempts, color='red', linestyle='dashed', linewidth=2, label=f'Mean = {mean_attempts:.2f}')
plt.legend()
plt.show()
