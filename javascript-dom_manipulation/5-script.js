const update_the_header = document.getElementById('update_header');

update_the_header.addEventListener('click', function() {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});
