import json
import uuid
import requests
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
        logging.debug('No table found')
    return tables

def get_names(tables, names):
    for table in tables:
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if not tds:
                continue
            nationality = tds[0].find('span', class_='flag').find('a').attrs['title']
            player_name, real_name, team, _ = [td.text.strip() for td in tds[:5]]
            
            player_info = {
                'id': uuid.uuid4().hex,
                'player': player_name,
                'nationality': nationality,
                'real_name': real_name,
                'team': team
            }

            logging.debug(player_name)
            logging.debug(real_name)
            logging.debug(team)

            names.append(player_info)

def sort_players_by_team(names):
    logging.info('Sorting players by teams')
    names.sort(key=lambda x: x['team'])

def write_to_file(names):
    logging.info('Started writing to file')
    with open('names.json', 'w', encoding='utf-8') as fp:
        json.dump(names, fp, sort_keys=True, indent=4)
    
    logging.info('Write successful')

def write_namestxt(names):
    logging.info('Writing to names.txt')
    with open('names.txt', 'w', encoding='utf-8') as fp:
        for name in names:
            fp.write(name['player_id'] + '\n')
    
    logging.info('Write succesful')

def main():
    logging.basicConfig(filename='webscraping.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')
    urls = [
        'https://liquipedia.net/leagueoflegends/Portal:Players/Korea',
        'https://liquipedia.net/leagueoflegends/Portal:Players/China',
        'https://liquipedia.net/leagueoflegends/Portal:Players/South_America',
        'https://liquipedia.net/leagueoflegends/Portal:Players/North_America',
        'https://liquipedia.net/leagueoflegends/Portal:Players/Europe/West',
        'https://liquipedia.net/leagueoflegends/Portal:Players/Europe/Nordic',
        'https://liquipedia.net/leagueoflegends/Portal:Players/Europe/South',
        'https://liquipedia.net/leagueoflegends/Portal:Players/Europe/Balkan',
        'https://liquipedia.net/leagueoflegends/Portal:Players/Asia',
        'https://liquipedia.net/leagueoflegends/Portal:Players/Oceania',
        'https://liquipedia.net/leagueoflegends/Portal:Players/Africa',
        'https://liquipedia.net/leagueoflegends/Portal:Players/CIS',
    ]

    names = []
    for url in urls:
        tables = get_requests(url)
        get_names(tables, names)
    
    sort_players_by_team(names)
    write_to_file(names)
    # write_namestxt(names)

if __name__ == '__main__':
    main()