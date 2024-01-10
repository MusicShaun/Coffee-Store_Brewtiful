document.addEventListener('DOMContentLoaded', function () {
  updateBreadCrumb();

  window.addEventListener('popstate', function (event) {
    updateBreadCrumb();
  });
});



// Updates bread crumb based on the history state
// function is called by the event listeners above. calling it directly will cause issues 
function updateBreadCrumb() {
  let navigator = document.getElementById('historyNavigator')
  let historyState = history.state

  if (historyState) {
    let historyItems = historyState.navigation || [] 
    let navigatorContent = ''
    let title = historyItems[historyItems.length - 1].title
    let itemFoundIndex

    // Find if the current page is already in the history
    itemFoundIndex = historyItems.findIndex(i => i.title === title)

    // If the current page is already in the history, remove all the pages after it
    if (itemFoundIndex > -1) {
      historyItems.splice(itemFoundIndex + 1, historyItems.length - itemFoundIndex - 1)
    }

    // Add to DOM 
    for (let i = 0; i < historyItems.length; i++) {
      navigatorContent += '<span class="breadcrumb-item"><a href="' + historyItems[i].url + '">' + historyItems[i].title + '</a></span>';
    }

    navigator.innerHTML = navigatorContent; 

  } else {
    navigator.innerHTML = '';
  }
}


// This function is called when the user clicks on a link in the page
// It will add the current page to the history state
function userClicksAnchor(url, title) {
  let HState = history.state || { navigation: [] };

  HState.navigation.push({ url: url, title: title });
  history.pushState(HState, title, url);

}