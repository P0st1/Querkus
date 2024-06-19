// scrollNavigation.js

function setupScrollNavigation() {
  var originalOffset = $('.services-list').offset().top; // Initial offset from the top
  var footerOffset = $(document).height() - ($(window).height() * 0.6); // Calculate where to stop

  $(window).scroll(function() {
      var scrollDistance = $(window).scrollTop();
      var servicesListHeight = $('.services-list').outerHeight();

      if (scrollDistance > originalOffset) {
          if (scrollDistance > footerOffset - servicesListHeight) {
              // Switch to absolute positioning before it reaches 60% from the bottom
              $('.services-list').css({
                  'position': 'absolute',
                  'bottom': footerOffset - scrollDistance - servicesListHeight,
              });
          } else {
              // Stick to the bottom with fixed positioning
              $('.services-list').css({
                  'position': 'fixed',
                  'bottom': 470,
              });
          }
      } else {
          // Return to the original fixed position
          $('.services-list').css({
              'position': 'fixed',
              'bottom': 0,
          });
      }
  });

  // Add event listener for scroll event
  window.addEventListener('scroll', function() {
      // Get the sections and links
      var sections = document.querySelectorAll('.service-details section');
      var links = document.querySelectorAll('.services-list a');

      // Loop through each section to find which one is in the viewport
      sections.forEach(function(section, index) {
          var rect = section.getBoundingClientRect();
          if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
              // Remove active class from all links
              links.forEach(function(link) {
                  link.classList.remove('active');
              });
              // Add active class to the corresponding link
              links[index].classList.add('active');
          }
      });
  });
}
