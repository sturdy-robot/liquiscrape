import json
import requests
import logging
from bs4 import BeautifulSoup


def get_requests(url):
    logging.info('Getting url')
    logging.info(url)
    res = requests.get(url)
    logging.debug(res)
    soup = BeautifulSoup(res.content, 'html.parser')
    teams_tables = soup.find_all('div', class_='lp-col-12')
    if teams_tables is None:
        logging.info('No table found')
    return teams_tables


def get_names(tables):
    regions = []
    for table in tables:
        teams = []
        region_name = table.find('h3').text.strip()
        inside_table = table.find('div', class_='panel-box-body')
        for team in inside_table.find_all('a'):
            team_name = team.text.strip()
            if not team_name:
                continue
            logging.debug('Team name:')
            logging.debug(team_name)
            teams.append(team_name)
        region = {
            'name': region_name,
            'teams': teams
        }
        regions.append(region.copy())

    return regions


def write_to_file(names):
    logging.info('Started writing to file')
    with open('teams_test.json', 'w', encoding='utf-8') as fp:
        json.dump(names, fp, sort_keys=True, indent=4)
    
    logging.info('Write successful')


def write_namestxt(names):
    logging.info('Writing to teams.txt')
    with open('teams.txt', 'w', encoding='utf-8') as fp:
        for name in names:
            for team in name['teams']:
                fp.write(team + '\n')
    
    logging.info('Write successful')


def main():
    logging.basicConfig(filename='webscraping.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')
    urls = [
        'https://liquipedia.net/leagueoflegends/Portal:Teams'
    ]

    teams = []
    for url in urls:
        data = get_requests(url)
        regions = get_names(data)
    
    write_to_file(regions)
    write_namestxt(regions)


if __name__ == '__main__':
    main()
