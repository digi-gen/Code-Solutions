import requests
from bs4 import BeautifulSoup
import os

def scrap_web(url):
    
    correct_tags = ['Python', 'برنامه‌نویسی پیشرفته', 'پایگاه داده', 'دانش‌آموزی', 
                    'طراحی الگوریتم', 'مبانی برنامه‌نویسی', 'هوش مصنوعی و سیستم‌های خبره', 'یادگیری ماشین',
                    'هوش مصنوعی', 'برنامه‌نویسی پویا', 'بهینه‌سازی', 'پازل', 'پیاده‌سازی', 'ترکیبیات', 'تقسیم و حل', 
                    'جست‌وجو', 'حریصانه', 'داده ساختار', 'درخت', 'رشته‌ها', 'ریاضیات', 'گراف', 'معمایی', 'نظریه اعداد', 
                    'هندسه', 'مقدماتی', 'خلاقانه' ]

    # Start a session
    session = requests.Session()
    
    # Get the page content
    response = session.get(url)
    response.raise_for_status()  # Ensure we notice bad responses
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract question name
    question_name = soup.select_one("div#__next h1.chakra-heading.css-1o1jsbj").text
    
    # Extract question difficulty
    question_difficulty = soup.select_one("div#__next span[class*='chakra-badge css-']").text
    
    # Extract question id
    question_id = url.split('/')[-1]
    
    # Extract all tags
    all_tags_elements = soup.select("div#__next div.chakra-stack.css-1ainr4z span[dir='rtl'].chakra-text.css-zvlevn")
    tags = [tag.text for tag in all_tags_elements if tag.text in correct_tags]
    
    return [question_name, question_difficulty, 0, question_id, tags]



def insert_code(info, script, path):
    
    a = {'ساده':'Easy', 'متوسط':'Mid-level', 'سخت':'Hard',}
    
    if not os.path.exists(f'./Quera/{a[info[1]]}/{info[3]}/'):
        os.makedirs(f'./Quera/{a[info[1]]}/{info[3]}/')
    
    
    files_in_folder = os.listdir(f'./Quera/{a[info[1]]}/{info[3]}/')
    if len(files_in_folder) >= 1:
        for i in files_in_folder:
            
            with open(f'./Quera/{a[info[1]]}/{info[3]}/{i}', 'r', encoding='utf-8') as f:
                t = f.readlines()
                
            if script == t:
                return
        
    text = ''.join(script)
    with open(f'./Quera/{a[info[1]]}/{info[3]}/{info[3]}_{len(files_in_folder)+1}.py', 'w', encoding='utf-8') as f:
        f.write(text)
    
    tags = ''
    for i in info[4]:
        tags += f'`{i}` '
        
    # text = 'count, id, name(link to question), score(link to answer), tags'
    text = f'-1 | {info[3]} | [{info[0]}](https://quera.org/problemset/{info[3]}) | [جواب](./Quera/{a[info[1]]}/{info[3]}/) | {tags}|\n'
    
    update_csv(text, info[1], path)



def update_csv(text, diff, path):
    info = text.split(' | ')
    
    if diff == 'ساده':
        with open(f'{path}/update codes automatically/simple.txt', 'r', encoding='utf-8') as f:
            read_in_file = f.readlines()
            
    elif diff == 'متوسط':
        with open(f'{path}/update codes automatically/mid.txt', 'r', encoding='utf-8') as f:
            read_in_file = f.readlines()
            
    elif diff == 'سخت':
        with open(f'{path}/update codes automatically/hard.txt', 'r', encoding='utf-8') as f:
            read_in_file = f.readlines()
            
            
    read_in_file = [[j for j in i.split(' | ')] for i in read_in_file]
    read_in_file.append(info)
    read_in_file.sort(key=lambda x:int(x[1]))
    
    
    for i in range(1, len(read_in_file)+1):
        read_in_file[i-1][0] = '| ' + str(i)
    
    
    read_in_file = [' | '.join(i) for i in read_in_file]
    
    if diff == 'ساده':
        with open(f'{path}/update codes automatically//simple.txt', 'w', encoding='utf-8') as f:
            for item in read_in_file:
                f.write(item)
            
    elif diff == 'متوسط':
        with open(f'{path}/update codes automatically/mid.txt', 'w', encoding='utf-8') as f:
            for item in read_in_file:
                f.write(item)
            
    elif diff == 'سخت':
        with open(f'{path}/update codes automatically/hard.txt', 'w', encoding='utf-8') as f:
            for item in read_in_file:
                f.write(item)
        


def update_table(path):
    
    read_in_file = []
    
    for i in ['simple.txt', 'mid.txt', 'hard.txt']:
        with open(f'{path}/update codes automatically/{i}', 'r', encoding='utf-8') as f:
            read_in_file.append(f.read())

    with open('./README.md', 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split('***\n')
        
    
    
    easy = text[3].split('| 1 |')
    easy[1] = read_in_file[0]
    text[3] = easy[0]+easy[1]+'\n[بازگشت به ابتدا :back:](#حل-سوالات-Quera)\n'
    
    mid = text[4].split('| 1 |')
    mid[1] = read_in_file[1]
    text[4] = mid[0]+mid[1]+'\n[بازگشت به ابتدا :back:](#حل-سوالات-Quera)\n'
    
    hard = text[5].split('| 1 |')
    hard[1] = read_in_file[2]
    text[5] = hard[0]+hard[1]+'\n[بازگشت به ابتدا :back:](#حل-سوالات-Quera)\n'
    
    text = '***\n'.join(text)
    
    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(text)
    
    

    
if __name__ == '__main__':
    
    
    path = os.getcwd()
    
    try:
        path.replace('update codes automatically/', '')
    except:
        pass
    
    path_to_answer = input('Please enter path to your directory that all of your complete codes is there: ')
    
    browser = webdriver.Chrome()

    files_in_folder = os.listdir(path_to_answer)
    for i in files_in_folder:
        read_in_files = []
        
        for j in ['simple.txt', 'mid.txt', 'hard.txt']:
            with open(f'{path}/update codes automatically/{j}', 'r', encoding='utf-8') as f:
                read = f.readlines()
                try:
                    temp = [(i.split(' | ')[1]+'.py') for i in read]
                    read_in_files += temp
                except:
                    pass
                
        if i not in [j for j in read_in_files]:
            with open(path_to_answer+'/'+i, 'r', encoding='utf-8') as f:
                script = f.readlines()
                
            url = 'https://quera.org/problemset/'+i[:len(i)-3]
            info = scrap_web(url)
                
            if script[0] != '# '+url+'\n':
                script.insert(0, f"# {url}\n")
                    
            insert_code(info, script, path)
            
    update_table(path)
    
    
    
    