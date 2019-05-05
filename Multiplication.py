from die import Die
import pygal

# Create two D6.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store the results in a list.
results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D8 1000000 times."
hist.x_labels =[str(i) for i in range(2, 16)]
#print(list(range(1, 7)))
hist.x_title = "Result"
hist.y_tilte = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file("two_d8.svg")
