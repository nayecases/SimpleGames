
var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');
var circles = [];
var Game = {};
var player = {};
var leftPressed = false;
var rightPressed = false;
var upPressed = false;
var downPressed = false;
var enemies = [];
var tolerance = -5;

h=parseInt(document.getElementById('canvas').getAttribute("height"));
w=parseInt(document.getElementById('canvas').getAttribute("width"));


context.beginPath();
context.rect(0,0,w,h);
context.fillStyle = 'yellow';
context.fill();
context.lineWidth = 7;
context.strokeStyle = 'black';
context.stroke();

player.circle = circles.push(new circle(15,0,0, canvas.width/2, canvas.height/2,"green"));
player.x = circles[0].x;
player.y = circles[0].y;


for (i = 0; i < 10; i++) {
   put();
}

document.addEventListener('keydown', function(event) {
    if(event.keyCode == 37) {
        //alert('Left was pressed');
       leftPressed = true;
        //console.log("dfs "+leftPressed);
        
    }
    else if(event.keyCode == 39) {
        //alert('Right was pressed');
        rightPressed = true;
        

    } 
    else if(event.keyCode == 13) {
        alert('Paused');
        //circles.push(new circle(15,0,0, 150, 150,"green"));
    }else if(event.keyCode == 38) {
        upPressed = true;
        

       
    }else if(event.keyCode == 40) {
        downPressed = true;
       

        
    }
});

document.addEventListener('keyup', function(event) {
    if(event.keyCode == 37) {
        //alert('Left was pressed');
       leftPressed = false;
        //console.log("dfs "+leftPressed);
    }
    else if(event.keyCode == 39) {
        //alert('Right was pressed');
        rightPressed = false;

    }else if(event.keyCode == 38) {
        upPressed = false;

       
    }else if(event.keyCode == 40) {
        downPressed = false;

        
    }
});


function circleMoving(x, y, xModif, yModif,radio){
	context.clearRect(0,0,canvas.width, canvas.height);
	context.rect(0,0,w,h);
	context.fillStyle = 'yellow';
	context.fill();
	context.beginPath();
	context.arc(x,y,radio,0,2*Math.PI);
	context.fillStyle = 'blue';
	context.fill();
	context.stroke();
	x = x+xModif;
	y = y+yModif;

	if(y-radio<0 || y+radio>canvas.height){
		//xModif = -1*xModif;
		yModif = -1*yModif;
		
	}if(x-radio<0 || x+radio>canvas.width){
		//xModif = -1*xModif;
		xModif = -1*xModif;
		
	}
	setTimeout(circleMoving, 10);
}

function circleStatic(radio){
	context.beginPath();
	context.arc(Math.floor((Math.random() * 250) + 1),Math.floor((Math.random() * 250) + 1),radio,0,2*Math.PI);
	context.fillStyle = 'blue';
	context.fill();
	context.stroke();
}

function circle(radio,xModif,yModif,x,y,colour){
	this.radio=radio;
	this.xModif=xModif;
	this.yModif=yModif;
	this.x=x;
	this.y=y;
	this.colour=colour;
}

function put(){
	var number = (Math.random() * 10);
	if(number<5){
		circles.push(new circle((Math.random() * 25) + 1,0,0, (Math.random() * canvas.width) + 1, (Math.random() * canvas.height) + 1,"blue"));
		//console.log("if");

	}else{
		circles.push(new circle((Math.random() * 25) + 1,Math.random() < 0.5 ? -1 : 1,Math.random() < 0.5 ? -1 : 1, (Math.random() * canvas.width) + 1, (Math.random() * canvas.height) + 1,"blue"));
		//console.log("else");
	}

	console.log("pone uno nuevo");
}

function reload(){
	location.reload();
}


Game.draw = function(){

	context.clearRect(0,0,canvas.width, canvas.height);
	context.rect(0,0,w,h);
	context.fillStyle = 'yellow';
	context.fill();

	for(var z in circles){
	
	context.beginPath();
	context.arc(circles[z].x,circles[z].y,circles[z].radio,0,2*Math.PI);
	//console.log("el radio es  "+circles[j].radio);
	context.fillStyle = circles[z].colour;
	context.fill();
	context.stroke();
	circles[z].x = circles[z].x+circles[z].xModif;
	circles[z].y = circles[z].y+circles[z].yModif;

	if(circles[z].y-circles[z].radio<0 || circles[z].y+circles[z].radio>canvas.height){
		//xModif = -1*xModif;
		circles[z].yModif = -1*circles[z].yModif;
		
	}if(circles[z].x-circles[z].radio<0 || circles[z].x+circles[z].radio>canvas.width){
		//xModif = -1*xModif;
		circles[z].xModif = -1*circles[z].xModif;
		
	}
}
	if(circles[0].x<=0){
        	circles[0].x=0;
    }else if(circles[0].x>=canvas.width){
    		circles[0].x=canvas.width;
    }else if(circles[0].y<=0){
    		circles[0].y=0;
    }else if(circles[0].y>=canvas.height){
    		circles[0].y=canvas.height;
    }


    if(circles[0].colour=="red"){
		//alert("You loose, you survived  :  "+circles.length+" enemies!!");
		//location.reload();
		clearInterval(Game._intervalId);
		context.clearRect(0,0,canvas.width, canvas.height);
		context.rect(0,0,w,h);
		context.fillStyle = 'yellow';
		context.fill();
		context.fillStyle = 'black';
		context.font = "10px Arial";
		context.fillText("You loose!\r Survived:   "+circles.length+" enemies.", canvas.width/2, canvas.height/2);
		
	}
}

Game.update=function(){
//console.log("update");
	for(var i in circles){
		
			circles[i].x=circles[i].x+circles[i].xModif;
			circles[i].y=circles[i].y+circles[i].yModif;
			for(var j in circles){
				if(Math.abs(circles[i].x-circles[j].x)<circles[i].radio+circles[j].radio+tolerance && j!=i && Math.abs(circles[i].y-circles[j].y)<circles[i].radio+circles[j].radio+tolerance){
					circles[i].colour="red";
					circles[j].colour="red";
					//console.log("se pegan");
				}
		}
	}
	if(leftPressed){
		circles[0].x = circles[0].x-5;

	}if(rightPressed){
		circles[0].x = circles[0].x+5;

	}if(upPressed){
		circles[0].y = circles[0].y-5;

	}if(downPressed){
		circles[0].y = circles[0].y+5;

	}


}

Game.fps = 50;

Game.run = function() {
  Game.update();
  Game.draw();
};

// Start the game loop
Game._intervalId = setInterval(Game.run, 1000 / Game.fps);

Game.run();
setInterval(function(){put()}, 1000);

// To stop the game, use the following:

