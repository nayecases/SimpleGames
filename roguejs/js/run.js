
//----------------------CONTEXT------------------
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext('2d');
var elements = []


//-----------------------CLASSES-----------------

function Player(){
  this.x = canvas.width/2;
  this.y = canvas.height -30;
  this.radius = 10;
  this.color = 'green';
  this.update = function(){ this.x+=1; this.y+=1}
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

function cicle(){
  update()
  draw()
}

setInterval(cicle,1000)
