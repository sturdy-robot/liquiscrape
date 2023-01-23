import json
import requests
import re
import logging
from bs4 import BeautifulSoup



def get_requests(url):
    logging.info('Getting url')
    logging.info(url)
    res = requests.get(url)
    logging.debug(res)
    soup = BeautifulSoup(res.content, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    if tables is None:
        logging.info('No table found')
    return tables


def get_names(tables, teams):
    for table in tables:
        player_roster = []
        tbody = table.find('tbody')
        team_name = tbody.find('th').text.strip()
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if not tds:
                continue
            logging.debug(tds)

            pl_id, real_name = [td.text.strip() for td in tds]

            logging.debug(pl_id)
            logging.debug(real_name)

            player_info = {
                'player': pl_id,
                'real_name': real_name
            }

            player_roster.append(player_info.copy())

        team_info = {
            'team_name': team_name,
            'roster': player_roster
        }

        teams.append(team_info.copy())


def write_to_file(names):
    logging.info('Started writing to file')
    with open('teams_main.json', 'w', encoding='utf-8') as fp:
        json.dump(names, fp, sort_keys=True, indent=4)
    
    logging.info('Write successful')


def write_namestxt(names):
    logging.info('Writing to teams_file.txt')
    with open('teams_file.txt', 'w', encoding='utf-8') as fp:
        for name in names:
            fp.write(name['team_name'] + '\n')
    
    logging.info('Write successful')


def main():
    logging.basicConfig(filename='webscraping.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')
    urls = [
        'https://liquipedia.net/leagueoflegends/Portal:Teams/Brazil',
        'https://liquipedia.net/leagueoflegends/Portal:Teams/Japan'
        'https://liquipedia.net/leagueoflegends/Portal:Teams/Korea',
        'https://liquipedia.net/leagueoflegends/Portal:Teams/China',
        'https://liquipedia.net/leagueoflegends/Portal:Teams/Latin_America',
        'https://liquipedia.net/leagueoflegends/Portal:Teams/North_America',
        'https://liquipedia.net/leagueoflegends/Portal:Teams/Europe',
        'https://liquipedia.net/leagueoflegends/Portal:Teams/Pacific',
        'https://liquipedia.net/leagueoflegends/Portal:Teams/Vietnam',
    ]

    r = []
    for url in urls:
        pattern = re.compile(r'https://liquipedia.net/leagueoflegends/Portal:Teams/(\w+)')
        region = re.match(pattern, url).group(1)
        if region == "Korea":
            region = "South Korea"
        reg = {
            "region": region,
            "teams": []
        }
        regions = get_requests(url)
        get_names(regions, reg["teams"])
        r.append(reg)
    
    write_to_file(r)
    # write_namestxt(teams)


if __name__ == '__main__':
    main()
