const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const list_of_movies = document.getElementById('list_movies');
    data.results.forEach(film => {
      const listItem = document.createElement('li');
      listItem.textContent = film.title;
      list_of_movies.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('Error:', error);
});
