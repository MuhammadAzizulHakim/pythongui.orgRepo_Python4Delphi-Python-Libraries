# Import the matplotlib.pyplot module
import matplotlib.pyplot as plt

# Create some sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [10, 8, 6, 4, 2]

# Create a scatter plot of x and y
plt.scatter(x, y, color='red', marker='o', label='x vs y')

# Create a bar chart of x and z
plt.bar(x, z, color='blue', width=0.5, label='x vs z')

# Add a title and axis labels
plt.title('Example of Scatter Plot and Bar Chart')
plt.xlabel('x')
plt.ylabel('y and z')

# Add a legend
plt.legend()

# Show the plot
plt.show()
