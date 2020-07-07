"""
A simple script to find the weather of a given city in a country.

Returns:
    Float : Weather in fahrenheit.

Notes:

Set up will_rain method, and come up with a repeat message using the repeat snippet.

"""

import pyowm
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

    def __init__(self, city=None, country=None, timzone=None):
        self.city = city
        self.country = country
        self.timezone = timzone

    def weather(self):
        """
        Getting everything needed to present the user with the
        weather or any other information they request.
        """

        # * Location
        print(
            '\nPlease provide the [cyan underline]city, country, then timezone. (e.g Napa, US, PST)[/cyan underline]')
        self.city = ask_for('\n: ', 'Error', str)
        self.country = ask_for('\n: ', 'Error', str)
        self.timezone = ask_for('\n: ', 'Error', str)

        location = OWM.weather_at_place(f'{self.city},{self.country}')
        weather = location.get_weather()

        def get_weather():
            """
            A weather method to dynamically adjusts
            to whatever the user needs.
            """

            supported_types = ['sunrise', 'sunset',
                               'local weather', 'weather', 'rain', 'fog', 'clouds']

            # * Asking user what type of weather information they need
            print(
                '\n[cyan]Forecast[/cyan] only goes up to [bold underline]three hours away[/bold underline] and all [bold underline]times are in GMT[/bold underline].')
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
            if what_weather in supported_types[2] or supported_types[3]:

                print('\nFahrenheit [bold]or[/bold] Celsius? (Type c or f)')
                c_or_f = ask_for('\n: ', 'Error', str).lower()

                if c_or_f == 'f':

                    print('\nThe [cyan]weather[/cyan] is:')
                    print(weather.get_temperature('fahrenheit')['temp'])

                if c_or_f == 'c':

                    print('\nThe [cyan]weather[/cyan] is:')
                    print(weather.get_temperature('celsius')['temp'])

            # * Rain Forecast
            if what_weather in supported_types[4]:
                print('')
                print('')

            # * Fog
            if what_weather in supported_types[5]:
                pass

            # * Clouds
            if what_weather in supported_types[6]:
                pass

        get_weather()


GW = GetWeather()

if __name__ == '__main__':
    GW.weather()
    repeat = ''
    while True:
        # * Asks to repeat the script.
        repeat = input(
            '\nDo you need any more information? (Y/N): ').lower()
        if repeat[0] == 'y':
            GW.weather()
            continue
        if repeat[0] == 'n':
            break
