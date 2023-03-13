import json


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        data = json.load(fp)

    return data


def compare_data(regions, teams):
    new_data = []
    for region in regions:
        teams_data = []
        for r_team in region['teams']:
            teams_data.extend(team for team in teams if r_team == team['team_name'])
        reg = {
            'region': region['name'],
            'teams': teams_data
        }

        new_data.append(reg)

    return new_data


def write_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


def main():
    regions = read_file('teams_test.json')
    teams = read_file('teams_main.json')
    new_data = compare_data(regions, teams)
    write_to_file(new_data, 'data.json')


if __name__ == '__main__':
    main()
