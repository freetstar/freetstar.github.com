$(document).ready(function(){
	$('.box a').mouseover(function(){
		$(this).stop().animate({"top":"-364px"}, 200); 
	})
	$('.box a').mouseout(function(){
		$(this).stop().animate({"top":"0"}, 200); 
	})
})
