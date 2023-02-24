#!/usr/bin/env python3

import random

#Inputs from user
protein = input("What kind of protein would you like? (chicken, beef, fish, or random?): ")
while protein not in ["chicken", "beef", "fish", "random"]:
    print("Invalid input. Please enter chicken, beef, fish, or random.")
    protein = input("What kind of protein would you like? (chicken, beef, fish, or random): ")

side = input("What type of side would you like (vegetables, starch, or salad): ")
while side not in ["vegetables", "starch", "salad"]:
    print("Invalid input. Please enter vegetables, starch, or salad.")
    side = input("What type of vegetable would you like? (vegetables, starch, or salad): ")

#Determine What to Recommend For Chicken
if protein == "chicken":
    chicken_type = input("What type of chicken would you like? (breast, thigh, or drumstick): ")
    chicken_type = chicken_type.capitalize()
    while chicken_type not in ["breast", "thigh", "drumstick"]:
        print("Invalid input. Please enter breast, thigh, or drumstick.")
        chicken_type = input("What type of chicken would you like? (breast, thigh, or drumstick): ")
        chicken_type = chicken_type.capitalize()

    if chicken_type == "breast":
        if side == "vegetables":
            recommendation = "grilled chicken breast with roasted vegetables"
        elif side == "starch":
            recommendation = "Chicken breast and rice with a side of garlic bread"
        elif side == "salad":
            recommendation = "chicken caesar salad with grilled chicken breast"
        else: 
            recommendation = "Sorry, I'm not sure what to do with that type of side."
        # Print recommendation

    elif chicken_type == "thigh":
        if side == "vegetables":
            recommendation = "grilled chicken with roasted vegetables"
        elif side == "starch":
                recommendation = "chicken thigh and rice with a side of garlic bread"
        elif side =="salad":
                 recommendation = "chicken caesar salad with grilled chicken thigh"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."            
        # Print recommendation
        
    elif chicken_type == "drumstick":
        if side == "vegetables":
            recommendation = "grilled chicken drumstick with roasted vegetables"
        elif side == "starch":
            recommendation = "chicken drumstick and rice with a side of garlic bread"
        elif side == "salad":
            recommendation = "chicken caesar salad with grilled chicken drumstick"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."
    else:
        recommendation = "Sorry, I'm not sure what type of chicken that is."
        #Print recommendation
        
# Determine what to recommend Beef
elif protein == "beef":
    beef_type = input("What type of beef would you like? (steak, ground beef, or roast beef): ")
    beef_type = beef_type.capitalize()
    while beef_type not in ["Steak", "Ground beef", "Roast beef"]:
        print("Invalid input. Please enter steak, ground beef, or roast beef.")
        beef_type = input("What type of beef would you like?(steak, ground beef, or roast beef ): ")
        beef_type = beef_type.capitalize()

    if beef_type == "steak":
        if side == "vegetables":
            recommendation = "steak with a side of grilled asparagus"
        elif side == "starch":
            recommendation = "steak and mashed potatoes with a side of green beans"
        elif side == "salad":
            recommendation = "steak salad with balsamic vinaigrette"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."
   
    elif beef_type == "ground beef":
        if side == "vegetables":
            recommendation = "beef stir-fry with mixed vegetables"
        elif side == "starch":
            recommendation = "beef and noodles with a side of stir-fry vegetables"
        elif side == "salad":
            recommendation = "taco salad with ground beef"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."
   
    elif beef_type == "roast beef":
        if side == "vegetables":
            recommendation = "roast beef with a side of glazed carrots"
        elif side == "starch":
            recommendation = "roast beef and potatoes with a side of green beans"
        elif side == "salad":
            recommendation = "beef and blue cheese salad"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."
    else:
        recommendation = "Sorry, I'm not sure what type of beef that is."

# Determine what to recommend Fish
elif protein == "fish":
    fish_type = input("What type of fish would you like? (salmon, tuna, or shrimp): ")
    fish_type = fish_type.capitalize()
    while fish_type not in ["salmon", "tuna", "Roast beef"]:
        print("Invalid input. Please enter steak, ground beef, or roast beef.")
        chicken_type = input("What type of chicken would you like?(steak, ground beef, or roast beef ): ")
        fish_type = fish_type.capitalize()

    if fish_type == "salmon":
        if side == "vegetables":
            recommendation = "grilled salmon with roasted vegetables"
        elif side == "starch":
            recommendation = "salmon and rice with a side of garlic bread"
        elif side == "salad":
            recommendation = "salmon salad with balsamic vinaigrette"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."
   
    elif fish_type == "tuna":
        if side == "vegetables":
            recommendation = "seared tuna with stir-fry vegetables"
        elif side == "starch":
            recommendation = "tuna and noodles with a side of stir-fry vegetables"
        elif side == "salad":
            recommendation = "Avocado  tuna salad"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."
   
    elif fish_type == "shrimp":
        if side == "vegetables":
            recommendation = "pan-fried shrimp  with steamed vegetables"
        elif side == "starch":
            recommendation = "shrimp and quinoa with a side of grilled zucchini"
        elif side == "salad":
            recommendation = "shrimp caesar salad"
        else:
            recommendation = "Sorry, I'm not sure what type of side that is."
    else:
        recommendation = "Sorry, I'm not sure what type of fish that is."
else:
    recommendation = "Sorry, I'm not sure what protein you want."

print("Based on your preferences, you should eat", recommendation, "for dinner.")
    
    #return

    #print("Based on your preferences, you should eat", recommendation, "for dinner.")
    #return

