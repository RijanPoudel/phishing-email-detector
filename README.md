# 🛡️ Phishing Email Detector

A Machine Learning-based phishing email detection tool built with Python, Flask, and Scikit-Learn.

## Features

- Detect phishing emails using NLP
- Analyze suspicious keywords
- Detect URLs in email content
- Confidence score prediction
- REST API endpoint
- Simple web dashboard

## Project Structure

.
├── app.py
├── detector.py
├── train.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
├── data/
│   └── emails.csv
└── models/
    └── phishing_model.pkl

## Installation

### Clone Repository

git clone https://github.com/YOUR_USERNAME/phishing-email-detector.git

cd phishing-email-detector

### Create Virtual Environment

python -m venv venv

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

## Train Model

python train.py

## Run Application

python app.py

Application runs on:

http://127.0.0.1:5000

## API Example

POST /scan

Request:

{
  "text": "URGENT! Verify your bank account immediately."
}

Response:

{
  "phishing": true,
  "confidence": 94.52,
  "url_count": 0,
  "keywords_detected": [
    "verify",
    "urgent",
    "bank"
  ]
}

## Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- Joblib

## Future Improvements

- SPF/DKIM/DMARC validation
- URL reputation analysis
- Domain age lookup
- Email header inspection
- Threat intelligence integration
- Transformer-based models (BERT)

##MIT License

Copyright (c) 2025 Rijan Poudel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files

## Author

Rijan Poudel
