# UpGrad Chatbot for restaurant search Assignment

### Introduction

This bot searches for restaurants and gives them to us as a list

Some examples are as follows:
```
User: Hi
Bot: Hi there! How may I help you?
User: Can you suggest some good restaurants in coimbatore 
Bot: What kind of cuisine would you like to have?
1. Chinese 2. Mexican 3. Italian
4. American 5. Thai
6. North Indian
User: Chinese
Bot: What's the average budget for two people?
1. Lesser than 250 
2. between 250 to 500
3. More than 500
User: Lesser than 250
Bot: Showing you top rated restaurants:
1. Sree Annapoorna in 75, East Arokiasamy Road, RS Puram, Coimbatore rated 75, East Arokiasamy Road, RS Puram, Coimbatore with avg cost 400
2. Shahi Grill in 661, Devaraj Complex, Avinashi Rd, Peelamedu, Coimbatore rated 661, Devaraj Complex, Avinashi Rd, Peelamedu, Coimbatore with avg cost 350
3. Denmarrk Drive-Inn Restaurant in 17, Opposite Zoo Park, Nehru Stadium, Coimbatore rated 17, Opposite Zoo Park, Nehru Stadium, Coimbatore with avg cost 400
4. Hotel Delhi Dharbarr in 171/1, Avinashi Main Road, Near Hope College, Peelamedu, Coimbatore rated 171/1, Avinashi Main Road, Near Hope College, Peelamedu, Coimbatore with avg cost 500
5. Sri Velan Chettinadu Mess in 12, Masakalipalayam Road, Peelamedu, Coimbatore rated 12, Masakalipalayam Road, Peelamedu, Coimbatore with avg cost 300
User: kalirajb05@gmail.com
Bot: Sent. Good Bye!
```


### Installation

Download this repo and cd into the folder

Install the dependencies
```sh
$ pip install -r req.txt
```
Install the spacy en library
```sh
$ python -m spacy download en
```

### Training the RASA 

In order to train the NLU, run the following command

```sh
$ rasa train nlu
```

In order to train RASA CORE, run the following command

```sh
$ rasa train
```

### Running the RASA on commandline

In order to run rasa action server, execute
```sh
$ rasa run actions
```


In order to run rasa at commandline, execute
```sh
$ rasa shell
```

### Sending email

Update Email credentials in chat_config.py

### Running the RASA on Slack

Set up slack as mentioned here

https://rasa.com/docs/rasa/connectors/slack/

Update Slack details in credentials.yml

First get the rasa action server up and running
```sh
$ rasa run
```

Create the ngrok tunneling as mentioned in the video/blog post mentioned above.
Open slack and you're good to go.