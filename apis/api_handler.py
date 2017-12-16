
import pandas as pd
import json
import falcon

df = pd.read_csv('apis/finalapi.csv').fillna('')

class DetailedInfoResource(object):
    def on_get(self, req, resp, val):
        param = req.url.split('/')[-2]

        try:
            doc = df[(df[param] == val)][['AGENCY_ID', 'MONTHS', param, 'STATE_ABBR']].to_dict('list')
        except:
            doc = df[(df[param] == float(val))][['AGENCY_ID', 'MONTHS', param, 'STATE_ABBR']].to_dict('list')

        # create json representation
        resp.body = json.dumps(doc, ensure_ascii=False)

        # not required as default status returned by framework in 200
        resp.status = falcon.HTTP_200

class ReportResource(object):
    def on_get(self, req, resp, start_year, end_year):
        param1 = req.url.split('/')[4]
        param2 = req.url.split('/')[6]

        try:
            doc = df[(df[param1] == start_year) & (df[param2] == end_year)][['AGENCY_ID', 'PRIMARY_AGENCY_ID', 'PROD_ABBR', 'PROD_LINE', 'NB_WRTN_PREM_AMT', 'WRTN_PREM_AMT', 'PREV_WRTN_PREM_AMT', 'PRD_ERND_PREM_AMT']].to_dict('list')
        except:
            doc = df[(df[param1] == float(start_year)) & (df[param2] == float(end_year))][['AGENCY_ID', 'PRIMARY_AGENCY_ID', 'PROD_ABBR', 'PROD_LINE', 'NB_WRTN_PREM_AMT', 'WRTN_PREM_AMT', 'PREV_WRTN_PREM_AMT', 'PRD_ERND_PREM_AMT']].to_dict('list')

        # create json representation
        resp.body = json.dumps(doc, ensure_ascii=False)

        # not required as default status returned by framework in 200
        resp.status = falcon.HTTP_200

        pd.DataFrame(doc).to_csv('reports/' + param1.split('_')[0] + '-report.csv', index=False)