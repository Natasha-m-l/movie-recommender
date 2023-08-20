import streamlit as st
import pickle
import requests


st.title("Movie Recommendation")
def poster(id):
    url = 'https://api.themoviedb.org/3/movie/{}?language=en-US'.format(id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2M2JiYzcxMmU4YjNkMDY1MGJhNzYzOGEzNjkwODRkMCIsInN1YiI6IjY0ZDk1ZjMzYTEwNzRiMDBhZWIzNDQ5OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Cu2Xxqc1VbFs1FM1Gk9emQ81342Xd_DIeWN1TJP2Bgo"
        }
    response = requests.get(url, headers=headers)
    data=response.json()
    if 'poster_path' in data:
        return "https://image.tmdb.org/t/p/original" + data['poster_path']
    else:
        return "Poster not available"
    

def recommend(movie):
    movie_ind=movie_list.tolist().index(movie)
    dist=similarity[movie_ind]
    movie_li=sorted(list(enumerate(dist)),reverse=True,key=lambda x:x[1])[1:6]
    recommendedmov=[]
    recommendedmovposter=[]
    for i in movie_li:
        movie_id=movie_l.iloc[i[0]].movie_id
        recommendedmov.append(movie_list[i[0]])
        recommendedmovposter.append(poster(movie_id))
    return recommendedmov,recommendedmovposter
movie_l=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movie_list=movie_l['title'].values
option = st.selectbox('Enter the movie name',(movie_list))
#st.write('You selected:', option)
if st.button('Recommend'):
    names,posters=recommend(option)
    col=[]
    col=st.columns(5)
    for i in range(5):
        with col[i]:
            st.text(names[i])
            st.image(posters[i])

