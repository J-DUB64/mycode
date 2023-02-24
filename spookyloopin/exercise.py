#!/usr/bin/env python3
"""Count the line"""

counter = 0

with open("dracula.txt", "r") as blood:
    with open("vampytimes.txt", "w") as fangs:
        for line in blood:
            if "vampire" in line.lower():
                print(line)
                counter += 1
                fangs.write(line)

print(counter)
            

