import arcade


WIDTH = 640
HEIGHT = 480

def update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    # Draw in here...
    def treecoord(startx, starty, end, pixels):
        for trees in range(startx, end):
            if startx <= end-20:
                arcade.draw_xywh_rectangle_filled(startx, starty, 20, 30, arcade.color.BROWN)
                arcade.draw_triangle_filled(startx-20, starty+30, startx+40, starty+30, startx+10, starty+100, arcade.color.GO_GREEN)
            startx += pixels

    treecoord(140, 100, WIDTH, 100)
    treecoord(40, 10, 400, 60)
    treecoord(70, 200, 500, 30)
    treecoord(0, 300, WIDTH, 1)
def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Trees")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 0)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()