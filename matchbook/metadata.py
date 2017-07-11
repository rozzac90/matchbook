import pandas as pd
from pandas.io.json import json_normalize
from matchbook.utils import clean_time
import numpy as np
import re


def clean_bet_report(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_bets_report

    :param df: MatchbookAPI.MatchbookAPI.get_bets_report raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned bet report.
    :rtype: Pandas.Dataframe

    """
    if 'bets' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'bets')
        df.rename(columns={'id':'offer-id'}, inplace=True)
    for _ in ['submitted-at', 'placed-at', 'settled-at']:
        if _ in df.columns:
            df[_] = clean_time(df[_])
    return df


def clean_commission_report(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_commission_report

    :param df: MatchbookAPI.MatchbookAPI.get_commission_report raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned commission report.
    :rtype: Pandas.Dataframe

    """
    if 'sub-totals' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'sub-totals')
    if 'settled-at' in df.columns:
        df['settled-at'] = clean_time(df['settled-at'])
    if 'placed-at' in df.columns:
        df['placed-at'] = clean_time(df['placed-at'])
    return df


def clean_transaction_report(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_transactions_report

    :param df: MatchbookAPI.MatchbookAPI.get_transactions_report raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned transactions report.
    :rtype: Pandas.Dataframe

    """
    if 'transactions' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'transactions')
    return df


def clean_orders(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_orders

    :param df: MatchbookAPI.MatchbookAPI.get_orders raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned orders report.
    :rtype: Pandas.Dataframe

    """
    if 'offers' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'offers')
        df.rename(columns={'id': 'offer-id'}, inplace=True)
    if 'matched-bets' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'matched-bets')
        df.rename(columns={'id': 'bet-id'}, inplace=True)
    if 'created-at' in df.columns:
        df['created-at'] = clean_time(df['created-at'])
    return df


def clean_settlement_report(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_settlement_report

    :param df: MatchbookAPI.MatchbookAPI.get_settlement_report raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned settlement report.
    :rtype: Pandas.Dataframe

    """
    if 'markets' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'markets')
    if 'runners' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'runners')
    if 'settled-at' in df.columns:
        df['settled-at'] = clean_time(df['settled-at'])
    return df


def parse_meta_tags(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_navigation

    :param df: MatchbookAPI.MatchbookAPI.get_navigation raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned navigation data.
    :rtype: Pandas.Dataframe

    """
    if 'meta-tags' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'meta-tags')
        df.rename(columns={'id': 'tree-id1', 'name': 'tree-name1', 'url-name': 'tree-url1'}, inplace=True)
    if 'meta-tags' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'meta-tags')
        df.rename(columns={'id': 'type1-id', 'type': 'type1', 'name': 'type1-name', 'url-name': 'type1-url-name'},
                  inplace=True)
    if 'tree-id' in df.columns:
        df.drop('tree-id', axis=1, inplace=True)
    if 'meta-tags' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'meta-tags')
        df.rename(columns={'id': 'type2-id', 'type': 'type2', 'name': 'type2-name', 'url-name': 'type2-url-name'},
                  inplace=True)
    if 'meta-tags' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'meta-tags')
        df.rename(columns={'id': 'type3-id', 'type': 'type3', 'name': 'type3-name', 'url-name': 'type3-url-name'},
                  inplace=True)
    if 'meta-tags' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'meta-tags')
    return df


def split_pricedata(df):
    """
    Splits prices dictionary into individual columns by level.

    :param df: dataframe containing the pricing information to split.
    :type df: Dataframe
    :returns: pricing information.
    :rtype: Pandas.Series
    """
    p_d = {}
    back_count = 0
    lay_count = 0
    for price in df.prices:
        if price['side'] == 'back':
            back_count += 1
            p_d['Back' + str(back_count)] = price['odds']
            p_d['BackSize' + str(back_count)] = price['available-amount']
            #p_d['Back' + str(price['odds'])] = price['available-amount']
        elif price['side'] == 'lay':
            lay_count += 1
            p_d['Lay' + str(lay_count)] = price['odds']
            p_d['LaySize' + str(lay_count)] = price['available-amount']
            #p_d['Lay' + str(price['odds'])] = price['available-amount']
        else:
            continue
    return pd.Series(p_d)


def clean_event_col_types(df):
    """
    Clean specific columns returned from events requests.

    :param df: data returned from events requests.
    :type df: Pandas.Dataframe
    :returns: data with clean start, handicap and asian-handicap columns.
    :rtype: Pandas.Dataframe

    """
    all_cols = df.columns
    if 'start' in all_cols:
        df['start'] = clean_time(df['start'])
    if 'handicap' in all_cols:
        df['handicap'] = df.handicap.apply(lambda x: float(x) if x != '' else np.nan)
    if 'asian-handicap' in all_cols:
        df['asian-handicap'] = df['asian-handicap'].apply(lambda x:
                                                          np.mean([float(y) for y in re.findall('\d\.\d', x)]) *
                                                          (-1 if '-' in x else 1))
    return df


def parse_event_data(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_events or MatchbookAPI.MatchbookAPI.get_event_allmarkets.

    :param df: MatchbookAPI.MatchbookAPI.get_events or MatchbookAPI.MatchbookAPI.get_event_allmarkets raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned events data breakdown.
    :rtype: Pandas.Dataframe

    """
    if 'events' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'events')
    df.rename(columns={'id': 'event-id', 'name': 'event-name'}, inplace=True)
    if 'category-id' in df.columns:
        df['category-id'] = df['category-id'].apply(lambda x: x[0])
    if 'meta-tags' in df.columns:
        df.drop('meta-tags', axis=1, inplace=True)
    if 'markets' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'markets')
        df.rename(columns={'id': 'market-id', 'name': 'market-name'}, inplace=True)
    if 'runners' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'runners')
        df.rename(columns={'id': 'runner-id', 'name': 'runner-name'}, inplace=True)
    if 'prices' in df.columns:
        df = pd.concat([df, df.apply(split_pricedata, axis=1)], axis=1)
        df.drop('prices', axis=1, inplace=True)
    return df


def parse_single_market(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_event_singlemarket or MatchbookAPI.MatchbookAPI.get_event_marketrunners.

    :param df: MatchbookAPI.MatchbookAPI.get_event_singlemarket or MatchbookAPI.MatchbookAPI.get_event_marketrunners raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned events data breakdown.
    :rtype: Pandas.Dataframe

    """
    df.rename(columns={'id': 'market-id', 'name': 'market-name'}, inplace=True)
    if 'runners' in df.columns:
        df = df.pipe(parser_function, sculpt_col, 'runners')
        df.rename(columns={'id': 'runner-id', 'name': 'runner-name'}, inplace=True)
    if 'prices' in df.columns:
        df = pd.concat([df, df.apply(split_pricedata, axis=1)], axis=1)
        df.drop('prices', axis=1, inplace=True)
    return df


def parse_single_runner(df):
    """
    Clean raw data returned from MatchbookAPI.MatchbookAPI.get_event_singlerunner.

    :param df: MatchbookAPI.MatchbookAPI.get_event_singlerunner raw data.
    :type df: Pandas.Dataframe
    :returns: cleaned events data breakdown.
    :rtype: Pandas.Dataframe

    """
    df.rename(columns={'id': 'runner-id', 'name': 'runner-name'}, inplace=True)
    if 'prices' in df.columns:
        df = pd.concat([df, df.apply(split_pricedata, axis=1)], axis=1)
        df.drop('prices', axis=1, inplace=True)
    return df


def parser_function(df, parsing_function, col_name):
    """
    Parse a specified dataframe column when provided with parsing breakdowns to use.

    :param df: dataframe which contains the column to be parsed
    :type df: Dataframe
    :param parsing_function: function to parse the specified col_name using.
    :type parsing_function: func
    :param col_name: column name in df that is to be parsed.
    :returns: flattened dataframe
    :rtype: Dataframe

    """
    df[col_name] = df[col_name].map(lambda x: pd.DataFrame() if len(x) == 0 else json_normalize(x))
    df = df.apply(parsing_function, args=(col_name,), axis=1)
    df = pd.concat([x for x in df[col_name].tolist()], ignore_index=True)
    df = df.fillna('')
    return df


def sculpt_col(df, col_name):
    """
    Flattens Dataframe where column is of type dataframe, applied cell by cell.

    :param df:
    :type df: dataframe row
    :param col_name: name of the column which is to be flattened.
    :type col_name: str
    :returns: flattened dataframe
    :rtype: Dataframe

    """
    try:
        if len(df[col_name]) > 0:
            for key in df.keys().tolist():
                if key != col_name:
                    df[col_name][key] = df[key]
        else:
            keys = df.keys().tolist()
            keys.pop(keys.index(col_name))
            df[col_name] = pd.DataFrame(columns=[key for key in keys], data=[[df[key] for key in keys]])
    except:
        raise ValueError(df[col_name])
    return df
