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
    
    # Decode the response content with UTF-8 encoding
    response.encoding = 'utf-8'
    content = response.text
    
    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')
    
    # Extract question name
    question_name = soup.select_one("div#__next h1.chakra-heading.css-1o1jsbj").text
    
    # Extract question difficultyiculty
    question_difficultyiculty = soup.select_one("div#__next span[class*='chakra-badge css-']").text
    
    # Extract question id
    question_id = url.split('/')[-1]
    
    # Extract all tags
    all_tags_elements = soup.select("div#__next div.chakra-stack.css-1ainr4z span[dir='rtl'].chakra-text.css-zvlevn")
    tags = [tag.text for tag in all_tags_elements if tag.text in correct_tags]
    
    return [question_name, question_difficultyiculty, 0, question_id, tags]



def insert_code(info, script, path):
    global a
    
    path_temp = os.path.join('.', 'Quera', a[info[1]], info[3])
    if not os.path.exists(path_temp):
        os.makedirs(path_temp)
    
    files_in_folder = os.listdir(path_temp)
    if len(files_in_folder) >= 1:
        for i in files_in_folder:

            with open(os.path.join(path_temp, i), 'r', encoding='utf-8') as f:
                t = f.readlines()
                
            if script == t:
                return
        
    text = ''.join(script)
    with open(os.path.join(path_temp, f'{info[3]}_{len(files_in_folder)+1}.py'), 'w', encoding='utf-8') as f:
        f.write(text)
    
    tags = ''
    for i in info[4]:
        tags += f'`{i}` '
        
    # text = 'count, id, name(link to question), score(link to answer), tags'
    text = f'-1 | {info[3]} | [{info[0]}](https://quera.org/problemset/{info[3]}) | [جواب]({path_temp}\) | {tags}|\n'
    
    update_csv(text, info[1], path)



def update_csv(text, difficulty, path):
    global a
    
    info = text.split(' | ')
    
    name = a[difficulty]
    with open(os.path.join(path, f'{name}.txt'), 'r', encoding='utf-8') as f:
        read_in_file = f.readlines()
            
    
    read_in_file = [[j for j in i.split(' | ')] for i in read_in_file]
    
    codes_number = [i[1] for i in read_in_file]
    if info[1] not in codes_number:
        read_in_file.append(info)
        
    read_in_file.sort(key=lambda x:int(x[1]))
    
    
    for i in range(1, len(read_in_file)+1):
        read_in_file[i-1][0] = '| ' + str(i)
    
    
    read_in_file = [' | '.join(i) for i in read_in_file]
    
    name = a[difficulty]
    with open(os.path.join(path, f'{name}.txt'), 'w', encoding='utf-8') as f:
            for item in read_in_file:
                f.write(item)


def update_table(path):
    global a
    read_in_file = []
    
    for i in a.values():
        with open(os.path.join(path, f'{i}.txt'), 'r', encoding='utf-8') as f:
            read_in_file.append(f.read())

    root_path = path.split('\\')
    root_path = '\\'.join(root_path[0:len(root_path)-1])
    
    with open(os.path.join(root_path, 'README.md'), 'r', encoding='utf-8') as f:
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
    
    with open(os.path.join(root_path, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(text)
    
    

    
if __name__ == '__main__':
    global a 
    a = {'ساده':'Easy', 'متوسط':'Mid-level', 'سخت':'Hard'}
    
    
    path = os.path.dirname(os.path.abspath(__file__))
    
    path_to_answer = input('Please enter path to your directory that all of your complete codes is there: ')

    files_in_folder = os.listdir(path_to_answer)
    for i in files_in_folder:
        read_in_files = []
        
        for j in a.values():
            with open(os.path.join(path, f'{j}.txt'), 'r', encoding='utf-8') as f:
                read = f.readlines()
                try:
                    temp = [(i.split(' | ')[1]+'.py') for i in read]
                    read_in_files += temp
                except:
                    pass
                
        with open(os.path.join(path_to_answer ,i), 'r', encoding='utf-8') as f:
            script = f.readlines()
            
        url = 'https://quera.org/problemset/'+i[:len(i)-3]
        info = scrap_web(url)
            
        if script[0] != '# '+url+'\n':
            script.insert(0, f"# {url}\n")
                
        insert_code(info, script, path)
            
    update_table(path)
    
    print('done!!')
    
    
    
    