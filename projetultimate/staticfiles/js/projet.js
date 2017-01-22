/**
 * 
 */  

var ajaxRequest;  // The variable that makes Ajax possible!
function ajaxFunction(){
   try{
      
      // Opera 8.0+, Firefox, Safari
      ajaxRequest = new XMLHttpRequest();
   }catch (e){
   
      // Internet Explorer Browsers
      try{
         ajaxRequest = new ActiveXObject("Msxml2.XMLHTTP");
      }catch (e) {
      
         try{
            ajaxRequest = new ActiveXObject("Microsoft.XMLHTTP");
         }catch (e){
      
            // Something went wrong
            alert("Your browser broke!");
            return false;
         }
      }
   }
}

var URL = "";
var wish_list = new Array();
$(document).ready(function() {
		
	if(sessionStorage.listFiche==null){
		sessionStorage.setItem('listFiche', "");
	} else {
		var list = sessionStorage.listFiche;
	}
	if(sessionStorage.typeExercice==null){
		sessionStorage.setItem('typeExercice', "");
	}
	if(sessionStorage.niveauExercice==null){
		sessionStorage.setItem('niveauExercice', "");
	}
	if(sessionStorage.chapitreExercice==null){
		sessionStorage.setItem('chapitreExercice', "");
	}
	if(sessionStorage.sectionExercice==null){
		sessionStorage.setItem('sectionExercice', "");
	}
	
    $("button").click(function(event) {
    	id_exo = $(this).attr("exo_id")
    	if(jQuery.inArray(id_exo,wish_list)==-1){
    		wish_list.push(id_exo);
    		$(this).attr('disabled', 'disabled');
    		var list = sessionStorage.listFiche;
    		if (list == ""){
    			list = id_exo;
    		} else { 
    			if(list.search(id_exo)==-1){
        			list = list + "," + id_exo;
    			}
    		}
    		
        	sessionStorage.setItem('listFiche', list);
    		jQuery("#ficheExercice").text(list);
    	}
    });
    
    $("#type").change(function(event){
    	//
    	sessionStorage.setItem('typeExercice', $(this).val());
    	$(this).prop("disabled", true);
    	
    	if($("#divNiveauExercice").attr("typeUser") != ''){
    		$("#divNiveauExercice").prop("hidden",false);
    		$("#divNiveauExercice").prop("disabled", true);
    		sessionStorage.setItem('niveauExercice', $("#divNiveauExercice").attr("typeUser"));
        	$(this).prop("disabled", true);
        	$("#divChapitreExercice").prop("hidden",false);
        	var donnee = {
        			"niveau": $("#divNiveauExercice").attr("typeUser")
        	}
        	$.ajax({
        		url: "/terminals/chapitreAjax",
        		type: "GET",
        		dataType: 'json', 
        		data: donnee,
        		success: function(result){
        			for (var i in result){
        				$("#chapitre").append("<option>"+result[i]+"</section>");
        			}
        		}
        	});
    	}
    });
    
    $("#niveau").change(function(event){
    	//
    	sessionStorage.setItem('niveauExercice', $(this).val());
    	$(this).prop("disabled", true);
    	$("#divChapitreExercice").prop("hidden",false);
    	var donnee = {
    			"niveau": $("#niveau").val()
    	}
    	$.ajax({
    		url: "/terminals/chapitreAjax",
    		type: "GET",
    		dataType: 'json', 
    		data: donnee,
    		success: function(result){
    			for (var i in result){
    				$("#chapitre").append("<option>"+result[i]+"</section>");
    			}
    		}
    	});
    });
    
    
    $("#chapitre").change(function(event){
    	//
    	sessionStorage.setItem('chapitreExercice', $(this).val());
    	$(this).prop("disabled", true);
    	$("#divSectionExercice").prop("hidden",false);
    	var donnee = {
    			"chapitre": $("#chapitre").val()
    	}
    	$.ajax({
    		url: "/terminals/sectionAjax",
    		type: "GET",
    		dataType: 'json', 
    		data: donnee,
    		success: function(result){
    			for (var i in result){
    				$("#sectionChapitre").append("<option>"+result[i]+"</section>");
    			}
    		}
    	});
    });
    
    $("#sectionChapitre").change(function(event){
    	//
    	sessionStorage.setItem('sectionExercice', $(this).val());
    	var donnee = {
    			"section": $("#sectionChapitre").val()
    	}
    	$.ajax({
    		url: "/terminals/exercicesAjax",
    		type: "GET",
    		dataType: 'html', 
    		data: donnee,
    		success: function(result){
    			$("#exercices").html(result);
    			var exercice = document.getElementById(exercices);
    			MathJax.Hub.Queue(["Typeset", MathJax.Hub, exercice]);
    		}
    	});
    });
    
    
    $("#buttonImprimer").click(function(event){ 
    	var list = sessionStorage.listFiche;
    	window.location = "/terminals/imprimer/"+list.toString();
    	
    	var donnee = {
			"urlFiche": "/terminals/imprimer/"+list.toString(), 
		}
		$.ajax({
			url: "/terminals/FicheImpressionAjax",
			type: "GET",
			dataType: 'html', 
			data: donnee,
			success: function(result){
				alert("aler");
			}
		});
    });
    
    
    $("#reset").click(function(event){
    	//on reinitialise les cookies
    	sessionStorage.setItem('listFiche', "");
    	sessionStorage.setItem('typeExercice', "");
    	sessionStorage.setItem('niveauExercice', "");
    	sessionStorage.setItem('chapitreExercice', "");
    	sessionStorage.setItem('sectionExercice', "");
    	
    	
    	$("#ficheExercice").text("");
    });
    
    $("#btnChapExercice").click(function(event){
    	$("#chapitre").prop("disabled", false);
    	$("#divSectionExercice").prop("hidden",true);
    });
    
    $("#btnTypeExercice").click(function(event){
    	$("#chapitre").prop("disabled", false);
    	$("#type").prop("disabled", false);
    	$("#divSectionExercice").prop("hidden",true);
    	$("#divChapitreExercice").prop("hidden",true);
    	$("#type").val("0");
    });
    
    
    $('#example1').DataTable();
    
});

