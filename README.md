# Football-Predictor
Predict football scores based on historic data

## Aim
Use historic (and then current, mid season) league table position and score data to predict football *scores* based on relative league position

## Data
Source: https://datahub.io/sports-data/english-premier-league
(Could use Python library 'datapackage' to fetch: https://datahub.io/sports-data/english-premier-league#python)
Original data source is http://www.football-data.co.uk/, but this looks less convenient to use directly. 
Notes on data obtained from: http://www.football-data.co.uk/notes.txt

## Method

1. Construct historic point-in-time league tables
2. Analyse how relative league positions of two teams informs match score
3. Use the results of this analysis as the basis for making some predictions!

Then maybe:
* automate
* create twitter bot
* validate/compete against Lawro's predictions (see e.g. https://www.myfootballfacts.co.uk/stats/premier-league-by-season/premier-league-2018-19/mark-lawrensons-predictions-2018-19/. The BBC website doesn't do a good job of publishing Lawro's predictions in a data friendly way.)

## Tools

I think I want to use Python exclusively (for the main part anyway)..
