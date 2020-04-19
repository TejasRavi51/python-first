import os
import sys
import datetime
import requests
import webbrowser
import pandas as pd
from requests_html import HTML

Base_dir = os.path.dirname(os.path.abspath(__file__))
now = datetime.datetime.now()
print(Base_dir,'\n',now)

def open_page(url):
    webbrowser.open(url)
    print(url)

def url_to_text(url, save = False, year = None):
    r = requests.get(url)
    if r.status_code == 200:
        html_txt = r.text
        if save:
            with open(f"world-{year}.html", "w") as f:
                f.write(html_txt)
    return html_txt

def parse_and_extract(url, year = None):
    html_text = url_to_text(url ,save = True, year = start_year)
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)

    table_data = []
    #table_data_dicts = []
    header_names = []
    if len(r_table) == 0:
        return False
    parsed_table = r_table[0]           #assigning the first row of the table as the header
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find("th")
    #iterating through column's to assign each header name
    for x in header_cols:
        header_names.append(x.text)
    #header_names = [x.text for x in header_cols]
    print(header_names)

    for row in rows[1:]:
        cols = row.find("td")
        row_data =[]
        #row_dict_data = {}
        for cols in cols:
            row_data.append(cols.text)
            #print(i, cols.text, "\n")   
            # header_name = header_names[i]
            # row_dict_data[header_name] = cols.text        
        #print(row_data)
        table_data.append(row_data)
        #table_data_dicts.append(row_dict_data)
    df = pd.DataFrame(table_data, columns = header_names)
    #df = pd.DataFrame(table_data_dicts)

    path = os.path.join(Base_dir, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join(path, f"{year}.csv")
    df.to_csv(filepath, index=False)
    return True

def multiple_years(year= None, years_ago= 0):
    #code to run for multiple years
    for i in range(0,years_ago+1):
        pull_year = year - i
        url = "https://www.boxofficemojo.com/year/world/"+ f"{pull_year}"
        finished = parse_and_extract(url, year = pull_year)
        if finished:
            print(f'finished {pull_year}')
        else:
            print(f"{pull_year} wasn't finished")
    open_page(url)

if __name__ == "__main__":
    count = 0
    start_year = None
    if len(sys.argv) == 3:
        try:
            start_year = int(sys.argv[1])                 #try to concert the argument into integer 
            count = int(sys.argv[2])
            assert start_year >= 1977 and start_year <= now.year    #asserting the given year is in the valid range
        except:
            print("Please enter a valid year from 1977 to 2020 and a valid timeframe")
    
    elif len(sys.argv) == 2:
        try:
            start_year = int(sys.argv[1])                 #try to concert the argument into integer 
            assert start_year >= 1977 and start_year <= now.year    #asserting the given year is in the valid range
        except:
            print("Please enter a valid year from 1977 to 2020")
    elif len(sys.argv) == 1:
        start_year = now.year
        print(f"Showing results for the present year {start_year}")
    else:
        print("Enter valid arguments")
    
    multiple_years(year = start_year, years_ago= count)
    