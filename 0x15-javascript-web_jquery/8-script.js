var url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, (data) => {
	$('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
