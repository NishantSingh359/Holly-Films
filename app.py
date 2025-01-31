import streamlit as st
import pandas as pd
import requests

st.markdown("""
    <style>
    .navbar {
        display: flex; 
        justify-content: space-between; /* Pushes content apart */
        align-items: center; 
        background-color: #0e1117;
        padding: 0px 15px; 
        height: 60px; 
        border-radius: 5px; 
        margin-bottom: 0px;
    }

    .navbar .logo {
        display: flex; 
        align-items: center; 
        font-size: clamp(20px, 5vw, 24px); 
        font-weight: bold; 
        font-family: 'Roboto', sans-serif; 
        color: #d0d0d0; 
        gap: 10px;
    }

    .navbar .logo img {
       height: 35px; /* Adjust the size of your logo */
       margin-right: 5px;
    }

    .navbar .links {
        margin-left: auto; /* Pushes the links to the right */
        display: flex;
        gap: 15px;
    }

    .navbar .links a {
        text-decoration: none;
        font-size: clamp(10px, 3vw, 15px);
        color: #ffffff;
        transition: color 0.3s ease;
    }

    .navbar .links a:hover {
        color: #1DB954; /* Accent color on hover */
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="navbar">
        <div class="logo">
            <img src="https://cdn-icons-png.flaticon.com/512/5028/5028123.png" alt="Logo">
            <span>Holly Films</span>
        </div>
        <div class="links">
            <a href="#top-upcoming">Top Upcoming</a>
            <a href="#top-2024">Top 2024</a>
            <a href="#about-me">About me</a>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        /* Apply background color */
        .stApp {
            
            background: linear-gradient(120deg, #13161c, #1E1E23); /* Gradient definition */
            background-size: cover; /* Ensures the gradient covers the whole screen */
            background-attachment: fixed; /* Keeps the gradient fixed while scrolling */
        }
        .stButton > button {
        margin-top: 29px;
        width: 100%;
        font-size: 25px;
        border-radius: 7px;
        background-color: #262730;
        color: #e4e4e4;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
        }

        
        .stSelectbox .st-b {
           background-color: black; /* Darker background for options */
           color: #eee;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# TOPS__________________________________
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <a  href="#facts-of-hollywoods" style="text-decoration: none;">
            <h1 style="width: 100%; text-align: center; color: #d0d0d0; font-size: 12px; margin-bottom: 10px; padding: 3px;
            border-radius: 3px; font-family: 'Poppins', 'Montserrat', sans-serif; font-weight: 500;
            background: linear-gradient(90deg, #0e1117,#232836);">
                <strong>About Hollywood </strong>
            </h1>
        </a>
        """,

        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <a href="#facts-of-hollywoods" style="text-decoration: none;">
            <h1 style="width: 100%; text-align: center; color: #d0d0d0; font-size: 12px; margin-bottom: 10px; padding: 3px;
            border-radius: 3px; font-family: 'Poppins', 'Montserrat', sans-serif; font-weight: 500;
            background: linear-gradient(90deg, #0e1117,#232836);">
                <strong>Facts of Hollywood </strong>
            </h1>
        </a>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <a href="#history-of-hollywoods" style="text-decoration: none;">
            <h1 style="width: 100%; text-align: center; color: #d0d0d0; font-size: 12px; margin-bottom: 10px; padding: 3px;
            border-radius: 3px; font-family: 'Poppins', 'Montserrat', sans-serif; font-weight: 500;
            background: linear-gradient(90deg, #0e1117,#232836);">
                <strong>History of Hollywood </strong>
            </h1>
        </a>
        """,
        unsafe_allow_html=True
    )


# LET'S BREAK HOLLYWOOD'S______________________
st.markdown(
    """
    <h1 style=" width: 63%; text-align: left; color: #d0d0d0; font-size: clamp(9px, 3vw, 13px); margin-bottom: 29px; background-color: #191E29; padding: 3px;
    border-radius: 3px; padding-left: 15px;  font-family: 'Poppins', 'Montserrat', sans-serif; font-weight: 300;
    background: linear-gradient(90deg, #0e1117,#232836, #2c2c2c);">
        <em>Let's little break about Hollywood</em>
    </h1>
    """,
    unsafe_allow_html=True
)

# TOP HOLLYWOOD'S___________________________
st.markdown(
    """
    <h1 style=" width: 41%; text-align: left; color: #d0d0d0; font-size:  clamp(13px, 3vw, 15px); background-color: #2c2c2c; padding: 2px;
    border-radius: 10px; padding-left: 15px;">
        Top Hollywoods
    </h1>
    """,
    unsafe_allow_html=True
)
top_movies = [
    {"title": "Avatar", "poster": "https://i.pinimg.com/originals/f4/52/3d/f4523da522af9f29eaac9e70ee7519a5.jpg"},
    {"title": "The Dark Knight", "poster": "https://th.bing.com/th/id/OIP.XNV0RaZYZUF6CcMPc8irnQHaK-?rs=1&pid=ImgDetMain"},
    {"title": "Interstellar", "poster": "https://th.bing.com/th/id/OIP.jVVUF1D1uEuSPvQtvM5uXgHaLH?rs=1&pid=ImgDetMain"},
    {"title": "Titanic", "poster": "https://th.bing.com/th/id/OIP.aMEiA7fmAM0bHtCOpelwbgHaKj?rs=1&pid=ImgDetMain"},
    {"title": "Avengers: Endgame", "poster": "https://m.media-amazon.com/images/I/71niXI3lxlL._AC_SY679_.jpg"},
]
cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        # Adjusting image height using HTML
        col.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; 
                height: 200px; background-color: #2c2c2c; border-radius: 10px; padding-top: 10px; margin-top: 10px;">
                <img src="{top_movies[i]['poster']}" style="max-height: 150px; border-radius: 10px;">
                <p style="text-align: center; color: white; font-size: 14px;">{top_movies[i]['title']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

from duckduckgo_search import DDGS
def fetch_poster(movie_title):
    with DDGS() as ddgs:
        results = ddgs.images(f"{movie_title} movie poster", max_results=5)
        for result in results:
            return result["thumbnail"]
    return None


# RECOMMENDATION ENGINE______________________________________________________________________________
# Recommendation function with posters
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    reco_movies = []
    reco_posters = []
    reco_crew = []
    reco_cast = []
    reco_year = []
    reco_rating = []
    reco_colle = []
    reco_runtime = []
    reco_overview = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        reco_movies.append(movie_title)
        reco_posters.append(fetch_poster(movie_title))
        reco_crew.append(movies.iloc[i[0]].crew)
        reco_cast.append(movies.iloc[i[0]].cast_new)
        reco_year.append(movies.iloc[i[0]].year)
        reco_rating.append(movies.iloc[i[0]].vote_average)
        reco_colle.append(movies.iloc[i[0]].revenue)
        reco_runtime.append(movies.iloc[i[0]].runtime)
        reco_overview.append(movies.iloc[i[0]].overview_new)
    return reco_movies, reco_posters, reco_year, reco_crew, reco_cast, reco_rating, reco_colle, reco_runtime, reco_overview

# Load data
movies_dict = pickle.load(open('movie recomme.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl', 'rb'))


import os

# Google Drive file ID for `similarity.pkl`
file_id = "1iwapAB_sL9bvpRu-CXbCO5Nt0ArgXwGI"
download_url = f"https://drive.google.com/uc?id={file_id}"
file_path = "similarity.pkl"  # Local file path

@st.cache_resource
def load_similarity():
    """Downloads and loads the similarity.pkl file."""
    # Download if not already available
    if not os.path.exists(file_path):
        st.info("Downloading similarity.pkl from Google Drive...")
        gdown.download(download_url, file_path, quiet=False)
    # Load the pickle file
    with open(file_path, "rb") as f:
        similarity = pickle.load(f)

    return similarity
similarity = load_similarity()


col1, col2 =  st.columns([2,1])
with col1:
    option = st.selectbox('', movies['title'].values)
with col2:
    input = st.button('Search', icon=":material/search:")


if input:
    names, posters, year, crew, cast, rating, colle, run_time, overview = recommend(option)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            # Adjusting image height using HTML
            col.markdown(
                f"""
                <div style="display: flex; flex-direction: column; align-items: center;
                     height: 240px; background-color: #2c2c2c; border-radius: 10px; padding: 10px; margin-top: 10px;">
                    <img src="{posters[i]}" style="max-height: 200px; border-radius: 10px;">
                    <p style="text-align: center; color: white; font-size: 14px;">{names[i]}</p>
                    
                </div>
                """,
                unsafe_allow_html=True,
            )

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            # Adjusting image height using HTML
            col.markdown(
                f"""
                    <div style="display: flex; flex-direction: column;
                         height: 320px;  background-color: #2c2c2c; border-radius: 10px; padding: 10px; margin-top: 10px">
                        <p style="text-align: center; color: white; font-size: 12px;"><strong>in</strong> {year[i]}</p>
                        <p style="text-align: center; color: white; font-size: 12px;"><strong>Director:</strong> {crew[i][0]}</p>
                        <p style="text-align: center; color: white; font-size: 12px;"><strong>Cast:</strong> {cast[i][0]} | {cast[i][1]} | {cast[i][2]}</p>
                        <p style="text-align: center; color: white; font-size: 12px;"><strong>Running Time:</strong> {run_time[i]}</p>
                        <p style="text-align: center; color: white; font-size: 12px;"><strong>Rating:</strong> {rating[i]}/10</p>
                        <p style="text-align: center; color: white; font-size: 12px;"><strong>Box Office:</strong> {colle[i]}</p>
                        
                        
                    </div>
                    """,
                unsafe_allow_html=True,
            )
    height = []
    for i in overview:
        height.append(len(i))
    d_height = max(height)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            # Adjusting image height using HTML
            col.markdown(
                f"""
                        <div style="display: flex; flex-direction: column; 
                             height: auto;  background-color: #2c2c2c; border-radius: 11px; padding: 10px; margin-top: 10px">
                            <p style="text-align: center; color: white; font-size: 11px;"><strong>Overview:</strong> {overview[i]}</p>
                            
                        </div>
                        """,
                unsafe_allow_html=True,
            )
# TOP ACTORS___________________________________
st.markdown(
    """
    <h1 style=" width: 60%; text-align: left; color: #d0d0d0; font-size: clamp(13px, 3vw, 15px); background-color: #2c2c2c; padding: 2px;
    border-radius: 10px; padding-left: 15px; margin-top: 10px;">
        Popular Hollywood's Actors
    </h1>
    """,
    unsafe_allow_html=True
)
top_movies = [
    {"title": "Dwayne Johnson", "poster": "https://th.bing.com/th/id/OIP.HRRtKBy4H-WyHHHtnPtUxgHaLI?w=599&h=900&rs=1&pid=ImgDetMain"},
    {"title": "Vin Diesel", "poster": "https://tnhrce.org/wp-content/uploads/2022/09/vin-diesel_tmdb.jpg"},
    {"title": "Tom Cruise", "poster": "https://th.bing.com/th/id/OIP.pi33jySSz5T3JS1PMbatTQHaLH?rs=1&pid=ImgDetMain"},
    {"title": "Johnny Depp", "poster": "https://th.bing.com/th/id/R.86a096599588356a8b8553f46739fa14?rik=d%2bP%2fIrFi2hVaVQ&riu=http%3a%2f%2fweknowyourdreams.com%2fimages%2fjohnny-depp%2fjohnny-depp-02.jpg&ehk=Py%2baOknBswMCKOdzUu19CXVmBXkrb4Wj0BooRsGIRLk%3d&risl=&pid=ImgRaw&r=0"},
    {"title": "Robert Downey Jr.", "poster": "https://th.bing.com/th/id/OIP.P7FQWa94YaOtgV9G-ZL5cQHaLH?rs=1&pid=ImgDetMain"},
]
cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        # Adjusting image height using HTML
        col.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; 
                height: 200px; background-color: #2c2c2c; border-radius: 10px; padding-top: 10px; margin-top: 10px;">
                <img src="{top_movies[i]['poster']}" style="max-height: 150px; border-radius: 10px;">
                <p style="text-align: center; color: white; font-size: 14px;">{top_movies[i]['title']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# TOP UPCOMING__________________________________________

st.markdown("""
    <h1 style=" width: 40%; text-align: left; color: #d0d0d0; font-size: clamp(5px, 3vw, 15px); margin-top: 25px; background-color: #2c2c2c; padding: 2px;
    border-radius: 10px; padding-left: 15px;">
    Top Upcoming
    </h1>
    """, unsafe_allow_html=True)

top_movies = [
    {"title": "Mickey 17", "poster": "https://th.bing.com/th/id/OIP.zmLW15UWKHJ7tFMZGsCpKQHaK-?rs=1&pid=ImgDetMain"},
    {"title": "Snow White", "poster": "https://i.pinimg.com/originals/b5/46/7f/b5467f2221d78d204b5a44c8d57d516f.jpg"},
    {"title": "Minecraft Movie", "poster": "https://th.bing.com/th?id=OIP.dtgjDrKtXhid6AWXajNoUQC-EZ&w=135&h=201&c=10&rs=1&qlt=90&o=6&pid=23.1"},
    {"title": "Sinners", "poster": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Sinners_%282025_film%29_poster.jpg/220px-Sinners_%282025_film%29_poster.jpg"},
    {"title": "Mission Impossible", "poster": "https://assets.gadgets360cdn.com/pricee/assets/product/202203/Mission-Impossible-Fallout-poster_1646333607.jpg"},
]
cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        # Adjusting image height using HTML
        col.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; 
                height: 200px; background-color: #2c2c2c; border-radius: 10px; padding-top: 10px; margin-top: 10px;">
                <img src="{top_movies[i]['poster']}" style="max-height: 150px; border-radius: 10px;">
                <p style="text-align: center; color: white; font-size: 14px;">{top_movies[i]['title']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# TOP 2024____________________________
st.markdown("""
    <h1 style=" width: 30%; text-align: left; color: #d0d0d0; font-size:clamp(5px, 3vw, 15px); margin-top: 25px; 
    background-color: #2c2c2c; padding: 2px;border-radius: 10px; padding-left: 15px;">
    Top 2024
    </h1>
    """, unsafe_allow_html=True)

# Movie posters and titles
top_movies = [
    {"title": "Rebel Moon: Part 2", "poster": "https://th.bing.com/th/id/OIP.Q8kOTOAPnwCrv-i2jVjY8QHaLH?rs=1&pid=ImgDetMain"},
    {"title": "Challengers", "poster": "https://image.tmdb.org/t/p/original/H6vke7zGiuLsz4v4RPeReb9rsv.jpg"},
    {"title": "Dune: Part Two", "poster": "https://www.dolby.com/siteassets/xf-site/content-detail-pages/dune_excl_art_2x3.jpg"},
    {"title": "Descendants 4", "poster": "https://m.media-amazon.com/images/M/MV5BYjM0NTUxNmMtYmZmMS00OTMwLWI1MTItNGU1M2I2YTJjMTM4XkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_FMjpg_UX1000_.jpg"},
    {"title": "Deadpool 3:", "poster": "https://th.bing.com/th/id/OIP.08gnD7SzmkU43sC2Wa1dbAHaLH?w=1000&h=1500&rs=1&pid=ImgDetMain"},
]

# Create 5 columns
cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        # Adjusting image height using HTML
        col.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; 
                height: 200px; background-color: #2c2c2c; border-radius: 10px; padding-top: 10px; margin-top: 10px;">
                <img src="{top_movies[i]['poster']}" style="max-height: 150px; border-radius: 10px;">
                <p style="text-align: center; color: white; font-size: 14px;">{top_movies[i]['title']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ABOUT HOLLYWOOD'S___________________________________________________________________________________________
with st.container():
    st.markdown(
        """
        <div id="about-hollywoods" style = "margin-top: 25px;">
            <h1 style=" width: 48%; text-align: left; color: #d0d0d0; font-size: clamp(13px, 3vw, 15px); background-color: #2c2c2c; padding: 2px;
            border-radius: 3px; padding-left: 15px;">
            About Hollywood's
            </h1>
        </div>
        """,
        unsafe_allow_html=True)
images = [
    "https://a.cdn-hotels.com/gdcs/production74/d1387/6ed6c061-3e1e-4c01-aa87-1f2efa2732a7.jpg",
    "https://fthmb.tqn.com/tL6jutKJusmd1j8s4_AAD3V_jhA=/1500x1000/filters:fill(auto,1)/KMD12CityWalkLA_0009lg-5857632a5f9b586e02c24fb3.jpg",
    "https://www.vacationclubloans.com/wp-content/uploads/2017/12/Hollywood-Studios.jpg"
]
info = [
    """The Heart of the Global Entertainment Industry
    Hollywood, located in Los Angeles, California, is often referred
    to as the entertainment capital of the world. Over the decades, 
    it has become synonymous with the glitz and glamour of the film industry,
    earning a reputation as a hub for creativity, storytelling, and innovation.
    From its humble beginnings in the early 20th century, Hollywood has grown
    into a global cultural phenomenon, influencing fashion, music, and art
    while shaping how stories are told on screen.""",
         """Hollywood’s influence extends far beyond the boundaries of the United States.
    It serves as a cultural bridge, introducing global audiences to American ideals,
    traditions, and perspectives. Films produced in Hollywood often define mainstream
    entertainment trends and inspire filmmakers worldwide to emulate its storytelling techniques.
    Moreover, Hollywood's ability to adapt to changing times has kept it at the forefront of the
    entertainment industry. From the introduction of color films to the integration of digital 
    effects, Hollywood has consistently embraced technological advancements to elevate storytelling.
    Franchises like Star Wars, Marvel Cinematic Universe, and The Lord of the Rings have achieved 
    worldwide acclaim, proving Hollywood’s unparalleled ability to captivate audiences on a massive scale.""",
       """Hollywood remains a symbol of ambition and creativity. For more than a century, it has provided a 
    platform for filmmakers to tell stories that entertain, inspire, and provoke thought. 
    While it continues to evolve in response to societal and technological changes, 
    its core remains rooted in the pursuit of artistic excellence.
    In many ways, Hollywood represents the universal human desire to dream big, tell stories,
     and connect with others."""]

col1, col2 = st.columns([1, 3])  # Set weights: 1 for col1 and 2 for col2
with col1:
    st.markdown(
        f"""
            <div style="display: flex; flex-direction: column;   
                height: auto; background-color: #2c2c2c; padding: 10px; margin-top: 10px; border-radius: 1px;">
                    <img src="{images[0]}" style="max-height: 150px; border-radius: 1px; ">
                    <p style="text-align: center; color: white; font-size: 11px;">Hollywood Sign</p>
                    <img src="{images[1]}" style="max-height: 150px; border-radius: 1px;">
                    <p style="text-align: center; color: white; font-size: 11px;">Universal Studious</p>
                    <img src="{images[2]}" style="max-height: 150px; border-radius: 1px;">
                    <p style="text-align: center; color: white; font-size: 11px;">Disney Studious</p>       
            </div>
        """,
            unsafe_allow_html=True,
    )  # Add spacing between images
with col2:
    st.markdown(
        f"""
            <div style=" height: auto; padding: 10px; background-color: #2c2c2c; color: white; border-radius: 5px;margin-top: 10px; ">
                <p style="text-align: left; color: white; font-size: 12px;">
                <span style="font-size: 13px; font-weight: 900px;"><strong>Hollywood: </strong></span>{info[0]}
                </p>
                <p style="text-align: left; color: white; font-size: 12px;">
                <span style="font-size: 13px; font-weight: 900px;"><strong>Hollywood’s Global Influence: </strong></span>{info[1]}
                </p>
                <p style="text-align: left; color: white; font-size: 12px;">
                <span style="font-size: 13px; font-weight: 900px;"><strong>A Legacy of Dreams:</strong></span> {info[2]}
                </p>
            </div>
        """,
        unsafe_allow_html=True
    )

# FACTS ABOUT HOLLYHOODS_______________________________________________________________________________________________
st.markdown(
    """
    <div id="facts-of-hollywoods">
        <h1 style=" width: 50%; text-align: left; color: #d0d0d0; font-size: clamp(13px, 3vw, 15px); margin-top: 25px; background-color: #2c2c2c; padding: 2px;
        border-radius: 3px; padding-left: 15px;">
        Facts of Hollywood
        </h1>
    </div>
    """,
     unsafe_allow_html=True)

images = [
    "https://image3.mouthshut.com/images/imagesp/925747653s.jpeg",
    "https://th.bing.com/th/id/OIP.XaVJ1Ld9zUCJ1oyQXcQVLQHaFj?w=800&h=600&rs=1&pid=ImgDetMain",
    "https://2.bp.blogspot.com/-XzrM01pskSQ/T6UegNQVWcI/AAAAAAAAALk/I3WhYTPTYiU/s1600/Roosevelthotel.jpg"
]
info = [
    "Hollywood began its journey as a hub for filmmaking in the early 1900s, with its first movie, In Old California, made in 1910.",
    "The name ""Hollywood"" was coined by H.J. Whitley, a real estate developer, who envisioned it as a residential community before it became synonymous with the film industry.",
    "Originally reading ""Hollywoodland,"" the famous sign was erected in 1923 as an advertisement for a housing development. It was later shortened to ""Hollywood"" in 1949.",
    "The 1920s to the 1960s is considered the Golden Age, during which major studios like Warner Bros., Paramount, and MGM dominated filmmaking.",
    "Hollywood is home to world-renowned film studios such as Universal Studios, Warner Bros., and Sony Pictures, which continue to produce blockbuster movies.",
	"The first Academy Awards ceremony took place in 1929 at the Hollywood Roosevelt Hotel, with only 270 attendees.",
    "Hollywood attracts aspiring actors and established stars, with neighborhoods like Beverly Hills and the Hollywood Hills known for their celebrity residents.",
    "The Hollywood Walk of Fame, started in 1960, features over 2,700 stars honoring contributions to film, television, music, theater, and radio."]
col1, col2 = st.columns([1, 3])  # Set weights: 1 for col1 and 2 for col2
with col1:
    st.markdown(
        f"""
            <div style="display: flex; flex-direction: column;   
                height: auto; background-color: #2c2c2c; padding: 10px; margin-top: 10px; border-radius: 1px;">
                    <img src="{images[0]}" style="max-height: 150px; border-radius: 1px; ">
                    <p style="text-align: center; color: white; font-size: 11px;">Hollywood in 1910</p>
                    <img src="{images[1]}" style="max-height: 150px; border-radius: 1px;">
                    <p style="text-align: center; color: white; font-size: 11px;">Universal Studious</p>
                    <img src="{images[2]}" style="max-height: 150px; border-radius: 1px;">
                    <p style="text-align: center; color: white; font-size: 11px;">Disney Studious</p>       
            </div>
        """,
        unsafe_allow_html=True,
    )  # Add spacing between images
with col2:
        st.markdown(
            f"""
                <div style=" height: auto; padding: 10px; background-color: #2c2c2c; color: white; border-radius: 5px;margin-top: 10px; ">
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[0]}
                  </p>
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[1]}
                  </p>
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[2]}
                  </p>
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[3]}
                  </p>
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[4]}
                  </p>
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[5]}
                  </p>
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[6]}
                  </p>
                  <p style="text-align: left; color: white; font-size: 12px;">
                  <span style="font-size: 15px;"><strong>•</strong></span> {info[7]}
                  </p>
                </div>
            """,
            unsafe_allow_html=True
        )

# HISTORY OF HOLLYHOOD_______________________________________________________________________________________________
import streamlit as st

# Section Heading
st.markdown(
    """
    <div id="history-of-hollywoods">
        <h1 style="
            width: 50%; 
            text-align: left; 
            color: #d0d0d0; 
            font-size: clamp(12px, 3vw, 15px); 
            margin-top: 25px; 
            background-color: #2c2c2c; 
            padding: 2px;
            border-radius: 3px; 
            padding-left: 15px;">
            History of Hollywood's
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Images and Info
images = [
    "https://i.pinimg.com/originals/0a/af/fe/0aaffee8ce1c7176cfb7bbcf378e179e.jpg",
    "https://external-preview.redd.it/tqT1WudzsxeXZaEl07goJsymR83K8vNpw2zMSObUo4A.jpg?auto=webp&s=52c78fc2bad61699c14dc5603a258250f67dd0a7",
    "https://i.redd.it/g1fgy5w8rtq11.jpg"
]

info = [
    """Hollywood's rise as a film hub started in the early 1900s. Filmmakers migrated from the East Coast to Los
       Angeles, attracted by its mild climate, diverse landscapes, and abundant natural light—ideal conditions for outdoor
       filming. The establishment of the first permanent film studio, the Nestor Film Company, in 1911 marked the 
       beginning of Hollywood’s dominance. By 1915, notable studios like Universal, Paramount, Warner Bros.,
       and 20th Century Fox were flourishing.""",
    """The 1930s ushered in the "Golden Age" of Hollywood, defined by the dominance of major studios and the introduction
       of sound in films, known as "talkies." This period witnessed the rise of "studio systems," where companies controlled
       every aspect of filmmaking, from production to distribution. Classics like Gone with the Wind (1939) and The
       Wizard of Oz (1939) epitomized the era’s grandeur.""",
    """The post-World War II era brought significant changes. Television emerged as a competitor, challenging
       Hollywood's monopoly on entertainment. The 1950s saw the rise of epic films like Ben-Hur (1959) and experiments
       with technologies like Cinemascope and 3D to lure audiences back to theaters. """,
    """The 1970s introduced the "New Hollywood" movement, where directors like Martin Scorsese, Francis Ford Coppola,
       and Steven Spielberg gained prominence. Blockbusters like Jaws (1975) and Star Wars (1977) redefined box office success.
       The industry evolved further in the digital age, with advancements in CGI (computer-generated imagery) and 
       streaming platforms revolutionizing content creation and distribution. Today, Hollywood continues to influence
       global culture, adapting to changing tastes and technology."""
]

col1, col2 = st.columns([1, 3])

# Column 1: Images
with col1:
    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column;   
            height: auto; 
            background-color: #2c2c2c; 
            padding: 10px; 
            margin-top: 10px; 
            border-radius: 1px;">
                <img src="{images[0]}" style="max-height: 150px; border-radius: 1px;">
                <p style="text-align: center; color: white; font-size: 11px;">Hollywood in 1930</p>
                <img src="{images[1]}" style="max-height: 150px; border-radius: 1px;">
                <p style="text-align: center; color: white; font-size: 11px;">Hollywood in 1950</p>
                <img src="{images[2]}" style="max-height: 150px; border-radius: 1px;">
                <p style="text-align: center; color: white; font-size: 11px;">Hollywood in 1970</p>       
        </div>
        """,
        unsafe_allow_html=True
    )

# Column 2: Info
with col2:
    with st.container():
        st.markdown(
            f"""
                <div style="
                    height: auto;
                    padding: 10px; 
                    background-color: #2c2c2c; 
                    color: white; 
                    border-radius: 5px;
                    margin-top: 10px;">
                        <p style="text-align: left; color: white; font-size: 12px;">
                            <span style="font-size: 13px;"><strong>Origins and Early Days (1900–1920s):</strong></span> {info[0]}
                        </p>
                        <p style="text-align: left; color: white; font-size: 12px;">
                            <span style="font-size: 13px;"><strong>The Golden Age (1930s–1940s):</strong></span> {info[1]}
                        </p>
                        <p style="text-align: left; color: white; font-size: 12px;">
                            <span style="font-size: 13px;"><strong>Post-War Era and Decline of the Studio System (1950s–1960s):</strong></span> {info[2]}
                        </p>
                        <p style="text-align: left; color: white; font-size: 12px;">
                            <span style="font-size: 13px;"><strong>New Hollywood and Modern Era (1970s–Present):</strong></span> {info[3]}
                        </p>     
                </div>
            """,
            unsafe_allow_html=True
        )

import streamlit as st

# Section Heading
st.markdown(
    """
    <div>
        <h1 style="
            width: 50%; 
            text-align: left; 
            color: #a7a7a7; 
            font-size: clamp(12px, 3vw, 15px); 
            margin-top: 25px; 
            background-color: #202020; 
            padding: 2px;
            border-radius: 3px; 
            padding-left: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
            About me
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)
# Custom CSS for styling
import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
        .about-container {
            display: flex;
            justify-content: space-between;
            background: #202020;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        }
        .about-text {
            width: 60%;
            font-family: 'Poppins', sans-serif;
        }
        .about-text h1 {
            font-size: 28px;
            font-weight: bold;
            color: #7e7e7e;
        }
        .about-text h1 span {
            color: #7A52F4;
        }
        .about-text p {
            font-size: 16px;
            color: #666;
            margin-top: -10px;
        }
        .about-text img:hover {
        transform: scale(1.2);
        }
        .about-text a {
            text-decoration: none; # Removes blue underline 
            border: none; 
        }
    </style>
""", unsafe_allow_html=True)
skills = ["https://avatars.githubusercontent.com/u/180900384?v=4",
              "https://bootflare.com/wp-content/uploads/2023/04/Python-Logo2-1024x1020.png",
              "https://pngimg.com/d/mysql_PNG36.png",
              "https://img.icons8.com/fluency/452/microsoft-excel-2019.png",
              "https://cdn.freelogovectors.net/wp-content/uploads/2023/11/power-bi-logo-freelogovectors.net_.png",
              "https://iconape.com/wp-content/files/zt/110872/png/tableau-software.png"]
# Layout using columns
st.markdown(
        f"""
        <div class = "about-container">
            <div class="about-text">
            <h1>Hi, I'm <span>Nishant Singh</span></h1>
            <p>Hello, my name is Nishant Singh. I am a professional <b>Data Analytics</b>.</p>
            <p>I love to extract usefull information from row data and creates dynamic Dashboard .</p>
            <p style="text-align: left; color: gray; font-size: 24px;">Skills </p>
            <img src="{skills[1]}" style="height: 38.5px; margin-bottom: 20px;margin-right: 5px;">
            <img src="{skills[2]}" style="height: 40px; margin-bottom: 20px; margin-right: 5px;">
            <img src="{skills[3]}" style="height: 43px; margin-bottom: 20px;">
            <img src="{skills[4]}" style="height: 40px; margin-bottom: 20px;">
            <img src="{skills[5]}" style="height: 40px; margin-bottom: 20px;">
            <p style="text-align: left; color: gray; font-size: 20px;"> Find me on</p>
            <a href="https://github.com/NishantSingh359" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" alt="GitHub" style="height: 32px; 
                    margin-right: 10px;">
                </a>
                <a href="https://www.linkedin.com/in/nishant-singh-67966a303/" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn"  style="height: 30px;
                    margin-right: 10px;">
                </a>
                 <a href="https://mail.google.com/" target="_blank">
                <img src="https://www.freepnglogos.com/uploads/logo-gmail-png/logo-gmail-png-gmail-icon-download-png-and-vector-1.png" alt="Gmail" 
                style="height: 42px; width: 38px; ">
            </a>
            </div>
            <img src="{skills[0]}" style="max-height: 150px; border-radius: 50%;">
            
        </div>
        """,
        unsafe_allow_html = True )

# COLUMN LAST ________________

