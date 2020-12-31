import sys, pygame
class GameObject:
	def __init__(self, type, pos, speed, object, moveable=True, collidable=True, physics=True):
		self.type = type
		self.moveable = moveable
		self.collidable = collidable
		self.physics = physics
		self.object = object
		self.speed = speed
		rect = object.get_rect()
		self.rect = rect.move(pos)




background = black = 0, 0, 0


def setup(w = 1024, h = 640):
	global size, width, height
	size = width, height = w, h

	pygame.init()
	global screen
	screen = pygame.display.set_mode(size)


def render(objects):
	# Draw

	# Black background/reset from previous frame
	screen.fill(background)
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
