import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls):
        self.contents=self._get_content(balls)
    
    #methods
    def _get_content(self,balls):
        colors=[]
        for color,quantity in balls.items():
            for n in range(quantity):
                colors.append(color)
        return colors
    
    def draw(self,balls_to_draw):
        draw_list=[]
        if balls_to_draw> len(self.contents):
            return self.contents
        for _ in range(balls_to_draw):
            draw_one_ball=random.choice(self.contents)
            self.contents.remove(draw_one_ball)
            draw_list.append(draw_one_ball)
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches=0
    if num_balls_drawn>=len(hat.contents):
        return 1.0
    for experiment in range(num_experiments):
        content_for_experiment=copy.copy(hat.contents)
        draw_list=[]
        for _ in range(num_balls_drawn):
            draw_one_ball=random.choice(content_for_experiment)
            content_for_experiment.remove(draw_one_ball)
            draw_list.append(draw_one_ball)
        is_match='True'
        for color,quantity in expected_balls.items():
            if color not in draw_list:
                is_match= not is_match
                break
            ball_num=0
            for ball in draw_list:
                if ball == color:
                    ball_num+=1
            if ball_num < quantity:
                is_match= not is_match
                break
        if is_match:
            matches+=1
    return matches/num_experiments