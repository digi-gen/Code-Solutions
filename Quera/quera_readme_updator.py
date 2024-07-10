""" this python script is for updating the quera readme file tables of question after any question is added.

    simply run this file and give what info it asks about your solution.

    Warning! don't modify this file without complete knowledge about its implementation
"""
from re import compile, match

from typing import List
from os import path, rename


class QueraQuestion:
    quera_question_link_prefix = 'https://quera.org/problemset/'
    quera_question_pattern = compile(rf'^{quera_question_link_prefix}(?P<quera_id>\d+)/?$')
    all_possible_tags = [
        'Search',
        'Divide & Conquer',
        'Dynamic Programming',
        'Greedy',
        'Geometry',
        'Mathematics',
        'Enigmatic',
        'Strings',
        'Graph',
        'Data Structures',
        'Creative',
        'Numbers Theory',
        'Tree',
        'Combinatorics',
        'Implementation',
        'Puzzle',
        'Optimization',
        'Data Base',
        'AI',
        'Machine Learning',
        'Data Analyzing',
        'AI & Expert Systems',
        'Programming Fundamentals',
        'Algorithm Design',
        'Students',
        'Image Processing',
        'Advanced Programming',
        'Android',
        'C#',
        'DevOps',
        'Django',
        'Front-End',
        'Git',
        'Golang',
        'Java',
        'Laravel',
        'Linux',
        'PHP',
        'Python',
        'React',
        'Spring',
    ]

    quera_id: str

    tags: List[str]

    def __init__(self, link: str):
        self.name: str = self.get_name()
        self.link: str = QueraQuestion.get_validated_link(link)
        self.quera_id: str = self.get_quera_id()
        self.tags: List[str] = self.get_tags()
        self.difficulty: str = self.get_difficulty()
        self.solution_algorithm_method = self.get_solution_algorithm_method()
        self.is_solved: bool = self.get_is_solved()

    @classmethod
    def get_validated_link(cls, link: str) -> str:
        if QueraQuestion.is_valid_quera_link(link):
            return link
        else:
            raise ValueError('Invalid question link')

    def get_quera_id(self) -> str:
        """ returns the quera id wich is located in end of the question link"""
        question_match = QueraQuestion.quera_question_pattern.match(self.link)
        return question_match.group('quera_id')
        pass

    def get_tags(self):
        for i, tag in enumerate(QueraQuestion.all_possible_tags):
            print(f'    [{i}] : {tag}')

        question_tag_nums = input('\n enter number of question tags from list above,'
                                  '\n separated by comma (like 1,2,3) : ')
        question_tags: List[str] = []
        for tag_number in question_tag_nums.split(','):
            tag_number = int(tag_number.strip())
            question_tags.append(QueraQuestion.all_possible_tags[tag_number])

        return question_tags

    def get_solution_algorithm_method(self) -> str:
        """
        ask the solution algorithm method from CLI
        :returns empty string or user input
        """
        return input('\n\n please enter your solution algorithm method'
                     '\n (Greedy, Recursive, Dynamic ... ) you can left it empty: ')

    @staticmethod
    def is_valid_quera_link(link: str):
        """ checks if the question link matches the question pattern or not """
        return True if match(QueraQuestion.quera_question_pattern, link) else False

    def get_name(self):
        return input('\n\n please enter your question name\n' +
                     ' (please copy the name from question page and enter it here:')

    def get_difficulty(self):
        difficulties = ['Easy', 'Mid level', 'Hard']
        difficulty_i = int(input('\n\n enter your question difficulty number \n'
                           '0: Easy\n'
                           '1: Mid level\n'
                           '2: Hard\n'))

        return difficulties[difficulty_i]

    def get_tags_string_for_readme_file(self) -> str:
        """
        :return: a string or tags with format '`{tag1}`</br>`{tag2}</br>`{tag3}`...'
        """
        tags_string = f'`{self.tags.pop(0)}`'
        for tag in self.tags:
            tags_string += f'</br>`{tag}`'
        return tags_string

    def get_is_solved(self) -> bool:
        user_respond = input('Do you solved this question completely? (y/n) ')
        return True if (user_respond == 'y' or user_respond == 'Y') else False


all_possible_languages = [
    'C++',
    'C',
    'Python 3.8',
    'Python 2',
    'Pypy 3',
    'Kotlin',
    'Javascript',
    'Php 8',
    'C#',
    'Php 7',
    'Java 8',
    'Java 17',
    'Mono C#',
    'Node.js',
    'Perl',
    'Go',
    'Ruby',
    'Rust',
    'Obj-C',
    'Typescript',
    'Swift',
    'Haskell',
    'F#',
]

question_link = ''
language_of_solution = ''
solution_file_path = ''


def get_language_of_solution() -> str:
    for i, language in enumerate(all_possible_languages):
        print(f'    [{i}]: {language}')

    language_i = int(input('\n\n Enter solution programming language:'))
    return all_possible_languages[language_i]


def fix_directory_of_solution_file(file_path: str, ques: QueraQuestion) -> str:
    file_path = clean_path(file_path)
    if not path.exists(file_path):
        raise FileNotFoundError(' your file path does not exist')

    current_name = path.basename(file_path)
    extension = path.splitext(current_name)[1]

    new_file_path = rf'./{ques.difficulty}/{ques.quera_id}/{ques.quera_id}{extension}'
    try:
        rename(file_path, new_file_path)
    except FileExistsError:
        new_file_path = rf'./{ques.difficulty}/{ques.quera_id}/{ques.quera_id}_1{extension}'
        rename(file_path, new_file_path)
    return new_file_path


def clean_path(file_path: str) -> str:
    cleaned = file_path.strip(' ').strip('"')
    return cleaned


def inject_info_in_readme(question: QueraQuestion, solution_file_path: str, language_of_solution: str):
    solved_status = 'Solved' if question.is_solved else 'notSolved'
    readme_file_path = './Quera.md'

    anchor_line = f'<!--#{question.difficulty} {solved_status}#-->\n'

    with open(readme_file_path, 'r', encoding='utf-8') as readme_file:
        lines = readme_file.readlines()
    for i, line in enumerate(lines):
        if line == anchor_line:
            print('matched with line', i)
            line_to_inject = get_table_row_info_to_inject(question, solution_file_path, language_of_solution)
            line_to_inject += '\n' + anchor_line
            lines[i] = line_to_inject

    with open(readme_file_path, 'w', encoding='utf-8') as readme_file:
        readme_file.writelines(lines)


def get_table_row_info_to_inject(question: QueraQuestion, solution_file_path: str, language_of_solution: str) -> str:
    name_field = f'[{question.name}]({question.link})'
    solution_file_field = f'[{language_of_solution}]({solution_file_path})'
    algorithm_method_field = f'`{question.solution_algorithm_method}`' if question.solution_algorithm_method else '`--`'
    question_tags_field = question.get_tags_string_for_readme_file()
    quera_id = question.quera_id
    return (f'|{name_field}'
            f'|{solution_file_field}'
            f'|{algorithm_method_field}'
            f'|{question_tags_field}'
            f'|{quera_id}|')

if __name__ == '__main__':

    question_link = input('\n\ncopy and enter your question link address: ')
    question = QueraQuestion(question_link)
    language_of_solution = get_language_of_solution()
    solution_file_path = input('\n\n Enter solution solution file path in system here '
                               '\n path must contains filename and its extension :\n')
    estimated_file_path = f'./{question.difficulty}/{question.quera_id}/'

    if path.exists(estimated_file_path):
        respond = input('There is already a solution for this question, do you have a new solution ? (y/n) : ')
        if not (respond == 'y'):
            exit(1)

    new_solution_path = fix_directory_of_solution_file(solution_file_path, question)
    inject_info_in_readme(question, new_solution_path, language_of_solution)



