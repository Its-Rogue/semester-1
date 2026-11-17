
import matplotlib.pyplot as plt  # import library

x = [ k for k in range(10) ]  # create a range for the data
y = [ k*k for k in x ]      # create a simple function y=x^2

plt.plot(x, y, marker="o", color="tab:blue", label="y = x²")  # create a 2d plot

plt.xlabel('x')
plt.ylabel('y=x^2')  # annotate

plt.title("A square of the x values")
plt.legend()
plt.annotate("Largest value", xy=(9, 81), xytext=(6, 90),
             arrowprops={"arrowstyle": "->"})
plt.show()  # display

# Try a scatter plot and a bar chart using related data.
plt.scatter(x, y, color="tab:red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Square values scatter plot")
plt.show()

plt.bar(x, y, color="tab:green")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Square values bar chart")
plt.show()

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
