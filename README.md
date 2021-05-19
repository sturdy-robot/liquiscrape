# Liquiscrape

This is a testing repository to scrape data from Liquipedia.

This repo scrapes LoL players and creates three files:

**names.json**: Scraped data from each LoL player.

**team.json**: Organizes players in their respective team rosters.

**names.txt**: just a txt file with nick names.

All of this data can be really useful in eSports Manager.

At one point I plan on introducing more data to each file, making it more compatible with eSM, and eSM will be able to generate a lot of things from these files.

## Running

There is some confusion in these files.

Run `main.py` to get the players.

`main_team.py` doesn't work quite right.

`attempt.py` uses the files generated in `main.py` to get the `teams.json`.

`try_teams.py` is a new way to get the teams from one of the liquipedia pages.

# License

```
Copyright 2021 Pedrenrique G. Guimarães

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
