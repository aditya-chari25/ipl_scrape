from bs4 import BeautifulSoup
import requests
html_text = requests.get('https://www.espncricinfo.com/live-cricket-match-results').text

# print(html_text)
soup = BeautifulSoup(html_text,'lxml')                  
jobs = soup.find_all('div',class_="ds-px-4 ds-py-3");

for score in jobs:
    scores_team = score.find_all('div',class_="ds-text-compact-s ds-text-typo-title")
    score_1 = scores_team[0].strong.text
    score_2 = scores_team[1].strong.text
    link = score.find('a',class_='').get('href')
    twoteams = score.find_all('p',class_='ds-text-tight-m ds-font-bold ds-capitalize')
    descp = score.find('div',class_='ds-text-tight-xs ds-truncate ds-text-ui-typo-mid')
    winner = score.find('p',class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo-title').span.text
    team_1 = twoteams[0]
    team_2 = twoteams[1]
    if(descp.a.span.text=='Indian Premier League'):
        print("https://www.espncricinfo.com"+link)
        print('Match Type:',descp.a.span.text)
        print('Match_Result:',team_1.text," vs ",team_2.text)
        print(team_1.text," : ",score_1)
        print(team_2.text," : ",scores_team[1].span.text,"  ",score_2)
        print(winner);
        print('\n')
        new_soup = requests.get("https://www.espncricinfo.com"+link).text
        new_souper = BeautifulSoup(new_soup,'lxml')
        jobs = new_souper.find_all('div',class_="ds-grow");