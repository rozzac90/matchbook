"""
Sports as defined by Matchbook.
"""

from matchbook.enums import SportType


class Sport:
    """
    A sport as defined by Matchbook.
    """
    def __init__(self,  id_, name, type_=SportType.Sport):
        self.name = name
        self.type_ = type_
        self.id_ = id_


AmericanFootball = Sport(1, 'American Football')
Athletics = Sport(555636871580009, 'Athletics')
AustralianRules = Sport(112, 'Australian Rules')
Baseball = Sport(3, 'Baseball')
Basketball = Sport(4, 'Basketball')
Boxing = Sport(14, 'Boxing')
Cricket = Sport(110, 'Cricket')
CurrentEvents = Sport(11, 'Current Events')
Cycling = Sport(115, 'Cycling')
Darts = Sport(116, 'Darts')
GaelicFootball = Sport(117, 'Gaelic Football')
Golf = Sport(8, 'Golf')
GreyhoundRacing = Sport(241798357140019, 'Greyhound Racing')
HorseRacing = Sport(24735152712200, 'Horse Racing')
HorseRacingAntePost = Sport(222109340250019, 'Horse Racing (Ante Post)')
HorseRacingBeta = Sport(231138347942400, 'Horse Racing Beta')
Hurling = Sport(118, 'Hurling')
IceHockey = Sport(6, 'Ice Hockey')
Mma = Sport(126, 'MMA')
MotorSport = Sport(13, 'Motor Sport')
NcaaBasketball = Sport(5, 'NCAA Basketball')
NcaaFootball = Sport(2, 'NCAA Football')
Politics = Sport(385227477790005, 'Politics')
RugbyLeague = Sport(114, 'Rugby League')
RugbyUnion = Sport(18, 'Rugby Union')
Snooker = Sport(120, 'Snooker')
Soccer = Sport(15, 'Soccer')
TvSpecials = Sport(670369566180014, 'TV Specials')
Tennis = Sport(9, 'Tennis')
TestSport = Sport(502491395980009, 'Test Sport')
ESports = Sport(123, 'eSports')

All = [
    AmericanFootball,
    Athletics,
    AustralianRules,
    Baseball,
    Basketball,
    Boxing,
    Cricket,
    CurrentEvents,
    Cycling,
    Darts,
    GaelicFootball,
    Golf,
    GreyhoundRacing,
    HorseRacing,
    HorseRacingAntePost,
    HorseRacingBeta,
    Hurling,
    IceHockey,
    Mma,
    MotorSport,
    NcaaBasketball,
    NcaaFootball,
    Politics,
    RugbyLeague,
    RugbyUnion,
    Snooker,
    Soccer,
    TvSpecials,
    Tennis,
    TestSport,
    ESports,
]

_ID_SPORT_MAP = {
    sport.id_: sport for sport in All
}


def from_id(id_):
    """
    Gets a sport by its ID.
    :param id_: The sport's ID.
    :return: The sport.
    """
    return _ID_SPORT_MAP[id_]


def test(referencedata_path):
    import ast

    with open(referencedata_path) as f:
        sports_data = f.read()
        sports_data = ast.literal_eval(sports_data)
        sports_list = sports_data['sports']
        assert len(sports_list) == len(All)
        for sport_json in sports_list:
            sport_id = sport_json['id']
            sport = from_id(sport_id)
            assert sport_json['id'] == sport.id_
            assert sport_json['name'] == sport.name
            assert sport_json['type'] == sport.type_

    print('test passed.')
