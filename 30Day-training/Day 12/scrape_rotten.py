import os
import requests
import webbrowser
import pandas as pd

from requests_html import HTML

Base_dir = os.path.dirname(os.path.abspath(__file__))
print(Base_dir)

url = "https://www.rottentomatoes.com/top/bestofrt/"

def open_page(year = None):
    webbrowser.open(url)
    print(url)

def url_to_text(save = False, name = None):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"{name}.html", "w") as f:
                f.write(html_text)
    return html_text
    #return None

def parse_and_extract(name = None):
    html_text = url_to_text(save = True, name = name)
    r_html = HTML(html=html_text)
    table_class = ".table"
    r_table = r_html.find(table_class)

    #table_data = []
    table_data_dicts = []
    header_names = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find("th")
    
    for x in header_cols:
        header_names.append(x.text)
    #header_names = [x.text for x in header_cols]
    #print(header_names)

    for row in rows[1:]:
        cols = row.find("td")
        #row_data =[]
        row_dict_data = {}
        for i, cols in enumerate(cols):
            #print(i, cols.text, "\n")
            """dictionaries can be used in case all the header_names are unique 
            but in case of common header names the data will be overwritten for 
            programme with lists refer to scrape.py"""
            header_name = header_names[i]
            row_dict_data[header_name] = cols.text
            #row_data.append(cols.text)
            
        print(row_dict_data)
        #table_data.append(row_data)
        table_data_dicts.append(row_dict_data)
    #df = pd.DataFrame(table_data, columns = header_names)
    df = pd.DataFrame(table_data_dicts)

    path = os.path.join(Base_dir, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, f"{name}.csv")
    df.to_csv(filepath, index=False)
    return True


if __name__ == "__main__":
    name = "rotten"
    parse_and_extract(name = name)