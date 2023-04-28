$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  const firstCharacter = data.name;
  $('#character').text(firstCharacter);
});
