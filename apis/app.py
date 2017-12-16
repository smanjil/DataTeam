
import falcon

from .api_handler import DetailedInfoResource


api = application = falcon.API()

routes = DetailedInfoResource()

# agency (must be a number - int)
api.add_route('/routes/AGENCY_ID/{val}', routes)

# month (must be a number - int)
api.add_route('/routes/MONTHS/{val}', routes)

# year (must be a 4 digit number - int)
api.add_route('/routes/PL_START_YEAR/{val}', routes)

# state (2 letter upper case word - e.g: IN)
api.add_route('/routes/STATE_ABBR/{val}', routes)