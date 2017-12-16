
import falcon

from .api_handler import DetailedInfoResource


api = application = falcon.API()

routes = DetailedInfoResource()

api.add_route('/routes/AGENCY_ID/{val}', routes)
api.add_route('/routes/PL_START_YEAR/{val}', routes)