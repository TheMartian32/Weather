"""
A simple script to find the weather of a given city in a country.

Returns:
    Float : Weather in fahrenheit.

Notes:

Set up will_rain method, and come up with a repeat message using the repeat snippet.

"""

import pyowm
from rich import print


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


def dynamic_weather():
    """
    A weather method to dynamically adjust
    to whatever the user needs.
    """

    owm = pyowm.OWM('69b10ec96289a50844dfe3a39e28670f')

    supported_types = ['sunrise', 'sunset',
                       'local weather', 'rain', 'fog', 'clouds']

    print(
        '\n[cyan]Forecast[/cyan] only goes up to [bold underline]three hours away[/bold underline] and all [bold underline]times are in GMT[/bold underline].')
    print('\nWhat [cyan]weather information[/cyan] do you want to get? (e.g, [red]rain[/red], [bold]fog[/bold], [yellow]sunrise/set[/yellow], etc.)',)
    what_weather = ask_for('\n: ', 'Error', str).lower()
    print(
        '\nPlease provide the [underline]city, then country. (e.g Napa, US)[/underline]')
    city = ask_for('\n: ', 'Error', str)
    country = ask_for('\n: ', 'Error', str)
    # timezone = ask_for('\n: ', 'Error', str)

    location = owm.weather_at_place(f'{city},{country}')
    weather = location.get_weather()

    if what_weather in supported_types[0]:
        # * GMT timezone
        print('\nThe [yellow]sun will rise[/yellow] at: ')
        #usr_timezone = pytz.timezone(f'{country}/{city}')
        print(weather.get_sunrise_time(timeformat='iso'))
    else:
        print('\nNot [bold]supported[/bold]')


if __name__ == '__main__':
    dynamic_weather()
