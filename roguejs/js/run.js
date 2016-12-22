
//----------------------CONTEXT------------------
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext('2d');
var elements = []

//-----------------------CONSTANTS---------------
var rightPressed = false;
var leftPressed = false;
var upPressed = false;
var downPressed = false;
//-----------------------CLASSES-----------------

function Player(){
  this.x = canvas.width/2;
  this.y = canvas.height -30;
  this.radius = 10;
  this.color = 'green';
  this.dx = 1;
  this.dy = 1;
  this.update = function(){
    if(rightPressed){this.dx=1;this.dy=0;if(checkBoundaries(this)){this.move()};}
    if(leftPressed){this.dx=-1;this.dy=0;if(checkBoundaries(this)){this.move()};}
    if(upPressed){this.dx=0;this.dy=-1;if(checkBoundaries(this)){this.move()};}
    if(downPressed){this.dx=0;this.dy=1;if(checkBoundaries(this)){this.move()};}
  }
  this.move = function(){ this.x+=this.dx; this.y+=this.dy}
  this.draw = function(){
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI*2);
    ctx.fillStyle = this.color;
    ctx.fill();
    ctx.closePath();
  }
}


//----------------------INSTANCES-----------------

elements.push(new Player())

//-----------------------FUNCTIONS----------------
function checkBoundaries(elem){
  if(elem.x+elem.dx>=canvas.width-elem.radius ||
    elem.x-elem.radius+elem.dx<0 ||
    elem.y-elem.radius-elem.dy<0 ||
    elem.y+elem.dy>=canvas.height-elem.radius){
    return false
  }
  return true
}

function keyDownHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = true;
    }
    else if(e.keyCode == 37) {
        leftPressed = true;
    }
    else if(e.keyCode == 38) {
        upPressed = true;
    }
    else if(e.keyCode == 40) {
        downPressed = true;
    }
}

function keyUpHandler(e) {
    if(e.keyCode == 39) {
        rightPressed = false;
    }
    else if(e.keyCode == 37) {
        leftPressed = false;
    }
    else if(e.keyCode == 38) {
        upPressed = false;
    }
    else if(e.keyCode == 40) {
        downPressed = false;
    }
}


//-----------------------LIFE CICLE---------------

function update(){
  for (elem in elements){
    elements[elem].update();
  }
}

function draw(){
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (elem in elements){
    elements[elem].draw();
  }
}

function cycle(){
  update()
  draw()
}

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);
setInterval(cycle,10)
