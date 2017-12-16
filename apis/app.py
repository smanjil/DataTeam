
import falcon

from .api_handler import (
    DetailedInfoResource,
    ReportResource
)


api = application = falcon.API()


# detailed view
detail_routes = DetailedInfoResource()

# agency (must be a number - int)
api.add_route('/detail/AGENCY_ID/{val}', detail_routes)

# month (must be a number - int)
api.add_route('/detail/MONTHS/{val}', detail_routes)

# year (must be a 4 digit number - int)
api.add_route('/detail/PL_START_YEAR/{val}', detail_routes)

# state (2 letter upper case word - e.g: IN)
api.add_route('/detail/STATE_ABBR/{val}', detail_routes)


# report view
report_routes = ReportResource()

# PL
api.add_route('/report/PL_START_YEAR/{start_year}/PL_END_YEAR/{end_year}', report_routes)

# COMMISIONS
api.add_route('/report/COMMISIONS_START_YEAR/{start_year}/COMMISIONS_END_YEAR/{end_year}', report_routes)

# CL
api.add_route('/report/CL_START_YEAR/{start_year}/CL_END_YEAR/{end_year}', report_routes)

# ACTIVITY
api.add_route('/report/ACTIVITY_NOTES_START_YEAR/{start_year}/ACTIVITY_NOTES_END_YEAR/{end_year}', report_routes)   