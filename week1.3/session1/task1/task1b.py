# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# iterates through the list fruit while it still has items within it, in reverse order due to the nature of how a pop works

# What features of Python does it rely on?
# pop feature of lists

# 1st: apple pear banana orange -> pop orange
# 4th: apple -> pop apple
# after completion: " "

# Does not run forever as there are a finite number of items (4) in the fruit list