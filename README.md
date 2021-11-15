# Overview:
This is a chat-bot which can give the user information about the items storage 

# Prerequisites:
*  Python >= 3.6
*  Packages as defined in requirements.txt 
*  Redis (Recommended for local testing) 
Redis can be set up by following [this](https://redis.io/topics/quickstart)

# Set up: 
The following steps are needed to set up the envirement :
1. Set up python3 virtual environment: `python3 -m venv ./venv`
2. Activate the virtual environment: `.\venv\Scripts\activate`
3. Install Rasa Open Source: <br />
`pip install -U pip` <br />
`pip install rasa`
4. Dependencies for spaCy <br />
`pip install rasa[spacy]` <br />
`python -m spacy download en_core_web_md` <br />
`python -m spacy link en_core_web_md en` <br />
5. Rasa-SDK:`pip install rasa-sdk`