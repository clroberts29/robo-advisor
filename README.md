# robo-advisor

## Prerequisites
  
  + Anaconda 3.7
  + Python 3.7
  + Pip

Environment Setup
Create and activate a new Anaconda virtual environment:

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt
pip install pytest # (only if you'll be writing tests)

## Setup
Before suing or developing this application, take a moment to [obtain an AlphaVantage API Key] (https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key:

    ALPHAVANTAGE_API_KEY="abc123"

## Usage

To run the program:

```py
python app/robo-advisory.py
```

