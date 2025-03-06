# UniConvert Pro

A powerful unit conversion tool built with Streamlit that makes conversions quick and easy.

## Features

- 10 conversion categories: Length, Weight/Mass, Time, Temperature, Area, Volume, Speed, Data, Pressure, and Energy
- Modern, user-friendly interface
- Conversion history tracking with visual chart
- Quick reference formulas for each category

## Deployment Instructions

### Local Development

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Mac/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `streamlit run unit-converter.py`

### Deployment on Streamlit Cloud

1. Push your code to GitHub
2. Create an account on [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app and connect your GitHub repository
4. Set the main file to `unit-converter.py`
5. Deploy!

### Deployment on Heroku

1. Make sure you have the Heroku CLI installed
2. Login to Heroku: `heroku login`
3. Create a new Heroku app: `heroku create your-app-name`
4. Push to Heroku: `git push heroku main`

## Dependencies

- streamlit==1.32.0
- pandas==2.1.3
- matplotlib==3.8.2
- Pillow==10.1.0

## License

© 2024 UnitConvert Pro | Made by NISHAT 