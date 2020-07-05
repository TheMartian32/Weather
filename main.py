import pyowm
from rich import print 

"""
A simple script to find the weather of a given city in a country.

Returns:
    Float : Weather in fahrenheit.
"""


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

    def current_local_temp(self):

        print(
            '\nWhat [green]city[/green] do you want to get the [cyan]weather[/cyan] from?')
        city = ask.ask_for(
            '\n: ', "Couldn't find the weather for that city.", str)

        print(
            '\nwhat [green]country[/green] do you want to get the [cyan]weather[/cyan] from?')
        country = ask.ask_for('\n: ',
                              "Couldn't find the weather for that country.", str)

        try:
            owm = pyowm.OWM('69b10ec96289a50844dfe3a39e28670f')
            city_country = owm.weather_at_place(f'{city}, {country}')
            weather = city_country.get_weather()
            print('\nThis is the [green]current temperature[/green] :')
            current_temp = print(weather.get_temperature('fahrenheit')['temp'])
            return current_temp
        except:
            print(
                '\nAn [red]error[/red] occurred, could not find the [cyan]weather[/cyan].')


weather = Weather()

if __name__ == '__main__':
    weather.current_local_temp()
