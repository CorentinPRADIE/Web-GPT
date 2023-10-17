# Web-GPT

## Introduction

Web-GPT is a chatbot built on top of GPT which, in addition to its conversation capabilities, can also browse the web. It leverages the Bing search API to retrieve information from the internet.

## Setup and Installation

### Setup the Front-end:
```sh
cd Web-GPT
npm install
```
### Setup the Back-end:
```sh
cd Flask
pip install openai flask Flask-Cors
```


### Running the Application:

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