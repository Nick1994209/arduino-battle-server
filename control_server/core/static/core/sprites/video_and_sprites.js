var get_sprites_and_video = function(data, addr_car) {

    var canvas = document.getElementById('videoCanvas');
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = '#783293';
    ctx.fillText('Loading...', canvas.width/2-30, canvas.height/3);

    // Setup the WebSocket connection and start the player
    //var client = new WebSocket('ws://{{ car.address }}:8084/');
    var client = new WebSocket('ws://'+addr_car+'8084'); //('ws://10.0.0.16:8084/');
    var player = new jsmpeg(client, {canvas:canvas});

    //-----------------sprites-----------------------
    var sprite_canvas = document.getElementById('spriteCanvas');
    console.log(sprite_canvas);
    sprite_context = sprite_canvas.getContext('2d');
    console.log(sprite_context);

    var url_image_bullets = data['images']['balls'];
    var url_image_fire = data['images']['sprite_bullet_and_fire'];
    var sprites = [];

    //задание времени, через которое будет отображаться в с
    function fire() {
        console.log("GO");
        setTimeout(function(){
            //кол-во действий в сек
            var interval_id = setInterval(play, 1000 / 200);
        }, 1000);
    }
    fire();

    function play() {
        for (var i=0; i<sprites.length; i++){
            if (sprites[i].end_this_sprites == true)
                    sprites.splice(i--, 1); //a = 3 //delete me
            else
                sprites[i].play();
        }
    }

    function add_sprites() {
        var sprite = create_fire_and_bullet(url_image_fire, url_image_bullets, sprite_context);
        sprites.push(sprite)
    }
};