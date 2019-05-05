from die import Die
import pygal

# Create a D6.
die = Die()

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels =[]
for i in range(1, 7):
    hist.x_labels.append(str(i))

#print(list(range(1, 7)))
hist.x_title = "Result"
hist.y_tilte = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file("die_visual.svg")
