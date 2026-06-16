import arcade

# Open a window
arcade.open_window(600, 600, "My New Game")
arcade.set_background_color(arcade.color.SKY_BLUE)

# Start the render process
arcade.start_render()
arcade.draw_text("Hello World!", 250, 300, arcade.color.WHITE, 20)
arcade.finish_render()

# Keep the window open
arcade.run()