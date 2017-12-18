
import requests
import pandas as pd
import json
import falcon
from falcon import testing
import pytest


final_api_df = pd.read_csv('input/finalapi.csv')


@pytest.fixture
def client():
    return testing.TestClient(api)


def test_detail_info(client):
    doc = final_api_df[final_api_df['AGENCY_ID'] == 3][["AGENCY_ID", "MONTHS", "PL_START_YEAR", "STATE_ABBR"]].to_dict('list')

    response = requests.get('http://localhost:8000/detail/AGENCY_ID/3')
    result_doc = json.loads(response.text)

    assert result_doc.keys() == doc.keys()
    assert str(response.status_code) + ' OK' == falcon.HTTP_OK


def test_report(client):
    doc = final_api_df[(final_api_df['PL_START_YEAR'] == 99999) & (final_api_df['PL_END_YEAR'] == 99999)][["AGENCY_ID", "PRIMARY_AGENCY_ID", "PROD_ABBR", "PROD_LINE", "NB_WRTN_PREM_AMT", "WRTN_PREM_AMT", "PREV_WRTN_PREM_AMT", "PRD_ERND_PREM_AMT"]].to_dict('list')

    response = requests.get('http://localhost:8000/report/PL_START_YEAR/99999/PL_END_YEAR/99999')
    result_doc = json.loads(response.text)

    assert result_doc.keys() == doc.keys()
    assert str(response.status_code) + ' OK' == falcon.HTTP_OK