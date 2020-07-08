"""
A simple script to find the weather of a given city in a country.

Returns:
    Float : Weather in fahrenheit.

Notes:
"""

import sys
import pyowm
import pytz
from datetime import datetime, timedelta
from rich import print

OWM = pyowm.OWM('69b10ec96289a50844dfe3a39e28670f')


def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue
        return inp


class GetWeather():
    """
    Getting weather by using the Open Weather API
    """

    def __init__(self, city=None, country=None, region=None):
        self.city = city
        self.country = country
        self.region = region

    def convert_timzone(self):
        print(
            'Please enter the [cyan]region, then the country[/cyan]. This is for converting to your [bold]timezone[/bold].')
        self.region = ask_for('\n: ', 'Error', str)
        self.country = ask_for('\n: ', 'Error', str)
        convert_zone = pytz.timezone(f'{self.country}/{self.region}')
        return convert_zone

    def weather(self):
        """
        Getting everything needed to present the user with the
        weather or any other information they request.
        """

        # * Location
        try:
            # * getting location from user and then storing it for later reference.
            print(
                '\nPlease provide the [cyan underline]city, country, then timezone. (e.g Napa, US, Western)[/cyan underline]')
            self.city = ask_for('\n: ', 'Error', str)

            location = OWM.weather_at_place(f'{self.city},{self.country}')
            forecast = OWM.three_hours_forecast(f'{self.city},{self.country}')
            weather = location.get_weather()
        except:
            # * If they entered the wrong information, or didn't spell it correctly it will terminate the whole script.
            print('\n[red]Error[/red]. Couldnt find that location.')
            sys.exit()

        def get_weather():
            """
            A weather method to dynamically adjusts
            to whatever the user needs.
            """

            supported_types = ['sunrise', 'sunset',
                               'weather', 'rain', 'fog', 'clouds']

            # * Asking user what type of weather information they need
            print(
                '\n[cyan]Forecast[/cyan] only goes up to [bold underline]5 days, in 3 hour increments[/bold underline] and all [bold underline]times are in GMT[/bold underline].')
            print('\nWhat [cyan]weather information[/cyan] do you want to get? (e.g, [red]rain[/red], [bold]fog[/bold], [yellow]sunrise/set[/yellow], etc.)',)
            what_weather = ask_for('\n: ', 'Error', str).lower()

            # * Checking what user inputted into the script
            # * Sunrise
            if what_weather in supported_types[0]:

                # * GMT timezone
                print('\nThe [yellow]sun will rise[/yellow] at: ')
                print(weather.get_sunrise_time(timeformat='iso'))

            # * Sunset
            if what_weather in supported_types[1]:

                print('\nThe [yellow]sun will set[/yellow] at: ')
                print(weather.get_sunset_time(timeformat='iso'))

            # * Local weather
            if what_weather in supported_types[2]:

                print('\nFahrenheit [bold]or[/bold] Celsius? (Type c or f)')
                c_or_f = ask_for('\n: ', 'Error', str).lower()

                # * Celsius or fahrenheit
                if c_or_f == 'f':

                    print('\nThe [cyan]weather[/cyan] is:')
                    print(weather.get_temperature('fahrenheit')['temp'])

                if c_or_f == 'c':

                    print('\nThe [cyan]weather[/cyan] is:')
                    print(weather.get_temperature('celsius')['temp'])

            # * Rain Forecast
            if what_weather in supported_types[3]:
                print(
                    '\nThis will return [green]true[/green] or [red]false[/red].')
                print(forecast.will_have_rain())

            # * Fog
            if what_weather in supported_types[4]:
                print(
                    '\nThis will return [green]true[/green] or [red]false[/red].')
                print(forecast.will_have_fog())

            # * Clouds
            if what_weather in supported_types[5]:
                print(
                    '\nThis will return [green]true[/green] or [red]false[/red].')
                print(forecast.will_have_clouds())

            # * Checks if the user inputted anything that was supported
            # * If it isn't supported it prints an error.
            elif what_weather not in supported_types:
                print('\n[red]Error[/red], not supported.')

        get_weather()


GW = GetWeather()

if __name__ == '__main__':
    GW.weather()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        print(
            '\nTyping [green]Y[/green] will restart the script, typing [red]N[/red] will terminate it.')
        repeat = input(
            '\nDo you need any more information? (Y/N): ').lower()
        if repeat[0] == 'y':
            GW.weather()
            continue
        if repeat[0] == 'n':
            break
