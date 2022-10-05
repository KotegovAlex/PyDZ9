from pyowm import OWM
from pyowm.utils.config import get_default_config

def weather(city):
    owm = OWM('a15943b9de17ee15503fca01e6762916')
    config_dict = get_default_config()
    config_dict['language'] = 'ru'
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place(city)
    w = obs.weather

    temp = w.temperature('celsius')['temp']

    wind = w.wind()['speed'] 

    pressure_dict = w.barometric_pressure(unit='inHg')
    press = pressure_dict['press']
    # cl = w.clouds
    # dt = w.detailed_status

    return (f'''В городе {city} сейчас:
    Температура {round(temp)} C, 
    Ветер {wind} м/с, 
    Давление {round(press*25.4)} мм рт.ст.''')