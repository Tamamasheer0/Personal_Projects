from bs4 import BeautifulSoup as bs
import requests as req

# Web Scraping Function That Returns Desired Web Links For Each Team
# [Function] Params: <String> Link Description as Shown on Website


def espn_team_info_links(link_desc, Verbose=False):
    _base_url = 'http://www.espn.com'
    _htmldoc = req.get(_base_url + '/mlb/teams').text
    _soup = bs(_htmldoc, 'html.parser')
    _span_tags = _soup.find_all('span', class_='TeamLinks__Link n9 nowrap')

    _team_urls = {}
    for _span in _span_tags:
        _link = _span.a['href'].strip()
        _info = _link.split('/')

        if f'{link_desc.strip()}' in _info:
            _team = _info[-1].strip().title()
            _team_url = _base_url + _link
            _team_urls[_team] = _team_url
            if Verbose:
                print(_team, '\n', _team_url)
    return _team_urls

    # Web Scraping Function That Returns Basic Player Info & Links to Personal Page on ESPN
# [Function] Params: <Dictionary> Team Roster
#               Key: Team Name
#             Value: Link to Team Roster


def espn_player_info_links(roster, Verbose=False):
    _player_links = {}
    for _team, _url in roster.items():
        _htmldoc = req.get(_url).text
        _soup = bs(_htmldoc, 'html.parser')
        _span_tags = _soup.find_all('span', class_='Table2__td--headshot')

        for _span in _span_tags:
            try:
                _link = _span.a['href'].strip()
                _info = _link.split('/')

                if 'player' in _info:
                    _pID = _info[-1].strip()
                    _pName = _span.a.find('figure')['title'].strip().title()
                    _t = _url.split('/').index('name') + 1
                    _tID = _url.split('/')[_t].upper()

                    if _pID not in _player_links:
                        _player_links[_pID] = {
                            'id': _pID,
                            'name': _pName,
                            'team': _team,
                            'tid': _tID,
                            'link': _link
                        }
                        if Verbose:
                            print(f'ID: {_pID}, Name: {_pName}, Team: {_team}\n\tLink: {_link}')

            except TypeError:
                if Verbose:
                    print('\n<Skip> No Player Link Found\n')

    return _player_links


# Web Scraping Function That Returns Dictionary With Player's Gen Info Data
# [Function] Params: <String> Link to ESPN's Player Page
#            Return: <Dictionary> Player Profile Info

def get_player_info(p_link):
    _htmldoc = req.get(p_link).text
    _soup = bs(_htmldoc, 'html.parser')
    _li_tags = _soup.find_all('li')
    try:
        _num = _li_tags[0].text.split(' ')[0][1:]
        _pos = _li_tags[0].text.split(' ')[1]
        _thr = _li_tags[1].text.split(',')[0][-1]
        _bat = _li_tags[1].text.split(',')[1][-1]
        _team = _li_tags[2].text
        _bday = _li_tags[3].text[10:].split('(')[0].strip()
        _age = _li_tags[3].text[10:].split('(')[1].split(':')[1][:-1].strip()
        _city = _li_tags[4].text[10:].split(',')[0].strip()
        _exp = _li_tags[5].text[10:]
        _col = _li_tags[6].text[7:]
        _hght = _li_tags[7].text.split(',')[0][5:].strip()
        _wght = _li_tags[7].text.split(',')[1].strip()

    except IndexError:
        return {
            'pid': None,
            'fname': None,
            'lname': None,
            'age': 0,
            'height': None,
            'weight': None,
            'birthday': None,
            'city': None,
            'number': -1,
            'position': None,
            'exp': None,
            'team': None,
            'tid': None,
            'throw': None,
            'bat': None,
            'college': None,
        }
    return {
        'pid': None,
        'fname': None,
        'lname': None,
        'age': int(_age),
        'height': _hght,
        'weight': _wght,
        'birthday': _bday,
        'city': _city,
        'number': int(_num),
        'position': _pos,
        'exp': _exp,
        'team': _team,
        'tid': None,
        'throw': _thr,
        'bat': _bat,
        'college': _col,
    }
