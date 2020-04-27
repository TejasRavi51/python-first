import requests
import pprint
import pandas as pd

api_key = "5d32e8ef713148704a16f505a39c2e7e"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZDMyZThlZjcxMzE0ODcwNGExNmY1MDVhMzljMmU3ZSIsInN1YiI6IjVlOWFhZTExZmQ2ZmExMDAxZDAxNzNmOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Stpf-MSl_wMA831RN-Wmusnk9TJmTr7cWloXB6aq5so"

def version3():
    api_version = 3
    movie_id = 550
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    api_endpath = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{api_endpath}?api_key={api_key}"
    r = requests.get(endpoint)
    print(r.text)
    print(r.status_code)

def version4():
    api_version = 4
    movie_id = 540
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}"
    headers = {
        'Authorization': f'Bearer {api_key_v4}',
        'Content-Type': 'application/json;charset=utf-8'
    }
    r = requests.get(endpoint, headers=headers) # json={"api_key": api_key})
    print(r.status_code)
    print(r.text)

def search_movie():
    api_version =3
    movie = "The Matrix"
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    api_endpath = f"/search/movie"
    endpoint = f"{api_base_url}{api_endpath}?api_key={api_key}&query={movie}"
    r = requests.get(endpoint)
    print(r.status_code)
    #pprint.pprint(r.json())
    if r.status_code in range(200,299):
        data = r.json()
        results = data['results']
        movie_titles = set() # adds to the set irreecpective if they are unique or not
        for result in results:
            #print(result["original_title"])
            movie_titles.add(result["original_title"])
    return movie_titles

# def data_append():
#     output = "movies.csv"
#     movie_data =[]
#     df = pd.DataFrame()
if __name__ == "__main__":
    titles = search_movie()
    #pprint.pprint(titles)
    output = "movies.csv"
    df = pd.DataFrame(list(titles))
    print(df.head())
    df.to_csv(output, index=False)