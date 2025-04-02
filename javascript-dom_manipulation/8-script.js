const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const hello_id = document.getElementById('hello');
    hello_id.textContent = data.hello;
  })
  .catch(error => {
    console.error('Error;', error);
  });
