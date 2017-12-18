
import pandas as pd
from db.conn import engine


def save_detailed_info(final_api_df):
    final_api_df = final_api_df[final_api_df['AGENCY_ID'] == 3]
    final_api_df.to_sql('detailed_table', engine, if_exists = 'replace', index = False)


def save_summarized_info(final_api_df, *args):
    # agentwise prodlines
    agentwise_prod_lines = final_api_df.groupby(args[0])['PROD_LINE'].count().to_frame(name = 'agentwise_prodlines').reset_index()
    agentwise_prod_lines.to_sql('agencywise_prod_lines', engine, if_exists = 'replace', index = False)

    # agentwise premium amounts
    agentwise_prem_amounts = final_api_df.groupby(args[0][0])[['AGENCY_ID', 'NB_WRTN_PREM_AMT', 'WRTN_PREM_AMT', 'PREV_WRTN_PREM_AMT', 'PRD_ERND_PREM_AMT']]\
                                .sum()
    agentwise_prem_amounts.to_sql('agencywise_prem_amounts', engine, if_exists = 'replace', index = False)    


if __name__ == '__main__':
    final_api_df = pd.read_csv('input/finalapi.csv')

    # save detailed informations
    save_detailed_info(final_api_df)

    # save summarized informations
    grouping_columns = ['AGENCY_ID', 'PROD_LINE']
    save_summarized_info(final_api_df, grouping_columns)