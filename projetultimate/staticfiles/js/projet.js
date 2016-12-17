/**
 * 
 */  
var wish_list = new Array();
var URL = "";
$(document).ready(function() {
    $("button").click(function(event) {
    	id_exo = $(this).attr("exo_id")
    	if(jQuery.inArray(id_exo,wish_list)==-1){
    		wish_list.push(id_exo);
    		$(this).attr('disabled', 'disabled');
    		jQuery("#nombreExercice").text(wish_list.length);
    	}
    });
    $("#imprimer").click(function(event){ 
    	$("#buttonImprimer").attr("href", "/terminals/imprimer/"+wish_list.toString());
    });
    
    JXG.Options.renderer = 'canvas';


    var brd = JXG.JSXGraph.initBoard('box', {boundingbox:[-2,5,5,-2]});
    var A  = brd.create('point', [0,0]),
        B  = brd.create('point', [2,0]),
        C  = brd.create('point', [1,2]),

        a1 = brd.create('segment', [A,B], {name:'a_1', withLabel:true, label:{position:'top'} }),
        a2 = brd.create('segment', [B,C], {name:'a_2', withLabel:true, label:{position:'top'} }),
        a3 = brd.create('segment', [C,A], {name:'a_3', withLabel:true, label:{position:'top'} }),
        c1 = brd.create('circle', 
                [A, 
                 function(){ var r1 = (C.Dist(A)-B.Dist(C)+A.Dist(B))/2.0;
                            return r1; }
                ]);
        c2 = brd.create('circle', 
                [B, 
                 function(){ return A.Dist(B)-c1.Radius(); }
                ]);
        c3 = brd.create('circle', 
                [C, 
                 function(){ return B.Dist(C)-c2.Radius(); }
                ]);
        stream = brd.renderer.canvasRoot.toDataURL();
        $("image").attr("src", stream)

});