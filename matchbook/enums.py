class Side:
    '''
    Specify what order types to return in order requests, dependant on exchange type, Default will return all.

    :var back: orders backing the runner, suitable for exchange type back-lay.
    :var lay: orders backing the runner, suitable for exchange type back-lay.
    :var win: orders to win, suitable for exchange type binary.
    :var loss: orders to loss, suitable for exchange type binary.
    '''
    Back = 'back'
    Lay = 'lay'
    Win = 'win'
    Loss = 'loss'
    All = None
    Default = All


class ExchangeType:
    '''
    Format of odds/liquidity returned on both sides.
    '''
    Binary = 'binary'
    BackLay = 'back-lay'
    Default = BackLay


class Status:
    '''
    Specify the order status to return, Default will return all.

    :var matched:  Offer has been partially or fully matched. Returned status will be "matched" for fully matched or "open" for partially matched.
    :var unmatched: Offer still has some stake available to be matched but may be "open" or "paused".
    :var cancelled: Offer has been cancelled and can no longer be matched.
    :var open: Initial state of offer before being partially matched, fully matched or edited.
    :var paused: Offer still has some remaining stake but cannot be matched until unpaused.
    :var expired: Offer has expired and can no longer be matched.

    '''
    Matched = 'matched'
    Unmatched = 'unmatched'
    Cancelled = 'cancelled'
    Expired = 'expired'
    Open = 'open'
    Paused = 'paused'
    All = None
    Default = All


class OddsType:
    '''
    Odds format to be used/returned.

    :var US: american odds format.
    :var DECIMAL: decimal odds format.
    :var %: probability.
    :var HK: hong kong odds format.
    :var MALAY: malay odds format.
    :var INDO: indonesian odds format.

    '''
    US = 'US'
    Decimal = 'DECIMAL'
    Prob = '%'
    HongKong = 'HK'
    Malay = 'MALAY'
    Indo = 'INDO'
    Default = Decimal


class Currency:
    '''
    Currency selection for use in placing bets.

    :var EUR: EUR
    :var USD: USD
    :var GBP: GBP
    '''
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'
    Default = EUR


class MarketStates:
    '''
    Filter by market state.

    :var open: market is currently open.
    :var suspended: market is currently suspended.
    '''
    Open = 'open'
    Suspended = 'suspended'
    All = None
    Default = All


class RunnerStates:
    '''
    Filter by runner state

    :var open: market is currently open.
    :var suspended: market is currently suspended.
    '''
    Open = 'open'
    Suspended = 'suspended'
    All = None
    Default = All


class MarketType:
    '''
    Filter by market type

    :var multirunner: market has multirunner type.
    :var binary: market has a binary outcome.
    '''
    MultipleRunners = 'multirunner'
    Binary = 'binary'
    All = None
    Default = All


class GradingType:
    '''
    Filter by grading type i.e. how a market settles.

    :var asian-handicap: A dual handicap market, where each handicap is graded as per point spread below.
    :var high-score-wins: Markets where the team scoring the most points or goals are graded as the winner.
    :var low-score-wins: Markets where the team scoring the least points or goals are graded as the winner.
    :var point-spread: Markets where the score in the game, and the handicap value, are factored in for grading purposes.
    :var point-total: Markets where the total of all scores in the game decide the grading.
    :var single-winner-wins: Other markets where the grading is decided manually.
    '''
    AsianHandicap = 'asian-handicap'
    HighScore = 'high-score-wins'
    LowScore = 'low-score-wins'
    PointSpread = 'point-spread'
    PointTotal = 'point-total'
    SingleWinner = 'single-winner-wins'
    All = None
    Default = All


class MarketOrder:
    '''
    Determine how results are ordered when returned.

    :var start asc: order by start time ascending.
    :var start desc: order by start time descending.
    '''
    Ascending = 'start asc'
    Descending = 'start desc'
    Default = Ascending


class Boolean:
    '''
    booleans in api are lower case string type rather than python boolean.
    '''
    T = 'true'
    F = 'false'


class PriceOrder:
    '''
    Determine how prices are ordered when returned.

    :var price asc: order by price ascending.
    :var price desc: oder by price descending.
    '''
    Ascending = 'price asc'
    Descending = 'price desc'
    Default = Descending


class MarketNames:
    '''
    Market names which can be used to filter results.

    :TODO Check all market names for validity.
    '''
    Match = 'match'
    PointSpread = 'point spread'
    OverUnder = 'over/under'
    GameLine = 'gameline'
    Match1H = 'match 1H'
    GameLine1H = 'gameline 1H'
    OverUnder1H = 'over/under 1H'
    Winner = 'Winner'
    ML = 'Money Line'
    ml = 'moneyline'
    gl = 'goal line'
    NumberRounds = 'Number of Rounds'
    TotalRounds = 'Total Rounds'
    Totals = 'totals'
    ThreeWay = 'Three Way'
    Total = 'Total'
    RaceWinner = 'Race Winner'
    All = None
    Default = All


class SequenceOrder:
    '''
    Determine how markets are ordered when returned.

    :var start asc: sort by start time ascending.
    :var start desc: sort by start time descending.
    :var seq asc: sort in sequential order ascending.
    :var seq desc: sort in sequential order descending.
    '''
    StartAscending = 'start asc'
    StartDescending = 'start desc'
    SeqAscending = 'seq asc'
    SeqDescending = 'seq desc'
    Default = SeqAscending


class SportsOrder:
    '''
    Determine how sports are ordered when returned.

    :var name asc: order alphabetically ascending.
    :var name desc: order alphabetically descending.
    :var id asc: order by id number ascending.
    :var id desc: order by id number descending.
    '''
    NameAsc = 'name asc'
    NameDesc = 'name desc'
    IDAsc = 'id asc'
    IDDEsc = 'id desc'
    Default = NameAsc


class SportStatus:
    '''
    Filter sport search by status of sport.

    :var active: there are markets active on this sport.
    :var pending: there are no active markets on this sport.
    '''
    Active = 'active'
    Pending = 'pending'
    Default = Active


class BetsOrder:
    '''
    Determine the order in which bet report is sorted.

    :var event asc: event name alphabetically ascending.
    :var event desc: event name alphabetically descending.
    :var selection asc: selection name alphabetically ascending.
    :var selection desc: selection name alphabetically descending.
    :var market asc: market name alphabetically ascending.
    :var market desc: market name alphabetically descending.
    :var bet-id asc: bet id numerically ascending.
    :var bet-id desc: bet id numerically descending.
    '''
    EventAsc = 'event asc'
    EventDesc = 'event desc'
    SelectionAsc = 'selection asc'
    SelectionDesc = 'selection desc'
    MarketAsc = 'market asc'
    MarketDesc = 'market desc'
    IDAsc = 'bet-id asc'
    IDDesc = 'bet-id desc'


class BetStatusFilter:
    '''
    Filter bet report to return matched bets only or now.

    :var true: return only matched bets.
    :var false: return all bets.
    '''
    MatchedOnly = 'true'
    All = 'false'
    Default = MatchedOnly


class BetGrouping:
    '''
    Group betting report to return average odds and total stake on runners or all bets individually.

    :var true: group bets by runner and average odds, sum stakes
    :var false: return all bets individually
    '''
    GroupBets = 'true'
    IndividualBets = 'false'
    Default = IndividualBets


class SizeFilter:
    """
    Filter to only include data where a specified dataset meets this criteria.

    :var greater-than: values are greater than a specific cutoff.
    :var less-than: values are less than a specific cutoff.
    :var equals: values are equal to a specific value.
    """
    GreaterThan = 'greater-than'
    LessThan = 'less-than'
    Equal = 'equals'
    All = None
    Default = All


class PeriodFilter:
    """
    Period to filter reports to include.

    :var today: include only today.
    :var yesterday: include only yesterday
    :var 1-day: include one calendar day.
    :var 2-day: include two calendar day.
    :var week: include one calendar week.
    :var month: include one calendar month.
    :var 1-month: include one calendar month.
    :var 3-month: include three calendar months.
    """
    Today = 'today'
    Yesterday = 'yesterday'
    Days1 = '1-day'
    Days2 = '2-day'
    Week = 'week'
    Month = 'month'
    Month1 = '1-month'
    Month3 = '3-month'
    All = None
    Default = All


class TransactionCategories:
    """
    Categories a transaction can fall under.

    :var casino: transaction was made on the casino site.
    :var exchange: transaction was made on the exchange site.
    :var collosus: NFI.
    """
    Casino = 'casino'
    Exchange = 'exchange'
    Collosus = 'collosus'
    Default = Exchange


class TransactionTypes:
    """
    Types of transactions.
    
    :var
    """
    Payout = 'payout'
    Commission = 'commission'
    Transfer = 'transfer'
    Cancel = 'cancel'
    Manual = 'manual'
    Bonus = 'bonus'
    All = None
    Default = All


class AggregationType:
    """
    Method of aggregation to be used in grouping bets.
    """
    Average = 'average'
    Summary = 'summary'
    Default = Average


class SportType:
    """
    Types of sports.
    """
    Sport = "SPORT"
