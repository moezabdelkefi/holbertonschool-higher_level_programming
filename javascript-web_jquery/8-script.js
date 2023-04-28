$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  const movies = data.results;
  const list = $('#list_movies');
  $.each(movies, function(movie) {
    const title = movie.title;
    list.append('<li>' + title + '</li>');
  });
});
