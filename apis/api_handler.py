
import pandas as pd
import json
import falcon
from db.conn import engine


class DetailedInfoResource(object):
    def on_get(self, req, resp, val):
        param = req.url.split('/')[-2]

        doc = pd.read_sql(
            'select "AGENCY_ID", "MONTHS", "PL_START_YEAR", "STATE_ABBR" from detailed_table where "{0}" = {1}' .format(param, val), engine
        ).to_dict('list')

        # create json representation
        resp.body = json.dumps(doc, ensure_ascii=False)

        # not required as default status returned by framework in 200
        resp.status = falcon.HTTP_200

class ReportResource(object):
    def on_get(self, req, resp, start_year, end_year):
        param1 = req.url.split('/')[4]
        param2 = req.url.split('/')[6]

        doc = pd.read_sql(
            'select "AGENCY_ID", "PRIMARY_AGENCY_ID", "PROD_ABBR", "PROD_LINE", "NB_WRTN_PREM_AMT", "WRTN_PREM_AMT", "PREV_WRTN_PREM_AMT", "PRD_ERND_PREM_AMT" from detailed_table where "{0}" = {1} and "{2}" = {3}' .format(param1, start_year, param2, end_year), engine
        ).to_dict('list')
        
        # create json representation
        resp.body = json.dumps(doc, ensure_ascii = False)

        # not required as default status returned by framework in 200
        resp.status = falcon.HTTP_200

        pd.DataFrame(doc).to_csv('reports/' + param1.split('_')[0] + '-report.csv', index=False)