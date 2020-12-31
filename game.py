import sys, os, json, pygame, time,  graphics

# List of [object, object rectangle] lists
objects = []
forces = []
cur_level = None
sleep = time.sleep
def load_level(level):
	with open(os.path.join('gamedata', level), 'r') as f:
		global cur_level
		cur_level = json.loads(f.read())
def load_objects():
	if cur_level:
		data = cur_level['data']
		level_objects = data['objects']
		object_types = data['object_types']
		for obj in level_objects:
			object_type = data['object_types'][obj['object_type']]
			model = object_type['model']
			model = model if model else 'placeholder.gif'
			model_obj = pygame.image.load(os.path.join('assets', model))
			if 'size' in obj:
				model_obj = pygame.transform.scale(model_obj, obj['size'])
			game_obj = graphics.GameObject(object_type, obj['position'], obj['speed'], model_obj)

			objects.append(game_obj)


def detect_coll(obj, r):
	pass
def apply_forces(speed):
	for F in forces:
		F(speed)
def process_controls():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
			if event.mod == pygame.KMOD_NONE:
				pass
			else:
				if event.mod & pygame.KMOD_LSHIFT:
					pass
				if event.mod & pygame.KMOD_RSHIFT:
					pass
				if event.mod & pygame.KMOD_SHIFT:
					pass
		# Key pressed event
		if event.type == pygame.KEYDOWN:
			pass
		# Key released event
		if event.type == pygame.KEYUP:
			pass
move_buffer = [0,0]
def tick(objects):
	# Check events (currently for game quit event)
	process_controls()

	for ob in objects:
		r=ob.rect
		speed = ob.speed

		if getattr(ob, 'physics', False):
			apply_forces(speed)
		# Perform collide step
		if getattr(ob, 'collidable', False):
			detect_coll(ob, r)
		# # collision detection
		# def wall_coll(obj, r):
		# 	speed = obj.speed
		# 	if r.left < 0 or r.right > width:
		# 		speed[0] = -speed[0]
		#
		# 	if r.top < 0 or r.bottom > height:
		# 		speed[1] = -speed[1]
		# wall_coll(ob, r)
		# Perform move step

		move_buffer[0] = int(speed[0])
		move_buffer[1] = int(speed[1])
		if getattr(ob, 'moveable', False):
			move_buffer[0] = move_buffer[0] if r.left+move_buffer[0]<0 else move_buffer[0]
			r = r.move(move_buffer)
		ob.rect = r

def game_loop():
	# (False) Game loop (performance tied to framerate)
	while True:
		# Tick
		tick(objects)
		# Render
		graphics.render(objects)
		sleep(.01)

if __name__ == '__main__':
	load_level('level1.json')
	load_objects()
	graphics.setup()

	global size, width, height
	size = width, height = graphics.size

	def gravity(v):
		v[1] = v[1]+9.8
	def friction(v):
		v[0] = v[0]*0.95
		v[1] = v[1]*0.95
		v[0] = 0 if v[0]<1 else v[0]
		v[1] = 0 if v[1]<1 else v[1]
	forces.append(gravity)
	forces.append(friction)

	game_loop()
