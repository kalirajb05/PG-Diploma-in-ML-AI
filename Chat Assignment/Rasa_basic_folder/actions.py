from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
from mail_sender import sendmail

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
city_dict = [x.lower() for x in WeOperate]

def RestaurantSearch(City,Cuisine,Price):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	if('Lesser than 250' == Price):
		TEMP = TEMP[TEMP['Average Cost for two'] < 250]
	elif('between 250 to 500' == Price):
		TEMP = TEMP[(TEMP['Average Cost for two'] >= 250) & (TEMP['Average Cost for two'] <= 500)]
	else:
		TEMP = TEMP[TEMP['Average Cost for two'] > 500]

	TEMP = TEMP.sort_values(['Aggregate rating'], ascending=0)
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

def check_location(loc,city_dict=city_dict):
	if len(loc) == 0:
		return {'location_f' : 'notfound', 'location_new' : None}
	elif loc.lower() not in city_dict:
		return {'location_f' : 'tier3', 'location_new' : None}
	else:
		return {'location_f' : 'found', 'location_new' : loc}

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		print(loc, cuisine, price)
		global results
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Price=price)
		top5 = results.head(5) 
		response=""
		if len(top5) == 0:
			response= 'No restaurants found'
		else:
			response = 'Showing you top results:' + "\n"
			for restaurant in top5.iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
		print(response)
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('email')
		top10 = results.head(10)
		response =u'<h2>Foodie has found few restaurants for you:</h2>'
		restaurant_names = top10['Restaurant Name'].values
		restaurant_location = top10['Address'].values
		restaurant_budget = top10['Average Cost for two'].values
		restaurant_rating = top10['Aggregate rating'].values
		for i in range(len(restaurant_names)):
			name = restaurant_names[i]
			location = restaurant_location[i]
			budget = restaurant_budget[i]
			rating = restaurant_rating[i]
				#msg.body +="This is final test"
			response += u'<h3>{name} (Rating: {rating})</h3>'.format(name = name, rating = rating)
			response += u'<h4>Address: {locality}</h4>'.format(locality = location)
			response += u'<h4>Average Budget for 2 people: Rs{budget}</h4>'.format(budget = budget)

		print(MailID, response)
		sendmail(MailID, '',response)
		return [SlotSet('email',MailID)]

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		res = check_location(location)
		print(location, res)
		return [SlotSet('location',res['location_new']), SlotSet('location_found',res['location_f'])]