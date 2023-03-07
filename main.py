import os
import openai

users={}
genres = ["Action","Adventure", "Comedy","Drama", "Horror", "Mystery","Romance"]

def add_id(): #KEY
    i = len(users)+1
    print("Your id number is "+ str(i))
    users[i]= []  #add -> dictionary_name[key] = value

def rating(id): #LIST
    for genre in genres:
        rate = int(input("Rate " + str(genre) + " in scale 1-5: "))
        users[id].append(rate)

def recommendation(category):
    prompt = "Recommendations of " + category + " movies of 2021"
    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    print(response.choices[0].text)

def book(cat):
    prompt = "List of 10 books from category: " + cat
    openai.api_key ="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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200,
        top_p=1.0,
        frequency_penalty=0.52,
        presence_penalty=0.5,
        stop=["11."]
    )
    print(response.choices[0].text)

def tweet(tw):
    prompt = "Decide whether" + tw + " sentiment is positive, neutral or negative"
    openai.api_key = "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"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    print(response.choices[0].text)

while True:
    print("Menu")
    print("1) Get your ID")
    print("2) Rate your preferences")
    print("3) Create recommendation")
    print("4) Book")
    print("5) Tweet")
    print("6) Exit")
    choice = int(input("What is your choice? "))
    if choice == 1:
        add_id()
    if choice == 2:
        ID = int(input("What is your ID number? "))
        rating(ID)
    if choice == 3:
        ID2 = int(input("What is your ID number? "))
        index = users[ID2].index(max(users[ID2]))
        category = genres[index]
        recommendation(category)
    if choice == 4:
        print("Categories: Action, Adventure, Comedy, Drama, Horror, Mystery, Romance")
        cat = input("Choose the category:" )
        book(cat)
    if choice ==5:
        tw = input("Write your tweet: ")
        tweet(tw)
    if choice ==6:
        exit()
