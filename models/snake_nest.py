class Nest:
    def __init__(self):
        self.snake_position_list = list()

    def get_snakes_positions(self):
        return self.snake_position_list

    def add_new_snake_to_nest(self, new_snake):
        self.snake_position_list.append(new_snake)


snake_nest = Nest()
