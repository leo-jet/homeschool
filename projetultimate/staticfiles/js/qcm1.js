/**
 * 
 */
var question = {
		"question1": {
			"enonce": "calculer 1", 
			"figure": "fig1.JPG",
			"propositions":{
				"propo1": {
					"enonce": "Résoudre dans Z l'équation : $x = x + x^2 + x^6 + x^3$.", 
					"solution": "non"
				},
				"propo2": {
					"enonce": "l'équation est égale à $- 2 x^{6} - 3 x^{3} - 5$", 
					"solution": "oui"
				},
				"propo3": {
					"enonce": "proposition 2 de 2", 
					"solution": "oui"
				},
				"propo4": {
					"enonce": "proposition 2 de 2", 
					"solution": "oui"
				}
			}
		}, 
		"question2": {
			"enonce": "calculer 2",
			"figure": "fig2.JPG", 
			"propositions":{
				"propo1": {
					"enonce":"proposition 1 de 2 ceci est un blabla juste pour tester le responsive de mon site web ahahahah", 
					"solution": "non"
				},
				"propo2": {
					"enonce": "proposition 2 de 2", 
					"solution": "oui"
				},
				"propo3": {
					"enonce": "proposition 2 de 2", 
					"solution": "oui"
				}
			}
		},
		"question3": {
			"enonce": "calculer 2",
			"figure": "fig2.JPG", 
			"propositions":{
				"propo1": {
					"enonce":"proposition 1 de 2 ceci est un blabla juste pour tester le responsive de mon site web ahahahah", 
					"solution": "non"
				},
				"propo2": {
					"enonce": "proposition 2 de 2", 
					"solution": "oui"
				}
			}
		}
}; 

var my_url = "/home/leo/workspace/projetultimate/staticfiles/img/qcm/"


var nombreDeQuestion = Object.keys(question).length;

var numeroQuestionCourante = 1;
$(document).ready(function() {

	var questionCourante = "question"+numeroQuestionCourante;

	var resultat = 0;
	$("#bilan").text("BILAN : " +resultat);

	$("#enonce").text(question[questionCourante].enonce);
	var radio_home = document.getElementById("proposition");
	var j = 0;
	for(key in question[questionCourante].propositions){
		$("#proposition").append("<div class='radio icheck-primary' id ='class'"+key+"'> <input type='radio' id='"+key+"' name='propo' value ='"+question[questionCourante].propositions[key].solution+"'/> <label for='"+key+"'> <h3>"+question[questionCourante].propositions[key].enonce+"</h3></label></div>");
		$("#questionSelection").append("<option>Question "+j+" sur "+nombreDeQuestion+"</option>");
		j = j + 1;
	}

	$("#navigation_div").append("<div class='pull-left' id='left'></div>");
	$("#navigation_div").append("<div class='pull-right' id='right'></div>");
	$("#right").append("<button class='btn btn-md  btn-primary marge' id='prev'><i class='fa fa-arrow-left'></i></button>");
	$("#right").append("<button class='btn btn-md  btn-primary marge' id='next'><i class='fa fa-arrow-right'></i></button>");

	$("#left").append("<button class='btn btn-md  btn-primary marge' id='check'>Corriger</button>");
	//create img
	$("#image").attr('src', my_url+question[questionCourante].figure);

	// 3. Add event handler
	var buttonNext = document.getElementById("next");
	buttonNext.addEventListener ("click", function() {
		var propo = document.getElementsByName("propo");
		for(var i = 0; i < propo.length; i++) {
			if((propo[i].checked == true)&&( propo[i].value=="oui")) {
				resultat = resultat+1;
				$("#bilan").text("BILAN : " +resultat);

				// on passe à la question suivante
				$("#enonce").empty();
				$("#proposition").empty();
				numeroQuestionCourante = numeroQuestionCourante + 1;

				if(nombreDeQuestion>=numeroQuestionCourante){
					questionCourante = "question"+numeroQuestionCourante;

					exerciceSuivant(questionCourante);
					$("#left").empty();
					$("#left").append("<button class='btn btn-md  btn-primary marge' id='check'>Corriger</button>");

					//check button
					var ButtonVerifier = document.getElementById("check");
					ButtonVerifier.addEventListener ("click", function() {
						var propo = document.getElementsByName("propo");
						for(var i = 0; i < propo.length; i++) {
							if((propo[i].checked == true)&&( propo[i].value=="oui")) {
								propo[i].parentElement.setAttribute("class", "radio icheck-success");
								propo[i].parentElement.append(" Bonne réponse");
							}
							if((propo[i].checked == true)&&( propo[i].value=="non")) {
								propo[i].parentElement.setAttribute("class", "radio icheck-danger");
								propo[i].parentElement.append(" Mauvaise réponse");
							}
							propo[i].disabled = "true"
						}
						this.setAttribute("disabled", true);
					});

					//create img
					$("#image").attr('src', my_url+question[questionCourante].figure);
				} else {
					$("#left").empty();
				}
			}
		}

	});

	//check button
	var ButtonVerifier = document.getElementById("check");
	ButtonVerifier.addEventListener ("click", function() {
		var propo = document.getElementsByName("propo");
		for(var i = 0; i < propo.length; i++) {
			if((propo[i].checked == true)&&( propo[i].value=="oui")) {
				propo[i].parentElement.setAttribute("class", "radio icheck-success");
				propo[i].parentElement.append(" Bonne réponse");
			}
			if((propo[i].checked == true)&&( propo[i].value=="non")) {
				propo[i].parentElement.setAttribute("class", "radio icheck-danger");
				propo[i].parentElement.append(" Mauvaise réponse");
			}
			propo[i].disabled = "true"
		}
		this.setAttribute("disabled", true);
	});

});

function exerciceSuivant(courant){
	$("#enonce").text(question[courant].enonce);
	var radio_home = document.getElementById("proposition");
	for(key in question[courant].propositions){
		$("#proposition").append("<div class='radio icheck-primary'><input type='radio' id='"+key+"' name='propo' value ='"+question[courant].propositions[key].solution+"'/> <label for='"+key+"'>"+question[courant].propositions[key].enonce+"</label></div>");
	}
}


var totaltime = 60;
function update(percent){
	var deg;
	if(percent<(totaltime/2)){
		deg = 90 + (360*percent/totaltime);
		$('.pie').css('background-image',
				'linear-gradient('+deg+'deg, transparent 50%, white 50%),linear-gradient(90deg, white 50%, transparent 50%)'
		);
	} else if(percent>=(totaltime/2)){
		deg = -90 + (360*percent/totaltime);
		$('.pie').css('background-image',
				'linear-gradient('+deg+'deg, transparent 50%, red 50%),linear-gradient(90deg, white 50%, transparent 50%)'
		);
	}
}

var timer = new Timer();
timer.start({precision: 'seconds', startValues: {seconds: 0}, target: {seconds: 60}});
$('#values').html(timer.getTimeValues().toString());
timer.addEventListener('secondsUpdated', function (e) {
	$('#values').html(timer.getTimeValues().minutes+":"+timer.getTimeValues().seconds);
	var count = timer.getTotalTimeValues().seconds;
	update(count);
});
