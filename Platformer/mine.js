
//var context = canvas.getContext('2d');

(function() {
    var requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;
    window.requestAnimationFrame = requestAnimationFrame;
})();

var Game = {};

var leftPressed = false;
var rightPressed = false;
var upPressed = false;
var downPressed = false;



h=parseInt(document.getElementById('canvas').getAttribute("height"));
w=parseInt(document.getElementById('canvas').getAttribute("width"));


var playerIm = new Image();
var playerImW;
var playerImH
playerIm.onload = function(){
playerImW = this.width;
playerImH = this.height;
};
playerIm.src = "./assets/jigglewalk_0.gif";
var canvas = document.getElementById("canvas"),
    ctx = canvas.getContext("2d"),
    width = 500,
    height = 200,
    player = {
	x : width/2,
  y : height - playerIm.width,
  width : 32,
  height : 32,
  speed: 3,
  velX: 0,
  velY: 0,
  jumping: false,
    grounded: false
    },
    gravity = 0.3,
    friction= 0.8;
    var boxes = [];
    var background = new Image();
    background.src = "./assets/back2.jpg";
    
 
// dimensions



boxes.push({
    x: 0,
    y: 0,
    width: 10,
    height: height
});
boxes.push({
    x: 0,
    y: height - 2,
    width: width,
    height: 50
});
boxes.push({
    x: width - 10,
    y: 0,
    width: 50,
    height: height
});

boxes.push({
    x: 120,
    y: 10,
    width: 80,
    height: 80
});
boxes.push({
    x: 170,
    y: 50,
    width: 80,
    height: 80
});
boxes.push({
    x: 220,
    y: 100,
    width: 80,
    height: 80
});
boxes.push({
    x: 270,
    y: 150,
    width: 40,
    height: 40
});




 
canvas.width = width;
canvas.height = height;




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





function reload(){
	location.reload();
}


Game.draw = function(){
  // draw our player

     ctx.clearRect(0,0,width,height);
     ctx.fillStyle = "black";
      ctx.beginPath();
 ctx.drawImage(background,0,0);
for (var i = 0; i < boxes.length; i++) {
    ctx.rect(boxes[i].x, boxes[i].y, boxes[i].width, boxes[i].height);
}
 
  ctx.fill();
  //ctx.fillStyle = "red";
  //ctx.fillRect(player.x, player.y, player.width, player.height);
  ctx.drawImage(playerIm,player.x,player.y);
}




Game.update=function(){
	if(rightPressed && player.velX < player.speed){	                       
           player.velX++;                  
       } 

    if(leftPressed && player.velX > -player.speed){
	                       //console.log("se actualiza");
            player.velX--;                 
       } 
       if(upPressed && !player.jumping && player.grounded){
        player.jumping = true;
        player.grounded = false; // We're not on the ground anymore!!
        player.velY = -player.speed * 2;
  }

	player.velX *= friction;
 
    player.velY += gravity;
 
    player.x += player.velX;
    player.y += player.velY;
 
    player.grounded = false;
for (var i = 0; i < boxes.length; i++) {
      res={};
      res = collision(player,boxes[i]);
      //console.log("res.direction  "+res.direction+"  res.offset  "+res.offset);
      if(res.direction){
       if (res.direction === "l" ) {
            player.velX = 0;
            player.jumping = false;
            player.x = player.x+res.offset;
            //player.x=boxes[i].x+boxes[i].width;
            console.log("por izquierda");
        } else if (res.direction === "r") {
            player.velX = 0;
            //player.grounded = true;
            player.jumping = false;
            player.x = player.x-res.offset;
            //player.x=boxes[i].x-player.width;
            console.log("por derecha");

        }else if (res.direction === "b") {
            player.grounded = true;
            player.jumping = false;
            player.y = Math.ceil(player.y-res.offset);
	   
            //player.y = boxes[i].y-player.height;
                       // console.log("por abajo");
	//console.log("por abajo");
        } else if (res.direction === "t") {
            player.velY *= -1;
	//console.log(res.offset);
                        console.log("por top");
            ///player.y = boxes[i].y+boxes[i].height;
            player.y = player.y+res.offset;
           // player.y = boxes[i].y-player.height;
        }
       // console.log("se choca  ".player);
}
}

	  if(player.grounded){
         player.velY = 0;
    }
	//console.log("update");

    // run through the loop again
    

}

Game.fps = 50;

Game.run = function() {
  Game.update();
  Game.draw();
  requestAnimationFrame(Game.run);
};

// Start the game loop
//Game._intervalId = setInterval(Game.run, 1000 / Game.fps);

//Game.run();


// To stop the game, use the following:
window.addEventListener("load", function(){
  Game.run();
});

function collision(elem1, elem2){
    wHalf= (elem1.width/2) + (elem2.width/2);
    hHalf= (elem1.height/2) + (elem2.height/2);
    vX = (elem1.x+elem1.width/2) - ((elem2.x+elem2.width/2));
    vY = (elem1.y+elem1.height/2) - ((elem2.y+elem2.height/2));
//console.log(vY);
    var result = {};
   //console.log(elem1.x+elem1.width/2);
   if(Math.abs(vX)<wHalf && Math.abs(vY)<hHalf){
    xIn= Math.ceil(wHalf - Math.abs(vX));
    yIn= Math.ceil(hHalf - Math.abs(vY));
    if(yIn>=xIn){
        if(vX<0){
          	result.direction = "r";
          	result.offset = xIn;
        }else{
         result.direction = "l";
    	result.offset = xIn;
        }
     }else{ 
        if( vY<0){
      result.direction = "b";
  	  result.offset = yIn;
      }else{
        result.direction = "t";
  	     result.offset = yIn;
      }
  }
}
    return result;
}


