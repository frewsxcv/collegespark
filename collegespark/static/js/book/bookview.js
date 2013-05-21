var currentURL = "http://sharrre.com/";
console.log(currentURL);


$('.twitter').sharrre({
  share: {
    twitter: true
  },
  url: currentURL,
  enableHover: true,
  enableTracking: true,
  enableCounter: false,
  click: function(api, options){
    api.simulateClick();
    api.openPopup('twitter');
  }
});

$('.facebook').sharrre({
  share: {
    facebook: true
  },
  url: currentURL,
  enableHover: false,
  enableTracking: true,
  enableCounter: false,
  click: function(api, options){
    api.simulateClick();
    api.openPopup('facebook');
  }
});

$('.googleplus').sharrre({
  share: {
    googlePlus: true
  },
  url: currentURL,
  enableHover: false,
  enableTracking: true,
  enableCounter: false,
  click: function(api, options){
    api.simulateClick();
    api.openPopup('googlePlus');
  }
});