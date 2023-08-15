import logging
import urllib


log = logging.getLogger(__name__)


def parse_basic_info(x):
    integers = ['port', 'err', 'pv']
    booleans = ['pow', 'led']
    parse_data(x, integers=integers, booleans=booleans)
    x['name'] = urllib.parse.unquote(x['name'])
    return x


def parse_sensor_info(x):
    integers = ['err']
    temps = ['hhum', 'htemp', 'otemp']
    parse_data(x, integers=integers, temps=temps)
    return x


ctrl_integers = 'mode'
ctrl_temps = 'stemp'
ctrl_booleans = 'pow'

def parse_control_info(x):
    parse_data(x, integers=ctrl_integers, temps=ctrl_temps, booleans=ctrl_booleans)
    return x

def format_control_info(x):
    format_data(x, integers=ctrl_integers, temps=ctrl_temps, booleans=ctrl_booleans)
    return x


def parse_data(x, integers=[],
                  booleans=[],
                  temps=[]):

    try:
        x[integers] = int(x[integers])
    except ValueError as e:
        log.exception("failed to parse field '{}': {}".format(integers, e.message))

    try:
        x[booleans] = bool(int(x[booleans]))
    except ValueError as e:
        log.exception("Failed to parse field '{}': {}".format(booleans, e.message))

    try:
        x[temps] = parse_temperature(x[temps])
    except ValueError:
        log.exception(("Failed to parse field {{'{}':'{}'}}."
                        "A temperature was expected").format(temps, x[temps]))
        pass


def format_data(x, strict=True,
                integers=[],
                booleans=[],
                temps=[]):

    try:
        x[integers] = str(int(x[integers]))
    except KeyError:
        if not strict:
            pass

    try:
        x[booleans] = str(int(bool(x[booleans])))
    except KeyError:
        if not strict:
            pass

    try:
        x[temps] = str(float(x[temps]))
    except KeyError:
        if not strict:
            pass


def parse_temperature(temp):
        try:
            return float(temp)
        except ValueError:
            if temp == '-' or temp == '--':
                return None
            else:
                raise