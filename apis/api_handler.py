
import pandas as pd
import json
import falcon

df = pd.read_csv('apis/finalapi.csv').fillna('')

class DetailedInfoResource(object):
    def on_get(self, req, resp, val):
        param = req.url.split('/')[-2]

        try:
            doc = df[(df[param] == val)][['AGENCY_ID', 'MONTHS', 'PL_START_YEAR', 'STATE_ABBR']].head(2).to_dict('list')
        except:
            doc = df[(df[param] == float(val))][['AGENCY_ID', 'MONTHS', 'PL_START_YEAR', 'STATE_ABBR']].head(2).to_dict('list')

        # create json representation
        resp.body = json.dumps(doc, ensure_ascii=False)

        # not required as default status returned by framework in 200
        resp.status = falcon.HTTP_200