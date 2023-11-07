import requests
import telebot
from cred import *

###TEST URL###
# BASE_URL = 'https://test.api.amadeus.com/'

###PROD URL###
BASE_URL = 'https://api.amadeus.com/'


def get_access_token():
    body = {"grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SEC
            }
    token = requests.request(method='post', url=f'{BASE_URL}v1/security/oauth2/token', data=body)
    access_token = token.json()['access_token']
    return access_token


def get_flight_data(origin: type(str),
                    destination: type(str),
                    depdate: type(str),
                    returndate: type(str),
                    pax: type(int),
                    bookclass: type(str)):
    auth_header = {'Authorization': f'Bearer {get_access_token()}'}
    flight_data = requests.request(method='get',
                                   url=f'{BASE_URL}v2/shopping/flight-offers?originLocationCode'
                                       f'={origin}'
                                       f'&destinationLocationCode={destination}'
                                       f'&departureDate={depdate}'
                                       f'&returnDate={returndate}'
                                       f'&adults={pax}'
                                       f'&travelClass={bookclass}'
                                       f'&nonStop=true',
                                   headers=auth_header)
    return flight_data.json()


def send_telegram(message):
    bot = telebot.TeleBot(token=TELE_TOKEN)
    bot.send_message(chat_id=TELE_CHAT_ID, text=message)

