import simplegui

frame = simplegui.create_frame("Home", 500, 500)

class ShapeAttributes:
    
    def __init__(self):
        self.line_width = 10
        self.line_color = "grey"
        self.fill_color = "blue"

class Circle:
    
    def __init__(self):
        self.radius = 33
        self.center_point = (100, 100)
        
    def update_x(self, shift_x):
        self.center_point = (
            self.center_point[0] + shift_x,
            self.center_point[1]
        )
        
    def update_y(self, shift_y):
        self.center_point = (
            self.center_point[0],
            self.center_point[1] + shift_y
        )

class Character:

    key_map = {
        "left": 37,
        "up": 38,
        "right": 39,
        "down": 40
    }
    
    move_dist = 2
    vel = [1, 1]
    
    
    
    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttributes()
        
    def draw_me(self, canvas):
         
        self.circle_shape.center_point = (
        self.circle_shape.center_point[0] +  Character.vel[0],
        self.circle_shape.center_point[1] + Character.vel[1]
        )
        
        canvas.draw_circle(
            self.circle_shape.center_point,
            self.circle_shape.radius,
            self.shape_attributes.line_width,
            self.shape_attributes.line_color,
            self.shape_attributes.fill_color
         )
        
    def move(self, key):
        if key in Character.key_map.values():
            if key == Character.key_map["right"]:
                print "move right"
                Character.vel =[Character.move_dist,0]
            if key == Character.key_map["left"]:
                print "move left"
                Character.vel = [-Character.move_dist,0]
            if key == Character.key_map["up"]:
                print "move up"
                Character.vel =[0, -Character.move_dist]

           
            if key == Character.key_map["down"]:
                print "move down"
                Character.vel =[0, Character.move_dist]              
cliq = Character()


#========add this code==================
def rect_coords (length, height, startpos = (0, 0)) :
    
    return [
        (startpos[0], startpos[1]),
        (startpos[0], startpos[1] + height),
        (startpos[0] + length, startpos[1] + height),
        (startpos[0] + length, startpos[1])  
    ]

box = rect_coords(500, 500)
#===============================



def draw(canvas):
    cliq.draw_me(canvas)
    
    #===========add this line===============
    canvas.draw_polygon(box, 20, "red")
    

frame.set_draw_handler(draw)
frame.set_keydown_handler(cliq.move)
frame.start()
