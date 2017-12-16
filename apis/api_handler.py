
import pandas as pd
import json
import falcon

df = pd.read_csv('look/finalapi.csv').fillna('')

class DetailedInfoResource(object):
    def on_get(self, req, resp, val):
        param = req.url.split('/')[-2]
        doc = df[(df[param] == float(val))][['AGENCY_ID', 'PL_START_YEAR']].head(1).to_dict('list')

        # create json representation
        resp.body = json.dumps(doc, ensure_ascii=False)

        # not required as default status returned by framework in 200
        resp.status = falcon.HTTP_200