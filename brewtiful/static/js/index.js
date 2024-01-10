let productCards = document.querySelectorAll('.product-card');
const productCardsRef = [...document.querySelectorAll('.product-card')];
let filterHistory = ""
let filterOpen = false; 
let productCount = 12;
updateFilterCount(productCount);

function clearFiltering() {
  productCards = [...productCardsRef]; // Reset cards to original state
  updateProductDisplay(productCards); // Update container with original data
  filterHistory = ""; 
  updateFilterCount(12);
}

function toggleFiltering() {
  showFiltering();
  clearFiltering();
}

// Filter buttons
function filterProducts(obj, label) {
  if (filterHistory == label) clearFiltering(); // if the same category is clicked, clear the filter then apply the new filter

  let originalProductCards = [...productCards];
  let filteredProducts = [];

  
  switch (label) {
    case 'blend':
      filteredProducts = filterProductsByBlend(obj, originalProductCards);
      break;
    case 'origin':
      filteredProducts = filterProductsByOrigin(obj, originalProductCards)
      break;
    case 'taste':
      filteredProducts = filterProductsByTaste(obj, originalProductCards);
      break;
    default:
      console.log('no filtering applied');
  }

  productCards = filterProductsByCombination(originalProductCards, filteredProducts);
  updateProductDisplay([...productCards]);
  filterHistory = label;
  updateFilterCount();
}



function updateProductDisplay(productCards) {
  const productContainer = document.querySelector('.product-container');
  productContainer.innerHTML = ''; // Clear the container

  productCards.forEach(card => {
    productContainer.appendChild(card);
  });

  productCards.forEach(card => {
    card.style.display = 'block';
  });

  // Hide all cards that are not in the filtered list
  const allCards = document.querySelectorAll('.product-card');
  allCards.forEach(card => {
    if (!productCards.includes(card)) {
      card.style.display = 'none';
    }
  });
}


function filterProductsByCombination(originalProducts, filteredProducts) {
  const combinedProducts = []; // Store combined results

  // Show previously displayed products that are also in current filter
  originalProducts.forEach((card) => {
    if (filteredProducts.includes(card)) {
      combinedProducts.push(card);
    }
  });

  // Add newly filtered products to the final list
  combinedProducts.push(...filteredProducts);

  return combinedProducts;
}



function filterProductsByBlend(obj, arr) {
  let textIsBlend = obj.innerText == 'BLEND'

  return arr.filter((card) => {
    const isBlend = card.dataset.origin === 'True';
    if (textIsBlend) {
      return isBlend; // Keep only blends if BLEND is selected
    } else {
      return !isBlend; // Keep only non-blends if BLEND is not selected
    }
  });
}

function filterProductsByTaste(obj, arr) {
  const taste = obj.innerText.toLowerCase(); // ['Chocolate', 'Citrus', 'Floral']

  return arr.filter((card) => {
    const notes = card.dataset.notes.toLowerCase();
    if (notes.includes(taste)) {
      return notes
    } else {
      return !notes
    }
  });
}

function filterProductsByOrigin(obj, arr) {
  const origin = obj.innerText.toLowerCase(); // ["Australia", "South America", "Central America", "Africa", "Asia"]

  return arr.filter((card) => {
    const location = card.dataset.location.toLowerCase().split(/\s+/).join(' ');
    return location == origin
  });
}

function showFiltering() {
  const filter = document.querySelectorAll('.filter');

  // add class 'filter__open' to filter 
  filter.forEach(filter => {
    filter.classList.toggle('filter__open');
  });
  filterOpen = !filterOpen;
}


function updateFilterCount() {
  let productsShowing = document.querySelectorAll('.product-card')
  const filterCount = document.getElementById('filter-count');
  filterCount ? filterCount.textContent = "Showing " + productsShowing.length +  " results" : null
}



// Search bar
const sortOptions = document.querySelectorAll('.dropdown-item');
const sortTextElement = document.querySelector('.sort-text');

function applySorting(trigger) {
  // Change inner text 
  sortOptions.forEach(option => {
    option.addEventListener('click', () => {
      const selectedOption = option.innerText;
      sortTextElement.textContent = `SORT BY: ${selectedOption}`;
    });
  });
  
  // Change order
  productCards = [...productCards]

  switch (trigger) {
    case 'A to Z':
      productCards = AtoZ([...productCards]);
      break;
    case 'Z to A':
      productCards = ZtoA([...productCards]);
      break;
    case 'Price: Low to High':
      productCards = lowToHigh([...productCards]);
      break;
    case 'Price: High to Low':
      productCards = highToLow([...productCards]);
      break;
    default:
      console.log('no sorting applied');
  }
    // Update the DOM with the sorted elements
  const productContainer = document.querySelector('.product-container');
  
  productContainer.innerHTML = ''; // Clear the container

  productCards.forEach(card => {
    productContainer.appendChild(card);
  });

}

function AtoZ(arr) {
  return arr.sort((a, b) => {
    const nameA = a.querySelector('h3').textContent;
    const nameB = b.querySelector('h3').textContent;
    return nameA.localeCompare(nameB);
  });
}
function ZtoA(arr) {
  return arr.sort((a, b) => {
    const nameA = a.querySelector('h3').textContent;
    const nameB = b.querySelector('h3').textContent;
    return nameB.localeCompare(nameA);
  });  
}
function lowToHigh(arr) {
  return arr.sort((a, b) => {
    const priceA = a.querySelector('.price').textContent.replace('FROM $', '').trim();
    const priceB = b.querySelector('.price').textContent.replace('FROM $', '').trim();
    return priceA - priceB;
  });
}
function highToLow(arr) {
  return arr.sort((a, b) => {
    const priceA = a.querySelector('.price').textContent.replace('FROM $', '').trim();
    const priceB = b.querySelector('.price').textContent.replace('FROM $', '').trim();
    return priceB - priceA;
  });
}



// Listener to exit filtering section when clicked outside container 
function exitFilter() {
  showFiltering();
}