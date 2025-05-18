import codecs
import re
def delete_html_tags(html_file:str, result_file:str='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
    clean_text = re.sub(r'<[^>]+>', '', html)
    with codecs.open(result_file, 'w', 'utf-8') as out:
        out.write(clean_text)

delete_html_tags('draft.html')
#################################################################################################################



from bs4 import BeautifulSoup
def delete_html_tags_no_spaces(html_file:str, result_file:str='cleaned_no_spaces.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator='\n')
    clean_text = '\n'.join([line for line in text.splitlines() if line.strip()])

    with codecs.open(result_file, 'w', 'utf-8') as out:
         out.write(clean_text)

delete_html_tags_no_spaces('draft.html')