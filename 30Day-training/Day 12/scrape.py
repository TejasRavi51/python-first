import os
import sys
import datetime
import requests
import webbrowser
import pandas as pd

from requests_html import HTML

Base_dir = os.path.dirname(os.path.abspath(__file__))
print(Base_dir)

now = datetime.datetime.now()
print(now)

url = "https://www.boxofficemojo.com/year/world/"

def open_page(year = None):
    new_url = url + f"{year}"
    webbrowser.open(new_url)
    print(new_url)

def url_to_text(save = False, year = None):
    #new_url = url + f"{year}"
    new_url = "https://www.rottentomatoes.com/top/bestofrt/"
    r = requests.get(new_url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", "w") as f:
                f.write(html_text)
    return html_text
    #return None

def parse_and_extract():
    html_text = url_to_text(save = True, year = start_year)
    r_html = HTML(html=html_text)
    table_class = ".table"
    r_table = r_html.find(table_class)

    table_data = []
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
    print(header_names)

    for row in rows[1:]:
        cols = row.find("td")
        row_data =[]
        row_dict_data = {}
        for i, cols in enumerate(cols):
            print(i, cols.text,"\n")   
            header_name = header_names[i]

if __name__ == "__main__":
    #url2 = "https://www.rottentomatoes.com/top/bestofrt/"
    if len(sys.argv) == 2:
        try:
            start_year = int(sys.argv[1])                 #try to concert the argument into integer 
            assert start_year >= 1977 and start_year <= 2020    #asserting the given year is in the valid range
        except:
            print("Please enter a valid year from 1977 to 2020")
    
    elif len(sys.argv) == 1:
        start_year = now.year
        print(f"Showing results for the present year {start_year}")
    
    open_page(year = start_year)
    parse_and_extract()
    