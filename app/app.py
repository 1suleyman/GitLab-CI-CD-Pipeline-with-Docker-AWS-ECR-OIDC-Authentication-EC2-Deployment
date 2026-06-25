from flask import Flask, Response

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/")
def game():
    html = """
<!DOCTYPE html>
<html>
<head>
  <title>GitLab Runner Flappy Lab</title>
  <style>
    body { margin: 0; text-align: center; font-family: Arial; background: #70c5ce; }
    canvas { background: #70c5ce; display: block; margin: 20px auto; border: 3px solid #333; }
  </style>
</head>
<body>
  <h1>Flappy Runner Lab</h1>
  <p>Press SPACE to flap. If you can play this, your container is running on EC2.</p>
  <canvas id="game" width="400" height="500"></canvas>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let bird = { x: 60, y: 200, velocity: 0 };
let gravity = 0.5;
let flap = -8;
let pipes = [];
let score = 0;

document.addEventListener("keydown", e => {
  if (e.code === "Space") bird.velocity = flap;
});

function reset() {
  bird.y = 200;
  bird.velocity = 0;
  pipes = [];
  score = 0;
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  bird.velocity += gravity;
  bird.y += bird.velocity;

  ctx.fillStyle = "yellow";
  ctx.beginPath();
  ctx.arc(bird.x, bird.y, 15, 0, Math.PI * 2);
  ctx.fill();

  if (pipes.length === 0 || pipes[pipes.length - 1].x < 220) {
    let top = Math.random() * 250 + 50;
    pipes.push({ x: 400, top: top, gap: 130 });
  }

  ctx.fillStyle = "green";
  pipes.forEach(pipe => {
    pipe.x -= 2;
    ctx.fillRect(pipe.x, 0, 50, pipe.top);
    ctx.fillRect(pipe.x, pipe.top + pipe.gap, 50, 500);

    if (
      bird.x + 15 > pipe.x &&
      bird.x - 15 < pipe.x + 50 &&
      (bird.y - 15 < pipe.top || bird.y + 15 > pipe.top + pipe.gap)
    ) {
      reset();
    }

    if (pipe.x === bird.x) score++;
  });

  if (bird.y > 500 || bird.y < 0) reset();

  ctx.fillStyle = "black";
  ctx.font = "20px Arial";
  ctx.fillText("Score: " + score, 10, 30);

  requestAnimationFrame(draw);
}

draw();
</script>
</body>
</html>
"""
    return Response(html, mimetype="text/html")
