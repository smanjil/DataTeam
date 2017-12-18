# DataTeam


-- install requirements using (pip install -r requirements.txt)

the input file is placed in input/

save_df_to_db.py (python save_df_to_db.py)
  - this code save the final api df to postgres db in detail and summarized form. 
  - the connection string for local as well as heroku is provided in db/conn.py


used falcon API to build REST api 
  - different routes as per requirements and their handlers are defined in apis/app.py
  - apis/api_handler.py defines the handler for those respective routes defined in apis/app.py, and does the sql read operation and present it as json
  - apis/api_handler has a report info handler which saves the df to csv, it is stored in reports/


to make successfull use of api:
  - from the app folder, run "gunicorn --reload apis.app", have used gunicorn server to listen to http requests.
  - to make a api call after gunicorn started with no error: 
    - http localhost:8000/detail/MONTHS/8 (detailed info)
    - only available for params like "AGENCY_ID, MONTHS, PL_START_YEAR, STATE_ABBR"
  - http localhost:8000/report/CL_START_YEAR/2013/CL_END_YEAR/99999  (report, saves csv)
    - available for "PL_START_YEAR .. PL_END_YEAR, COMMISIONS_START_YEAR .. COMMISIONS_END_YEAR, CL_START_YEAR .. CL_END_YEAR, ACTIVITY_NOTES_START_YEAR .. ACTIVITY_NOTES_END_YEAR" date ranges..

have deployed on heroku
  - to verify: https://datateamse.herokuapp.com/report/PL_START_YEAR/99999/PL_END_YEAR/99999 
              : https://datateamse.herokuapp.com/detail/AGENCY_ID/3
  - heroku limited the usage of pandas df to sql, which could not load all records to df, so I have filtered out for agency_id 3 and stored in detail_table.
  - the reports file could not be stored in Amazon S3, as I do not have the subscription.
  - tried to store in /tmp/ inside heroku app, but with no errors, it did not get stored there as well.
  

have used pytest module to write some unit tests.
  - can be found in tests/test_app.py
  - to run, from project folder just type "pytest" and hit enter, the test should pass.
  - checked the keys returned from the queries and in actual df, and the status code
  
