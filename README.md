# WebGPT

While ChatGPT stands as one of the most advanced chatbots in existence, it operates without a direct link to internet. Recognizing this gap, GPT WEB was conceived. Welcome to GPT WEB, where the limitations of static knowledge meet the boundlessness of the internet.

## How It Works:
1. User Interaction: Users initiate a conversation or ask a question through our intuitive interface.
2. Initial Assessment: The system evaluates the query to determine if it requires real-time data from the BING Search API.
3. Search Integration: Should the system identify the need, a web search is triggered to fetch the latest information related to the user's query.
4. Informed Response Generation: Results from the search are melded with the initial question, allowing for a more informed response to be crafted.
5. User Feedback: A comprehensive and current answer is presented to the user.


With GPT WEB, we've created a bridge between vast static knowledge and dynamic real-time updates, ensuring users always receive the most pertinent information.

## Tech Stack:
Frontend: Vue.js
Backend: Flask.py
Front-Back connection : Axiom
Api’s: OpenAI's ChatGPT and BING Search API
Cloud hosting: Microsoft Azure Cloud

## WebGPT Team:
PONDEVIE Sam
TAVANI Lucas
PRADIE Corentin

## Setup and Installation

```sh
git clone https://github.com/CorentinPRADIE/Web-GPT.git
```

### Front-end Setup:
```sh
cd Web-GPT
npm install
```
### Back-end Setup:
```sh
cd Flask
pip install openai flask Flask-Cors
```
## Run the WebGPT:

#### Run the Front-end:
```sh
cd Web-GPT 
npm run dev
```
#### Run the Back-end:
```sh
cd Flask
python app.py
```