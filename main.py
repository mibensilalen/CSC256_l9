
import requests
import pytest
@pytest.fixture
def ddg_response():
   return requests.get('http://api.duckduckgo.com/?q=the-white-house/presidents/&format=json')

def test_presidents_in_response(ddg_response):
   data = ddg_response.json()
   related_topics = data['RelatedTopics']

   presidents = [ 'Washington','Madison','Monroe', 'Jackson', 'Van Buren','Harrison','Tyler','Polk','Taylor',
                  'Fillmore','Pierce','Buchanan','Lincoln','Johnson','Grant','Hayes',
                  'Garfield','Arthur','Cleveland','Harrison','McKinley','Roosevelt','Taft','Wilson',
                  'Harding','Coolidge','Hoover','Roosevelt','Truman','Eisenhower','Kennedy',
                  'Johnson','Nixon','Ford','Carter','Reagan','Bush','Clinton',
                  'Bush','Obama','Trump','Biden' ]
   for x in related_topics:
       if x[''] in presidents:
           presidents.remove(x[''])
   assert len(set(presidents)) == 0