import json


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    
    return data


def extract_team_names(data):
    team_names = []
    for team in data:
        team_name = {'name': team['team']}
        if team_name not in team_names:
            team_names.append(team_name)
    
    return team_names


def compare_team_names_players(data, team_names):
    new_data = []
    for team in team_names:
        roster = []
        
        for player in data:
            if player['team'] == team['name']:
                player_dict = player.copy()
                player_dict.pop('team', None)
                roster.append(player_dict)
        
        team['roster'] = roster

        new_data.append(team.copy())
    
    return new_data


def write_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)


def main():
    data = read_json('names.json')
    team_names = extract_team_names(data)
    new_data = compare_team_names_players(data, team_names)

    write_to_file('teams.json', new_data)


if __name__ == '__main__':
    main()