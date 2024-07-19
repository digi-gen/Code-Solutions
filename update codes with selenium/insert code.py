from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time

def scrap_web(url, username, passeord):
    
    correct_tags = ['Python', 'برنامه‌نویسی پیشرفته', 'پایگاه داده', 'دانش‌آموزی', 
                    'طراحی الگوریتم', 'مبانی برنامه‌نویسی', 'هوش مصنوعی و سیستم‌های خبره', 'یادگیری ماشین',
                    'هوش مصنوعی', 'برنامه‌نویسی پویا', 'بهینه‌سازی', 'پازل', 'پیاده‌سازی', 'ترکیبیات', 'تقسیم و حل', 
                    'جست‌وجو', 'حریصانه', 'داده ساختار', 'درخت', 'رشته‌ها', 'ریاضیات', 'گراف', 'معمایی', 'نظریه اعداد', 
                    'هندسه', 'مقدماتی' ]

    browser.get(url)
    
    time.sleep(1)
    guestion_name = browser.find_element(By.XPATH,".//div[@id='__next']//h1[@class='chakra-heading css-1o1jsbj']").text
    guestion_difficulty = browser.find_element(By.XPATH,".//div[@id='__next']//span[contains(@class, 'chakra-badge css-')]").text
    
    time.sleep(1)
    browser.find_element(By.XPATH,".//div[@id='__next']//button[@class='chakra-tabs__tab css-3wuodn'][2]").click()
    guestion_score = browser.find_element(By.XPATH,".//div[@id='__next']//main//tr[@class='css-0'][1]//td[4]//span").text
    all_tags = browser.find_elements(By.XPATH,".//div[@id='__next']//div[@class='chakra-stack css-1ainr4z']//span[@dir='rtl' and @class='chakra-text css-zvlevn']")
    
    question_id = url.split('/')
    question_id = question_id[len(question_id)-1]
    
    
    tags = []
    for i in range(len(all_tags)):
        if all_tags[i].text in correct_tags:
            tags.append(all_tags[i].text)
    
    return [guestion_name, guestion_difficulty, guestion_score, question_id, tags]



def insert_code(info, script):
    
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
    text = f'-1 | {info[3]} | [{info[0]}](https://quera.org/problemset/{info[3]}) | [{info[2]}](./Quera/{a[info[1]]}/{info[3]}/{info[3]}) | {tags}|\n'
    
    update_csv(text, info[1])



def update_csv(text, diff):
    info = text.split(' | ')
    
    if diff == 'ساده':
        with open('./update codes with selenium/simple.txt', 'r', encoding='utf-8') as f:
            read_in_file = f.readlines()
            
    elif diff == 'متوسط':
        with open('./update codes with selenium/mid.txt', 'r', encoding='utf-8') as f:
            read_in_file = f.readlines()
            
    elif diff == 'سخت':
        with open('./update codes with selenium/hard.txt', 'r', encoding='utf-8') as f:
            read_in_file = f.readlines()
            
            
    read_in_file = [[j for j in i.split(' | ')] for i in read_in_file]
    read_in_file.append(info)
    read_in_file.sort(key=lambda x:int(x[1]))
    
    
    for i in range(1, len(read_in_file)+1):
        read_in_file[i-1][0] = str(i)
    
    
    read_in_file = [' | '.join(i) for i in read_in_file]
    
    if diff == 'ساده':
        with open('./update codes with selenium/simple.txt', 'w', encoding='utf-8') as f:
            for item in read_in_file:
                f.write(item)
            
    elif diff == 'متوسط':
        with open('./update codes with selenium/mid.txt', 'w', encoding='utf-8') as f:
            for item in read_in_file:
                f.write(item)
            
    elif diff == 'سخت':
        with open('./update codes with selenium/hard.txt', 'w', encoding='utf-8') as f:
            for item in read_in_file:
                f.write(item)
        


def update_table():
    
    read_in_file = []
    for i in ['simple.txt', 'mid.txt', 'hard.txt']:
        with open(f'./update codes with selenium/{i}', 'r', encoding='utf-8') as f:
            read_in_file.append(f.read())

    with open('./README.md', 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.split('***\n')
        
    
    
    easy = text[3].split('1 |')
    easy[1] = read_in_file[0]
    text[3] = easy[0]+easy[1]+'\n[بازگشت به ابتدا :back:](#حل-سوالات-Quera)'
    
    mid = text[4].split('1 |')
    mid[1] = read_in_file[1]
    text[4] = mid[0]+mid[1]+'\n[بازگشت به ابتدا :back:](#حل-سوالات-Quera)'
    
    hard = text[5].split('1 |')
    hard[1] = read_in_file[2]
    text[5] = hard[0]+hard[1]+'\n[بازگشت به ابتدا :back:](#حل-سوالات-Quera)'
    
    text = '***\n'.join(text)
    
    with open('./README.md', 'w', encoding='utf-8') as f:
        f.write(text)
    
    

    
if __name__ == '__main__':
    
    
    path_to_answer = input('Please enter path to your directory that all of your complete codes is there: ')
    
    user_name = 'mr.manmahmood@gmail.com'
    password = 'feS2U4X4iQxLSSQ'
    
    #user_name = input("Please enter your Quera user name: ")
    #password = input("Please enter your Quera password: ")
    
    browser = webdriver.Chrome()
    browser.get('https://quera.org/accounts/login')  
    temp = browser.find_element(By.NAME,'login')
    temp.send_keys(user_name)
    temp = browser.find_element(By.NAME,'password')
    temp.send_keys(password)
    browser.find_element(By.XPATH,".//button[@class='ui fluid large primary submit button']").click()
    


    files_in_folder = os.listdir(path_to_answer)
        
    for i in files_in_folder:
        read_in_files = []
        
        for j in ['simple.txt', 'mid.txt', 'hard.txt']:
            with open(f'./update codes with selenium/{j}', 'r', encoding='utf-8') as f:
                read = f.readlines()
                try:
                    read_in_files.append([(i.split(' | ')[1]+'.py') for i in read][0])
                except:
                    pass

        with open(path_to_answer+'/'+i, 'r', encoding='utf-8') as f:
            script = f.readlines()
            
        url = 'https://quera.org/problemset/'+i[:len(i)-3]
        info = scrap_web(url, user_name, password)
            
        if script[0] != '# '+url+'\n':
            script.insert(0, f"# {url}\n")
                
        insert_code(info, script)
            
        
        
    
    update_table()
    
    
    
    