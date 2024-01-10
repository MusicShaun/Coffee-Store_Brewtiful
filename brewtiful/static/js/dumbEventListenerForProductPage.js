
function handleFormSubmit() {
  // ! use this if you want to run some AJAX code to prevent the page reloading and retain the history object
  let productForm = document.querySelector('#product-form');
  userClicksAnchor('/cart', 'Cart');
  productForm.submit(); // submit the form manually
}
