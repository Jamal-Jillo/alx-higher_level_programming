$(document).ready(function(){
  $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
    var movies = data.results;
    for (var i = 0; i < movies.length; i++) {
      $("#list_movies").append("<li>" + movies[i].title + "</li>");
    }
  });
});
