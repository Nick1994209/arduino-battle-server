function FireAndBuletSprite (options) {
    var self = this;
    self.sprite_fire = options.sprite_fire;
    self.sprite_bullet = options.sprite_bullet;
    self.end_this_sprites = false;
}

FireAndBuletSprite.prototype.play = function (){
    var self = this;
    self.sprite_bullet.loop(); // функция для работы с спрайтом пули
    if (self.sprite_bullet.sprite_end === true) {
        self.sprite_bullet.clear_rect();
        self.sprite_fire.loop();
    }
    if (self.sprite_fire.sprite_end === true) {
        self.sprite_fire.clear_rect();
        self.end_this_sprites = true;
    }
};


// функция создания спрайтов
var create_fire_and_bullet = function(url_image_fire, url_image_bullets, sprite_canvas) {

    var sprite_context = sprite_canvas.getContext('2d');
    //"sprite_bullet_and_fire.png";
    var bulletImage = new Image();
    bulletImage.src = url_image_bullets; 
    var sprite_bullet = new Sprite({
        context: sprite_context,
        width: 544,
        height: 35,
        start_point_height: 256-16,
        image: bulletImage,
        numberOfFrames: 34, // число кадров в спрайте (каждый кадр должен быть одинаков по размера dy, dx)
        path_points: [[580, 480], [320, 240]], //точки перемещения спрайта
        is_dying_because_of_the_way: true
    });

    var fireImage = new Image();
    fireImage.src = url_image_fire; 
    var sprite_fire = new Sprite({
        context: sprite_context,
        width: 506,
        height: 35,
        start_point_height: 120,
        image: fireImage,
        numberOfFrames: 13, // число кадров в спрайте (каждый кадр должен быть одинаков по размера dy, dx)
        path_points: [ [320, 240],[320, 240]], //точки перемещения спрайта
        is_dying_because_of_last_frame: true
    });

    var fire_and_bullet_sprite = new FireAndBuletSprite({
        'sprite_fire': sprite_fire,
        'sprite_bullet': sprite_bullet
        });

    return fire_and_bullet_sprite;
};