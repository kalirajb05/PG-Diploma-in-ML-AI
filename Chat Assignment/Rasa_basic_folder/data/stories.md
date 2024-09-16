## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* deny
    - utter_final_bye

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* affirm{"email": "kalirajb05@gmail.com"}
    - slot{"email": "kalirajb05@gmail.com"}
    - action_send_mail


## location specified
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nothing"}
    - slot{"location": "nothing"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than 250"}
    - slot{"price": "Lesser than 250"}
    - action_search_restaurants
* deny
    - utter_final_bye

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "nothing"}
    - slot{"location": "nothing"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than 250"}
    - slot{"price": "Lesser than 250"}
    - action_search_restaurants
* deny
    - utter_final_bye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* affirm{"email": "kalirajb05@gmail.com"}
    - slot{"email": "kalirajb05@gmail.com"}
    - action_send_mail

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "haridwar"}
    - slot{"location": "haridwar"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* deny
    - utter_final_bye

## complete path 5
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "between 250 to 500"}
    - slot{"price": "between 250 to 500"}
    - action_search_restaurants
* affirm{"email": "kalirajb05@gmail.com"}
    - slot{"email": "kalirajb05@gmail.com"}
    - action_send_mail

## Story 1 - search restaurant
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* deny
    - utter_final_bye
    - export

## Story 2 - search restaurant & send mail
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* affirm
    - utter_ask_mail
* affirm{"email": "kalirajb05@gmail.com"}
    - slot{"email": "kalirajb05@gmail.com"}
    - action_send_mail
    - export

## Story 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mbusmkwoid"}
    - slot{"location": "mbusmkwoid"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 250"}
    - slot{"price": "lesser than 250"}
    - action_search_restaurants
* deny
    - utter_final_bye

## Story - User given Location
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "between 250 to 500"}
    - slot{"price": "between 250 to 500"}
    - action_search_restaurants
* deny
    - utter_final_bye

## Story - User given Location & send mail
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "between 250 to 500"}
    - slot{"price": "between 250 to 500"}
    - action_search_restaurants
* affirm
    - utter_ask_mail
* affirm{"email": "kalirajb05@gmail.com"}
    - slot{"email": "kalirajb05@gmail.com"}
    - action_send_mail

## Story - User given cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 250 to 500"}
    - slot{"price": "between 250 to 500"}
    - action_search_restaurants
* deny
    - utter_final_bye

## Story - User given cuisine
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "between 250 to 500"}
    - slot{"price": "between 250 to 500"}
    - action_search_restaurants
* deny
    - utter_final_bye

## Story - cuisine & location and send mail
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "nothing"}
    - slot{"cuisine": "italian"}
    - slot{"location": "nothing"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* affirm
    - utter_ask_mail
* affirm{"email": "kalirajb05@gmail.com"}
    - slot{"email": "kalirajb05@gmail.com"}
    - action_send_mail

## Story - cuisine & location and send mail
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "nothing"}
    - slot{"cuisine": "italian"}
    - slot{"location": "nothing"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search{"price": "more than 500"}
    - slot{"price": "more than 500"}
    - action_search_restaurants
* affirm
    - utter_ask_mail
* affirm{"email": "kalirajb05@gmail.com"}
    - slot{"email": "kalirajb05@gmail.com"}
    - action_send_mail

    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye