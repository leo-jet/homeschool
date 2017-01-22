/**
 * 
 */

$(".submenu").parent().prepend('<i class="entypo-down-open-big sf"></i>');


$("#vert-nav .topmenu a").click( function() {
  var $menu = $(this).next(".submenu");
  $menu.slideToggle('slow');
  $menu.parent().toggleClass('openmenu');
});




