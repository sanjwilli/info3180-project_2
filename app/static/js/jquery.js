/* global $ */

$(document).ready(function(e){
    console.log("jquery is working");
	
	$("body").on("click",function(e){
		
	    //console.log($(e.target).next());
	    if($(e.target).is("img")){
	        //console.log("img clicked true")
	        if($(e.target).hasClass("imgCheck")){
	            //console.log("has the class");
	            $("img").each(function(){
	            	$(this).removeClass("check");
	            });
	            $(e.target).toggleClass("check");
	            $(e.target).next().prop("checked", "checked");
	        }
	    }
	    
	    
    });
});

