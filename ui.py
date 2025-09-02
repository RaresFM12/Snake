from service import Service


class UI:
    def __init__(self):
        self.__service = Service()
        self.__game_over = False

    def run_ui(self):
        print("This is the board:")
        b = self.__service.get_board()
        print(b)

        while not self.__game_over:
            cmd = input("Enter your command: ")
            cmd = cmd.split(" ")

            if cmd[0] == "up":
                try:
                    self.__service.moves_up()
                    self.__game_over = self.__service.get_over()

                    if self.__game_over:
                        print("The game is over!")
                        break
                    else:
                        b = self.__service.get_board()
                        print(b)

                except ValueError as ve:
                    print(ve)

            elif cmd[0] == "down":
                try:
                    self.__service.moves_down()
                    self.__game_over = self.__service.get_over()

                    if self.__game_over:
                        print("The game is over!")
                        break
                    else:
                        b = self.__service.get_board()
                        print(b)

                except ValueError as ve:
                    print(ve)

            elif cmd[0] == "left":
                try:
                    self.__service.moves_left()
                    self.__game_over = self.__service.get_over()

                    if self.__game_over:
                        print("The game is over!")
                        break
                    else:
                        b = self.__service.get_board()
                        print(b)

                except ValueError as ve:
                    print(ve)

            elif cmd[0] == "right":
                try:
                    self.__service.moves_right()
                    self.__game_over = self.__service.get_over()

                    if self.__game_over:
                        print("The game is over!")
                        break
                    else:
                        b = self.__service.get_board()
                        print(b)

                except ValueError as ve:
                    print(ve)

            elif cmd[0] == "move":
                try:
                    if len(cmd) == 1:
                        n = 1
                    else:
                        n = int(cmd[1])
                        
                    dir =  self.__service.get_last_operation()

                    if dir == "up" or dir == "":
                        for i in range(n):
                            try:
                                self.__service.moves_up()
                                self.__game_over = self.__service.get_over()

                                if self.__game_over:
                                    print("The game is over!")
                                    exit()

                            except ValueError as ve:
                                print(ve)

                        b = self.__service.get_board()
                        print(b)

                    elif dir == "down":
                        for i in range(n):
                            try:
                                self.__service.moves_down()
                                self.__game_over = self.__service.get_over()

                                if self.__game_over:
                                    print("The game is over!")
                                    exit()

                            except ValueError as ve:
                                print(ve)

                        b = self.__service.get_board()
                        print(b)

                    elif dir == "left":
                        for i in range(n):
                            try:
                                self.__service.moves_left()
                                self.__game_over = self.__service.get_over()

                                if self.__game_over:
                                    print("The game is over!")
                                    exit()

                            except ValueError as ve:
                                print(ve)

                        b = self.__service.get_board()
                        print(b)

                    elif dir == "right":
                        for i in range(n):
                            try:
                                self.__service.moves_right()
                                self.__game_over = self.__service.get_over()

                                if self.__game_over:
                                    print("The game is over!")
                                    exit()

                            except ValueError as ve:
                                print(ve)

                        b = self.__service.get_board()
                        print(b)

                except:
                    pass

            else:
                print("Bad command!")