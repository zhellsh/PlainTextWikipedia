from dewiki_functions import *
wiki_xml_file = '../simplewiki.xml'  # update this
json_save_dir = '../out/wiki.json'

if __name__ == '__main__':
    process_file_text(wiki_xml_file, json_save_dir)
