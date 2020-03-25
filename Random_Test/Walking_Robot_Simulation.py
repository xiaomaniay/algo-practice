class Solution:
    """
    @param commands: type: List[int]
    @param obstacles: type: List[List[int]]
    @return: Return the square of the maximum Euclidean distance
    """
    def robotSim(self, commands, obstacles):
        pos = [0, 0]
        direction = 0  # set direction: 0, 1, 2, 3 anticlockwise from the north
        for i in range(len(commands)):
            if commands[i] < 0:
                if commands[i] == -2:
                    direction = (direction + 1) % 4
                if commands[i] == -1:
                    direction = (direction - 1) % 4
            else:
                if direction == 0:
                    new_pos = [pos[0], pos[1] + commands[i]]
                    for j in range(len(obstacles)):
                        if obstacles[j][0] == new_pos[0] and  pos[1] < obstacles[j][1] <= new_pos[1]:
                            new_pos[1] = obstacles[j][1] - 1
                elif direction == 2:
                    new_pos = [pos[0], pos[1] - commands[i]]
                    for j in range(len(obstacles)):
                        if obstacles[j][0] == new_pos[0] and  new_pos[1] <= obstacles[j][1] < pos[1]:
                            new_pos[1] = obstacles[j][1] + 1
                elif direction == 3:
                    new_pos = [pos[0] + commands[i], pos[1]]
                    for j in range(len(obstacles)):
                        if obstacles[j][1] == new_pos[1] and pos[0] < obstacles[j][0] <= new_pos[0]:
                            new_pos[0] = obstacles[j][0] - 1
                else:
                    new_pos = [pos[0] - commands[i], pos[1]]
                    for j in range(len(obstacles)):
                        if obstacles[j][1] == new_pos[1] and new_pos[0] <= obstacles[j][0] < pos[0]:
                            new_pos[0] = obstacles[j][0] + 1
                pos = new_pos

        return pos[0]**2 + pos[1]**2


commands = [4,-1,4,-2,4]
obstables = [[2,4]]
print(Solution().robotSim(commands, obstables))

