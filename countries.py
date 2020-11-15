import json
import sys

import requests

URL_ALL = "https://restcountries.eu/rest/v2/all"
URL_NAME = "https://restcountries.eu/rest/v2/name"


def request(URL):
    try:
        request = requests.get(URL)
        if request.status_code == 200:
            return request.text
    except:
        print("Error making request in: ", URL)


def parsing(response_text):
    try:
        return json.loads(response_text)
    except:
        print("Error making parsing.")


def count_countries():
    response = request(URL_ALL)
    if response:
        list_of_countries = parsing(response)
        if list_of_countries:
            return len(list_of_countries)


def list_countries():
    response = request(URL_ALL)
    if response:
        list_of_countries = parsing(response)
        if list_of_countries:
            for country in list_of_countries:
                print(country['name'])


def show_population(country_name):
    response = request("{}/{}".format(URL_NAME, country_name))
    list_of_countries = parsing(response)
    if response:
        if list_of_countries:
            for country in list_of_countries:
                print("{}: {} inhabitants".format(country['name'], country['population']))
    else:
        print("Country not found!")


def show_currencies(country_name):
    response = request("{}/{}".format(URL_NAME, country_name))
    if response:
        list_of_countries = parsing(response)
        if list_of_countries:
            for country in list_of_countries:
                print("Currency of", country['name'])
                currencies = country['currencies']
                for currency in currencies:
                    print("{} - {}".format(currency['name'], currency['code']))


def languages(country_name):
    response = request("{}/{}".format(URL_NAME, country_name))
    if response:
        list_of_countries = parsing(response)
        if list_of_countries:
            for country in list_of_countries:
                print("Language of", country['name'])
                languages = country['languages']
                for language in languages:
                    print("Language: {}/{}".format(language['name'], language['nativeName']))


def capital(country_name):
    response = request("{}/{}".format(URL_NAME, country_name))
    list_of_countries = parsing(response)
    if response and list_of_countries:
        for country in list_of_countries:
            print("capital of {}: {}".format(country['name'], country['capital']))


def read_country_name():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print("You need to pass the name of the country")


def help():
    print("### welcome to the countries's system ###")
    print("Usage: python countries.py [OPTION] [COUNTRY]")
    print("OPTIONS: [-t total countries] [-b capital] [-l list countries] [-p population] [-c currency]\n")
    print("Example:\npython countries.py -l\npython countries.py -p brasil")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Try 'python country.py --help' for more information.")
    elif sys.argv[1] == "--help":
        help()
    elif sys.argv[1] == "-t":
        print("Number of countries in the world: {}".format(count_countries()))
    elif sys.argv[1] == "-c":
        country = read_country_name()
        if country:
            show_currencies(country)
    elif sys.argv[1] == "-p":
        country = read_country_name()
        if country:
            show_population(country)
    elif sys.argv[1] == "-l":
        list_countries()
    elif sys.argv[1] == "-i":
        country = read_country_name()
        if country:
            languages(country)
    elif sys.argv[1] == "-b":
        country = read_country_name()
        if country:
            capital(country)
    else:
        print("Unknown option!")
        help()
