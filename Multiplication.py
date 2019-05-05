from die import Die
import pygal

# Create two D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store the results in a list.
results = [die_1.roll() * die_2.roll() for roll_num in range(100000)]
'''for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)'''

#Analyze the results.
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling multiply 2D6 100000 times."
hist.x_labels = [str(i) for i in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6*D6', frequencies)
hist.render_to_file("multiplication.svg")
