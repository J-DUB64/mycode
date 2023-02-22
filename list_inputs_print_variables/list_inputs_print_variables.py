#!/usr/bin.env python3
#!/usr/bin/env python3
""" Alta3 Research | Lists Challenge """

# import random module
import random

def main():

    wordbank = ["indentation", "spaces"]
    tlgstudents= ['Chris', 'Humberto', 'Brandi',
                  'CJ', 'Diego', 'Hussain', 'James',
                  'Jon', 'Kun', 'Nyckolle', 'Sam',
                  'Paul', 'Miggie', 'Max', 'Jynx', 'Suly',
                  'Pat', 'Peter', 'Winton', 'Christian', 'Homer']

    
    print(tlgstudents)


    wordbank.append(4)
    print(wordbank)


    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]


    print(f"Your unfortunate victim is {name}!")
    # print here is pulling variable data from wordbank list as well as 'name' set above
    print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    # for Bonus 1, from the random library, .choice is used to pick a random student name and printed out
    name = random.choice(tlgstudents)
    print(f"{name}")

if __name__ == "__main__":
    main()
