$(document).ready(function(){
 
$(".show-panel").click(function(){
    $("#lightbox").fadeIn(300);
	$("#lightbox-panel").fadeIn(300);
 })
 $("#close-panel").click(function(){
     $("#lightbox, #lightbox-panel").fadeOut(300);
 })

})

$(document).ready(function(){
 
$(".show-feedback").click(function(){
    $("#lightbox-feedback").fadeIn(300);
	$("#lightbox-feedbackform").fadeIn(300);
 })
 $("#close-feedback").click(function(){
     $("#lightbox-feedback, #lightbox-feedbackform").fadeOut(300);
 })

})

$(document).ready(function(){
 
$(".show-product").click(function(){
    $("#lightbox-product").fadeIn(300);
	$("#lightbox-productform").fadeIn(300);
 })
 $("#close-product").click(function(){
     $("#lightbox-product, #lightbox-productform").fadeOut(300);
 })

})

$(document).ready(function(){
 
$("#add_shipping").click(function(){
    $("#shipping_address").fadeIn(300);
 })

})