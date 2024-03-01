import re
from collections import defaultdict


def solution(word, pages):
    answer = 0
    max_score = 0
    
    indexes = defaultdict(int)
    basic_scores = defaultdict(int)
    total_scores = defaultdict(int)
    external_urls = defaultdict(set)
    internal_urls = defaultdict(set)
    
    for index, page in enumerate(pages):
        word, page = word.lower(), page.lower()
        
        url = re.search(r'(<meta property.+content=")(https://\S*)"/>', page).group(2)
        basic_scores[url] += sum(x == word for x in re.findall('[a-z]+', page))
        indexes[url] = index
        
        for ex_url in re.findall(r'<a href="(https://\S*)">', page):
            external_urls[url].add(ex_url)
            internal_urls[ex_url].add(url)
        
    for url in basic_scores:
        link_score = basic_scores[url] + sum(basic_scores[target] / len(external_urls[target]) for target in internal_urls[url])
        
        if max_score < link_score:
            max_score = link_score
            answer = indexes[url]

    return answer
