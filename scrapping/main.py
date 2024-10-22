import pycountry 
from module.INTERPOL_SCRAPPING import *


def main():
    # for country in pycountry.countries:
    #     json_object = getData(payload, headers, country, 120, 0)
    #     loadJsonData(json_object)
    json_object = getData(payload, headers, pycountry.countries.get(alpha_2='RU'), 0, 120)

    return None


if __name__ == '__main__':
    main()