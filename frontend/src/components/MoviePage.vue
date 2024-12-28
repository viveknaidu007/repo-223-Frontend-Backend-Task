<template>
  <div>


    <div class="navbar">
      <div class="navbar-left">
        <h2 class="tmdb-title">TMDb</h2>
        <ul class="navbar-links" :class="{ 'show-links': showLinks }">
          <li><a href="#">Movies</a></li>
          <li><a href="#">TV Shows</a></li>
          <li><a href="#">People</a></li>
          <li><a href="#">More</a></li>
        </ul>
      </div>
      <div class="navbar-right">
        <button class="login-btn">Login</button>
        <button class="join-btn">Join TMDb</button>
      </div>


      <div class="hamburger" @click="toggleLinks">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>


    <div class="middle">
    <div class="navbar-le">
        <ul class="middle-links" :class="{ 'show-links': showLinks }">
        <li><a href="#">OverView</a></li>
        <li><a href="#">Media</a></li>
        <li><a href="#">Fandom</a></li>
        <li><a href="#">Share</a></li>
        </ul>
    </div>
    </div>



    <!--  movie page content -->
    <div class="movie-page">
      <div class="background" :style="{ backgroundImage: `url(${backgroundImageUrl})` }">
        <div class="overlay"></div>
      </div>
      <div class="movie-content">
        <div class="movie-poster">
          <img :src="movieData.Poster" alt="Movie Poster" />
        </div>
        <div class="movie-details">
          <h1>{{ movieData.Title }} ({{ movieData.Year }})</h1>
          <div class="user-score">
            <div class="circle">
              <div class="circle-bar"></div>
              <span class="circle-text">75%</span>
            </div>
            <p class="score-text">User Score</p>
            <div class="emojis">
              <span role="img" aria-label="love" class="emoji">❤️</span>
              <span role="img" aria-label="happy" class="emoji">😊</span>
              <span role="img" aria-label="emphasis" class="emoji">💥</span>
            </div>
          </div>
          <p><strong>Rating:</strong> {{ movieData.Rated }}</p>
          <p><strong>Released:</strong> {{ movieData.Released }}</p>
          <p><strong>Runtime:</strong> {{ movieData.Runtime }}</p>
          <p><strong>Genre:</strong> {{ movieData.Genre }}</p>
          <p><strong>Director:</strong> {{ movieData.Director }}</p>
          <p><strong>Actors:</strong> {{ movieData.Actors }}</p>
          <p><strong>Plot:</strong> {{ movieData.Plot }}</p>
          <p><strong>IMDB Rating:</strong> {{ movieData.imdbRating }}</p>
          <p><strong>Box Office:</strong> {{ movieData.BoxOffice }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";

export default {
  name: "MoviePage",
  setup() {
    const movieData = ref({});
    const backgroundImageUrl = new URL("../assets/img1.png", import.meta.url).href;
    const showLinks = ref(false); // 

    onMounted(async () => {
      try {
        const response = await axios.get(
          "http://www.omdbapi.com/?i=tt3896198&apikey=d2132124"
        );
        movieData.value = response.data;
      } catch (error) {
        console.error("Error fetching movie data:", error);
      }
    });

    // toggle function for mobile menu
    const toggleLinks = () => {
      showLinks.value = !showLinks.value;
    };

    return { movieData, backgroundImageUrl, showLinks, toggleLinks };
  },
};
</script>

<style scoped>
/* Navbar Styles */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: relative;
  padding: 0px 40px;
  background-color: rgba(10.5, 31.5, 73.5, 1);
  color: white;
  bottom : 8px;
  right : 9px;
  z-index: 1000;
  width: 100%;
  max-width: var(--maxPrimaryPageWidth);
}

.navbar-left {
  display: flex;
  align-items: center;
}

.tmdb-title {
  font-size: 1.8rem;
  margin-right: 20px;
}

.navbar-links {
  display: flex;
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.navbar-links li {
  margin: 0 15px;
}

.navbar-links li a {
  text-decoration: none;
  color: white;
  font-size: 1.1rem;
}

.navbar-right {
  display: flex;
  align-items: center;
  margin-right: 50px;
}

.login-btn,
.join-btn {
  margin-left: 15px;
  padding: 8px 20px;
  background-color: #ffcc00;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  color: black;
  font-size: 1rem;
}

.login-btn:hover,
.join-btn:hover {
  background-color: #ffb300;
}

/* Mobile Hamburger Menu Styles */
.hamburger {
  display: none;
  flex-direction: column;
  justify-content: space-around;
  width: 30px;
  height: 25px;
  cursor: pointer;
}

.hamburger span {
  display: block;
  width: 100%;
  height: 3px;
  background-color: white;
}

@media (max-width: 768px) {
  .navbar-links {
    display: none;
    flex-direction: column;
    width: 100%;
    text-align: center;
  }

  .navbar-links.show-links {
    display: flex;
  }

  .navbar-links li {
    margin: 10px 0;
  }

  .hamburger {
    display: flex;
  }

  .movie-page {
    margin-top: 60px;
  }
}

/* Movie Page Content */
.movie-page {
  position: absolute;
  width: 100%;
  height: 100vh;
  overflow: none;
  margin-top: 60px;
  right: 3px;
  top:75px;
  bottom : 0px;
}

.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  z-index: -1;
  filter: brightness(0.6) contrast(1.1);
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(17, 21, 233, 0.475);
  z-index: -1;
}

.movie-content {
  display: flex;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.movie-poster img {
  width: 250px;
  height: auto;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
}

.movie-details {
  margin-left: 30px;
  max-width: 600px;
  color: white;
}

.movie-details h1 {
  font-size: 2rem;
  margin-bottom: 15px;
}

.movie-details p {
  margin: 5px 0;
  color: white;
}

.user-score {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 5px solid white;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.circle:hover {
  transform: scale(1.1);
}

.circle-bar {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: conic-gradient(#4caf50 75%, #f5f1f1 0);
  transition: background 0.3s ease;
}

.circle:hover .circle-bar {
  background: conic-gradient(#ff5722 75%, #ddd 0);
}

.circle-text {
  font-weight: bold;
  font-size: 20px;
  color: rgb(76, 0, 147);
  position: absolute;
}

.score-text {
  margin-left: 15px;
  font-size: 1rem;
  color: white;
}

.emojis {
  margin-left: 10px;
  transition: 0.3s ease;
}

.emojis:hover {
  transform: scale(1.1);
}

.emojis .emoji {
  font-size: 1.5rem;
  margin-right: 10px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.emojis .emoji:hover {
  transform: scale(1.2);
}






/* Middle Navbar Styles */
.middle {
  background-color: white; /* White background */
  padding: 10px 0px; /* Padding for top and bottom */
  display: flex;
  justify-content: center; /* Center the navbar horizontally */
  align-items: center; /* Center the content vertically */
  width:100%
}

.navbar-le {
  width: 100%; /* Full width of the parent container */
  display: flex;
  justify-content: center; /* Center the list of links */
}

.middle-links {
  list-style-type: none; /* Remove default list styling */
  margin: 0; /* Remove margin */
  padding: 0; /* Remove padding */
  display: flex; /* Arrange the links horizontally */
}

.middle-links li {
  margin: 0 20px; /* Add some space between the links */
}

.middle-links li a {
  text-decoration: none; /* Remove underline from links */
  color: black; /* Set text color to black */
  font-size: 1.2rem; /* Set font size */
  font-weight: bold; /* Make text bold */
  transition: color 0.3s ease; /* Smooth transition on hover */
}

.middle-links li a:hover {
  color: #ff5722; /* Change text color on hover */
}

/* Mobile View - Shrinking Navbar (Optional) */
@media (max-width: 768px) {
  .middle {
    padding: 5px 0; /* Reduce padding on mobile for more space */
  }

  .middle-links {
    justify-content: space-around; /* Spread out the links a bit more evenly */
    width: 100%; /* Full width for the navbar */
    flex-wrap: wrap; /* Allow the links to wrap if necessary */
  }

  .middle-links li {
    margin: 5px; /* Reduce space between the links */
  }

  .middle-links li a {
    font-size: 1rem; /* Adjust font size on mobile */
  }
}



/* Mobile View */
@media (max-width: 768px) {
  .movie-content {
    flex-direction: column; /* Stack the content vertically */
    text-align: center; /* Center the content for mobile */
  }

  .movie-poster img {
    width: 200px; /* Adjust poster size */
    margin-bottom: 20px; /* Add spacing below the image */
  }

  .movie-details {
    margin-left: 0;
    max-width: 100%;
    text-align: center; /* Center the text */
  }

  .movie-details h1 {
    font-size: 1.5rem; /* Reduce title size */
  }

  .movie-details p {
    font-size: 1rem; /* Adjust text size */
  }

  .user-score {
    flex-direction: column; /* Stack user score elements vertically */
    margin-bottom: 10px;
  }

  .circle {
    width: 40px;
    height: 40px;
  }

  .circle-text {
    font-size: 16px; /* Adjust text size inside circle */
  }

  .score-text {
    font-size: 0.9rem; /* Adjust font size */
    margin-left: 0;
    margin-top: 5px; /* Add space above score text */
  }

  .emojis .emoji {
    font-size: 1.2rem; /* Reduce emoji size */
    margin-right: 5px;
  }

  .background {
    filter: blur(5px); /* Apply blur for mobile screens */
  }
}

@media (max-width: 480px) {
  .movie-poster img {
    width: 150px; /* Further reduce poster size */
  }

  .movie-details h1 {
    font-size: 1.2rem; /* Further reduce title size */
  }

  .movie-details p {
    font-size: 0.9rem; /* Further adjust text size */
  }
}


</style>
