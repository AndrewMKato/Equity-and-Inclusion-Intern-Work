from wc_functions import wc, fq
import stop_words as sw

def main():

    stops: list = sw.get_stop_words('english')
    stops.extend(['UCR', 'Riverside', 'used', 'will'])
    tuple(stops)

    UCR_text_files = {
        'Classrooms': 'inc_classrooms.png',
        'Conversations': 'inc_conversations.png',
        'Language': 'inc_language.png',
        'Organizations': 'inc_organizations.png'
    }

    for file_keyword, output_title in UCR_text_files.items():
        wc(f'Inclusive_{file_keyword}_for_web.txt', output_title, chosen_stop_words=stops) # File name choice is dynamic.
        print(fq(f'Inclusive_{file_keyword}_for_web.txt', chosen_stop_words=stops))

if __name__ == '__main__':
    main()