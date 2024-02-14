from dewiki_functions import *
wiki_xml_file = '../simplewiki-latest-pages-articles.xml'
json_save_dir = '../out/wiki.json'

if __name__ == '__main__':
    process_file_text(wiki_xml_file, json_save_dir)
