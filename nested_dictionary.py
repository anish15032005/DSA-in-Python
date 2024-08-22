travel_log = {
    "France" : {"Number of times visited": 3,"People you met": "Lexie Alford", "Special Attraction":"The Eiffel Tower"},
    "Agra" : {"Number of times visited": 1,"People you met": "Tom Cruise", "Special Attraction":"The Taj Mahal"}
}
#we can get the any key-value pair as a list or as a dictionary
#As a list
second_keyvalue_pair = list(travel_log["France"].items())[1]
print(second_keyvalue_pair)

#As a dictionary
second_element = travel_log["Agra"]
third_keyvalue_pair = dict([list(second_element.items())[2]])
print(third_keyvalue_pair)
