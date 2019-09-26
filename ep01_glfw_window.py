import glfw


# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
window = glfw.create_window(1280, 720, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# make the context current
glfw.make_context_current(window)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
