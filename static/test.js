let btn = document.getElementById("getDataBtn");
let content = document.getElementById("content");
let results = document.getElementById("results");
let sortBy = document.getElementById("sort");

btn.addEventListener("click", async () => {
  results.innerHTML = "";
  let apiURL = "";
  console.log(sortBy.value);
  if (sortBy.value == "title") {
    apiURL = "/api/data/name";
  } else if (sortBy.value == "rating") {
    apiURL = "/api/data/rating";
  } else if (sortBy.value == "releasedate") {
    apiURL = "/api/data/date";
  }
  console.log(apiURL);
  const response = await fetch(apiURL);
  const data = await response.json();
  for (let i = 0; i < data["message"].length; i++) {
    createMovieNode(data["message"][i]);
  }
});

function createMovieNode(object) {
  let c_rating = object["contentRating"];
  let name = object["name"];
  let date = object["datePublished"];
  let imgsrc = object["poster"];
  let rating = object["rating"]["ratingValue"];
  let genre = object["genre"];

  movie = document.createElement("div");
  movie_img = document.createElement("div");
  movie_info = document.createElement("div");
  movie_date = document.createElement("div");
  movie_genre = document.createElement("div");
  movie_name = document.createElement("div");
  movie_c_rating = document.createElement("div");
  movie_rating = document.createElement("div");

  let img = document.createElement("img");
  img.setAttribute("src", imgsrc);
  movie.classList.add("movie");
  movie_img.classList.add("movie_img");
  movie_name.classList.add("movie_name");
  movie_info.classList.add("movie_info");

  movie_img.appendChild(img);
  movie_rating.textContent = `Rating: ${rating}/10`;
  movie_date.textContent = date;
  movie_genre.textContent = genre;
  movie_name.textContent = name;
  movie_c_rating.textContent = `Rated: ${c_rating}`;

  movie_info.appendChild(movie_name);
  movie_info.appendChild(movie_rating);
  movie_info.appendChild(movie_date);
  movie_info.appendChild(movie_genre);
  movie_info.appendChild(movie_c_rating);

  movie.appendChild(movie_img);
  movie.appendChild(movie_info);
  results.appendChild(movie);
}
