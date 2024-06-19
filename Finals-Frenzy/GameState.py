class GameState:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.exam_score = [10, 12, 14, 16, 18]
        self.exam_index = 0
        self.running = True

    def update(self, player, collisions):
        for collision in collisions:
            if collision.obj_type == 'support':
                self.score += 0.5
            else:
                player.energy -= 15

        if self.score >= self.exam_score[self.exam_index]:
            self.level_up()
            self.score = 0
            player.energy = 100

        if player.energy <= 0:
            print("Franklin ira a susti :(")
            self.running = False

    def level_up(self):
        self.level += 1
        self.exam_index += 1
        if self.exam_index >= len(self.exam_score):
            print("Franklin paso el semestre :D sin ir a susti!")
            self.running = False