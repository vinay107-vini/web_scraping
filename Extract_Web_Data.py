# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://stackoverflow.com/questions/tagged/python/')

# soup = BeautifulSoup(r.content, 'html.parser')

# question= soup.find_all('h3', class_="s-post-summary--content-title")
# answer=soup.find_all('div', class_="s-post-summary--content-excerpt")

# a=1
# for question_,answer_ in zip(question,answer):
#     print(f"{a})",question_.text.strip())
#     print(f"-> {answer_.text.strip()}")
#     a+=1






