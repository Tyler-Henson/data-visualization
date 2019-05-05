from die import Die
import pygal

# Create two D6.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling 3D6 100000 times."
hist.x_labels = [str(i) for i in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('3D6', frequencies)
hist.render_to_file("three_dice.svg")
