import pyowm
from rich import print
import pytz
import re

"""
A simple script to find the weather of a given city in a country.

Returns:
    Float : Weather in fahrenheit.

Notes:

Set up will_rain method, and come up with a repeat message using the repeat snippet.

"""

owm = pyowm.OWM('API key') # TODO: Put your open weather api key here.


class UI_Inputs():

    """
    A class responsible for the inputs in the UI and basically anything that requires
    either the UI or inputs.
    """

    def ask_for(self, prompt, error_msg=None, _type=None):
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


ask = UI_Inputs()


class Weather():

    #! Do not use, will be deprecated soon.
    def current_temp(self):

        print(
            '\nWhat [green]city[/green] do you want to get the [cyan]weather[/cyan] from?')

        city = ask.ask_for(
            '\n: ', "Couldn't find the weather for that city.", str)

        print(
            '\nwhat [green]country[/green] do you want to get the [cyan]weather[/cyan] from?')
        country = ask.ask_for('\n: ',
                              "Couldn't find the weather for that country.", str)

        try:
            city_country = owm.weather_at_place(f'{city}, {country}')
            weather = city_country.get_weather()
            print('\nThis is the [green]current temperature[/green] :')
            current_temp = print(weather.get_temperature('fahrenheit')['temp'])
            return current_temp
        except:
            print(
                '\nAn [bold red]error[/bold red] occurred, could not find the [cyan]weather[/cyan].')

    def dynamic_weather(self):

        print(
            '\n[cyan]Forecast[/cyan] only goes up to [bold underline]three hours away[/bold underline].')
        print('\nWhat [cyan]weather information[/cyan] do you want to get? (e.g, [red]rain[/red], [bold]fog[/bold], [yellow]sunrise/set[/yellow], etc.)',)
        what_weather = ask.ask_for('\n: ', 'Error', str)
        print(
            '\nPlease provide the [underline]city, then country.[/underline]')
        city = ask.ask_for('\n: ', 'Error', str)
        country = ask.ask_for('\n: ', 'Error', str)

        location = owm.weather_at_place(f'{city},{country}')
        weather = location.get_weather()



weather = Weather()

if __name__ == '__main__':
    weather.dynamic_weather()
