import sys, pygame
class GameObject:
	def __init__(self, object, moveable=True, collidable=True):
		self.moveable=moveable
		self.collidable=collidable
		self.object = object
		self.speed = [2,2]
		self.rect = object.get_rect()

# collision detection
def coll_detect(obj, r):
	speed = obj.speed
	if r.left < 0 or r.right > width:
		speed[0] = -speed[0]
	if r.top < 0 or r.bottom > height:
		speed[1] = -speed[1]

background = black = 0, 0, 0


def setup(w = 1024, h = 640):
	global size, width, height, objects
	size = width, height = w, h
	# List of [object, object rectangle] lists
	objects = []

	pygame.init()

	screen = pygame.display.set_mode(size)

	ball = pygame.image.load("assets/intro_ball.gif")
	ballObj = GameObject(ball)
	ballObj.speed = [2, 2]

def start_game_loop():
	# (False) Game loop (performance tied to framerate)
	while True:

		# Tick

		# Check events (currently for game quit event)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		for ob in objects:
			r=ob.rect
			# Perform move step
			if getattr(ob, 'moveable', False):
				r = r.move(ob.speed)
			# Perform collide step
			if getattr(ob, 'collidable', False):
				coll_detect(ob, r)
			ob.rect = r

		# Draw

		# Black background/reset from previous frame
		screen.fill(background if background else black)
		# Draw objects
		for ob in objects:
			o = ob.object
			r= ob.rect
			screen.blit(o, r)
		# Update screen
		pygame.display.flip()
if __name__ == '__main__':
	setup()
	start_game_loop()
