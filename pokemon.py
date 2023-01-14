import random

class Pokemon:
    def __init__(self, name, level, types, moves, stats):
        self.name = name
        self.level = level
        self.types = types
        self.moves = moves
        self.stats = stats
        self.shiny = False
        self.hp = self.calculate_max_hp()
        self.status = None

    def calculate_max_hp(self):
        base_hp = self.stats["hp"]
        level = self.level
        max_hp = ((2 * base_hp + 100) * level) / 100 + level + 10
        return max_hp

    def use_move(self, move_index, opponent):
        move = self.moves[move_index]
        move_type = move.type
        opponent_type = opponent.types

        # check type effectiveness
        effectiveness = 1
        if move_type in opponent_type:
            effectiveness = 2
        elif move_type not in opponent_type:
            effectiveness = 0.5

        damage = self.calculate_damage(move, opponent, effectiveness)
        opponent.take_damage(damage)

    def calculate_damage(self, move, opponent, effectiveness):
        attack = self.stats["attack"]
        defense = opponent.stats["defense"]
        base

class Trainer:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.items = []
        self.money = 0

    def battle(self, opponent):
        player_pokemon = self.party[self.current_pokemon]
        opponent_pokemon = opponent.party[opponent.current_pokemon]

        while player_pokemon.hp > 0 and opponent_pokemon.hp > 0:
            print("Your Pokemon:", player_pokemon.name)
            print("Opponent's Pokemon:", opponent_pokemon.name)
            print("What would you like to do?")
            print("1. Fight")
            print("2. Switch Pokemon")
            print("3. Use Item")
            choice = input("Enter choice: ")
            if choice == "1":
                print("Which move would you like to use?")
                for i, move in enumerate(player_pokemon.moves):
                    print(i+1, move.name)
                move_choice = int(input("Enter move choice: ")) - 1
                player_pokemon.use_move(move_choice, opponent_pokemon)
            elif choice == "2":
                print("Which Pokemon would you like to switch to?")
                for i, poke in enumerate(self.party):
                    print(i+1, poke.name)
                switch_choice = int(input("Enter switch choice: ")) - 1
                self.switch_pokemon(switch_choice)
            elif choice == "3":
                print("Which item would you like to use?")
                for i, item in enumerate(self.items):
                    print(i+1, item.name)
                item_choice = int(input("Enter item choice: ")) - 1
                self.use_item(item_choice, player_pokemon)

            if opponent_pokemon.hp <= 0:
                print("Opponent's", opponent_pokemon.name, "fainted.")
                opponent.switch_pokemon()

        if player_pokemon.hp <= 0:
            print("Your", player_pokemon.name, "fainted.")
            self.switch_pokemon()
        elif opponent_p
class Item:
    def __init__(self, name, item_type, target, effect, quantity):
        self.name = name
        self.item_type = item_type # 'heal' or 'status'
        self.target = target # 'self' or 'opponent'
        self.effect = effect # amount of hp restored or status effect applied
        self.quantity = quantity

    def use(self, target_pokemon):
        if self.item_type == 'heal':
            target_pokemon.hp += self.effect
            print("Used", self.name, "to restore", self.effect, "HP to", target_pokemon.name)
            self.quantity -= 1
        elif self.item_type == 'status':
            target_pokemon.status = self.effect
            print("Used", self.name, "to give", target_pokemon.name, self.effect, "status effect.")
            self.quantity -= 1
        if target_pokemon.hp > target_pokemon.calculate_max_hp():
            target_pokemon.hp = target_pokemon.calculate_max_hp()
class Pokemon:
    def __init__(self, name, level, types, moves, base_stats):
        self.name = name
        self.level = level
        self.types = types
        self.moves = moves
        self.base_stats = base_stats
        self.shiny = False
        self.hp = self.calculate_max_hp()
        self.status = None

    def calculate_max_hp(self):
        base_hp = self.base_stats["hp"]
        level = self.level
        max_hp = ((2 * base_hp + 100) * level) / 100 + level + 10
        return max_hp

    def use_move(self, move_index, opponent):
        move = self.moves[move_index]
        move_type = move.type
        opponent_type = opponent.types

        # check type effectiveness
        effectiveness = 1
        if move_type in opponent_type:
            effectiveness = 2
        elif move_type not in opponent_type:
            effectiveness = 0.5

        damage = self.calculate_damage(move, opponent, effectiveness)
        opponent.take_damage(damage)

    def calculate_damage(self, move, opponent, effectiveness):
        level = self.level
        attack = self.base_stats["attack"]
        defense = opponent.base_stats["defense"]
        power = move.power
        random_factor = random.randint(85, 100) / 100
        damage = (((2 * level + 10) / 250) * (attack / defense) * power + 2) * effectiveness


class Trainer:
    def __init__(self, name, party, items):
        self.name = name
        self.party = party
        self.items = items
        self.current_pokemon = 0

    def battle(self, opponent):
        while True:
            print("What would you like to do? \n1. Fight \n2. Pokemon \n3. Bag \n4. Run")
            choice = input()
            if choice == "1":
                print("Which move would you like to use?\n")
                for i, move in enumerate(self.party[self.current_pokemon].moves):
                    print(f"{i + 1}. {move.name}")
                move_choice = int(input()) - 1
                self.party[self.current_pokemon].use_move(move_choice, opponent)
            elif choice == "2":
                print("Which Pokemon would you like to switch to?\n")
                for i, pokemon in enumerate(self.party):
                    print(f"{i + 1}. {pokemon.name}")
                switch_choice = int(input()) - 1
                self.switch_pokemon(switch_choice)
            elif choice == "3":
                print("Which item would you like to use?\n")
                for i, item in enumerate(self.items):
                    print(f"{i + 1}. {item.name}")
                item_choice = int(input()) - 1
                self.use_item(item_choice, opponent)
            elif choice == "4":
                run_chance = random.random()
                if run_chance <= 0.5:
                    print("Got away safely!")
                    break
                else:
                    print("Can't escape!")

    def switch_pokemon(self, index):
        self.current_pokemon = index
        print(f"Go! {self.party[self.current_pokemon].name}!")

    def use_item(self, item_index, target):
        item = self.items[item_index]
        if item.item_type == "heal":
            target.hp += item.effect
            target.hp = min(target.hp, target.calculate_max_hp())
            print(f"{target.name}'s HP was restored by {item.effect}.")
            self.items[item_index].quantity -= 1
            if self.items[item_index].quantity <= 0:
                del self.items[item_index]
        elif item.item_type == "status":
            target.apply_status(item.effect)
            print(f"{target.name} was affected by {item.effect}.")

class Item:
    def __init__(self, name, item_type, target, effect, quantity):
        self.name = name
        self.item_type = item_type
        self.target = target
        self.effect = effect
        self.quantity = quantity

    def use(self, target):
        if self.item_type == "healing":
            target.hp += self.effect
            if target.hp > target.max_hp:
                target.hp = target.max_hp
            print(f"{target.name}'s HP has been restored by {self.effect} points!")
        elif self.item_type == "status":
            target.status = self.effect
            print(f"{target.name} has been inflicted with {self.effect}!")
        elif self.item_type == "capture":
            capture_odds = self.effect
            random_number = random.random()
            if random_number <= capture_odds:
                print(f"{target.name} has been caught!")
                self.quantity -= 1
                return True
            else:
                print(f"Failed to catch {target.name}")
                return False
        self.quantity -= 1

class Game:
    def __init__(self, player, towns, gyms):
        self.player = player
        self.towns = towns
        self.gyms = gyms
        self.current_town = None
        self.current_opponent = None

    def start(self):
        self.current_town = self.towns[0]
        self.display_menu()

    def display_menu(self):
        print("1. Explore Town")
        print("2. Battle")
        print("3. Pokemon")
        print("4. Bag")
        print("5. Save")
        print("6. Quit")
        choice = input("What would you like to do? ")
        if choice == "1":
            self.explore_town()
        elif choice == "2":
            self.start_battle()
        elif choice == "3":
            self.display_party()
        elif choice == "4":
            self.display_bag()
        elif choice == "5":
            self.save_game()
        elif choice == "6":
            self.quit_game()

    def start_battle(self, wild=True):
        if wild:
            wild_pokemon = self.generate_wild_pokemon()
            self.current_opponent = wild_pokemon
            print("A wild", wild_pokemon.name, "appeared!")
        else:
            trainer = self.generate_trainer()
            self.current_opponent = trainer
            print(trainer.name, "wants to battle!")

        while True:
            print("What would you like to do?")
            print("1. Fight")
            print("2. Switch Pokemon")
            print("3. Use Item")
            print("4. Run")

            def catch_pokemon(self, wild_pokemon):
                # Check if the player has any Pokeballs
                pokeballs = [item for item in self.player.items if item.name == "Pokeball"]
                if not pokeballs:
                    print("You don't have any Pokeballs!")
                    return

                # Use the first Pokeball in the player's inventory
                pokeball = pokeballs[0]
                pokeball.use(wild_pokemon)

                # Check if the Pokemon was caught
                if wild_pokemon.caught:
                    print("Congratulations! You caught a", wild_pokemon.name + "!")
                    self.player.party.append(wild_pokemon)
                else:
                    print("Oh no! The", wild_pokemon.name, "broke free!")

                    class Game:
                        def __init__(self, player, towns, gyms):
                            self.player = player
                            self.towns = towns
                            self.gyms = gyms
                            self.current_town = None
                            self.current_opponent = None

                        def catch_pokemon(self, wild_pokemon):
                            print("A wild", wild_pokemon.name, "appeared!")
                            print("What would you like to do?")
                            print("1. Throw a Pokeball")
                            print("2. Use a status move")
                            print("3. Run")
                            choice = input("Enter your choice: ")

                            if choice == "1":
                                catch_rate = wild_pokemon.catch_rate  # catch rate of the wild Pokemon
                                shake_count = 0
                                while shake_count < 4:
                                    rand_num = random.randint(0, 255)
                                    if rand_num < catch_rate:
                                        print("Gotcha! ", wild_pokemon.name, "was caught!")
                                        self.player.party.append(wild_pokemon)
                                        break
                                    shake_count += 1
                                    print("Shake...")
                                else:
                                    print("Oh no! The Pokemon broke free!")

                            elif choice == "2":
                                # code for using a status move
                                pass
                            elif choice == "3":
                                # code for running
                                pass
class Game:
    def __init__(self, player, towns, gyms):
        self.player = player
        self.towns = towns
        self.gyms = gyms
        self.current_town = None
        self.current_opponent = None

    def catch_pokemon(self, wild_pokemon):
        print("A wild", wild_pokemon.name, "appeared!")
        print("What would you like to do?")
        print("1. Throw a Pokeball")
        print("2. Use a status move")
        print("3. Run")
        choice = input("Enter your choice: ")

        if choice == "1":
            catch_rate = wild_pokemon.catch_rate # catch rate of the wild Pokemon
            shake_count = 0
            while shake_count < 4:
                rand_num = random.randint(0, 255)
                if rand_num < catch_rate:
                    print("Gotcha! ", wild_pokemon.name, "was caught!")
                    self.player.party.append(wild_pokemon)
                    break
                shake_count += 1
                print("Shake...")
            else:
                print("Oh no! The Pokemon broke free!")

        elif choice == "2":
            # code for using a status move
            pass
        elif choice == "3":
            # code for running
            pass
class Game:
    def __init__(self, player, towns, gyms):
        self.player = player
        self.towns = towns
        self.gyms = gyms
        self.current_town = None
        self.current_opponent = None

    def catch_pokemon(self, wild_pokemon):
        print("A wild", wild_pokemon.name, "appeared!")
        print("What would you like to do?")
        print("1. Throw a Pokeball")
        print("2. Use a status move")
        print("3. Run")
        choice = input("Enter your choice: ")

        if choice == "1":
            catch_rate = wild_pokemon.catch_rate # catch rate of the wild Pokemon
            shake_count = 0
            while shake_count < 4:
                rand_num = random.randint(0, 255)
                if rand_num < catch_rate:
                    print("Gotcha! ", wild_pokemon.name, "was caught!")
                    self.player.party.append(wild_pokemon)
                    break
                shake_count += 1
                print("Shake...")
            else:
                print("Oh no! The Pokemon broke free!")

        elif choice == "2":
            # code for using a status move
            pass
        elif choice == "3":
            # code for running
            pass
class Pokemon:
    def __init__(self, name, level, types, moves, base_stats, shiny=False, evolves_at=None, evolves_to=None):
        self.name = name
        self.level = level
        self.types = types
        self.moves = moves
        self.base_stats = base_stats
        self.shiny = shiny
        self.hp = self.calculate_max_hp()
        self.status = None
        self.experience = 0
        self.evolves_at = evolves_at
        self.evolves_to = evolves_to

    def calculate_max_hp(self):
        base_hp = self.base_stats["hp"]
        level = self.level
        max_hp = ((2 * base_hp + 100) * level) / 100 + level + 10
        return max_hp

    def give_experience(self, experience):
        self.experience += experience
        if self.experience >= self.level*self.level*self.level:
            self.level += 1
            self.hp = self.calculate_max_hp()
            for key in self.base_stats:
                self.base_stats[key] += 5
            if self.evolves_at and self.level >= self.evolves_at:
                self.evolve()

    def evolve(self):
        if self.evolves_to:
            self.name = self.evolves_to
            self.types = POKEMON_DATA[self.evolves_to]['types']
            self.base_stats = POKEMON_DATA[self.evolves_to]['base_stats']
            self.moves = POKEMON_DATA[self.evolves_to]['moves']
            self.evolves_at = POKEMON_DATA[self.evolves_to]['evolves_at']
            self.evolves_to = POKEMON_DATA[self.evolves_to]['evolves_to']
            print(f'{self.name} has evolved!')

class Trainer:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.items = []
        self.money = 0

    def battle(self, opponent):
        player_pokemon = self.party[self.current_pokemon]
        opponent_pokemon = opponent.party[opponent.current_pokemon]

        while player_pokemon.hp > 0 and opponent_pokemon.hp > 0:
            print("Your Pokemon:", player_pokemon.name)
            print("Opponent's Pokemon:", opponent_pokemon.name)
            print("What would you like to do?")
            print("1. Fight")
            print("2. Switch Pokemon")
            print("3. Use Item")
            choice = input("Enter choice: ")
            if choice == "1":
                print("Which move would you like to use?")
                for i, move in enumerate(player_pokemon.moves):
                    print(i+1, move.

                    def calculate_damage(self, move, opponent):
                        attack = self.stats["attack"]
                        defense = opponent.stats["defense"]
                        base_damage = move.base_damage
                        level = self.level
                        effective = move.effective
                        STAB = 1
                        if move.type in self.types:
                            STAB = 1.5
                        damage = ((2 * level + 10) / 250) * (attack / defense) * base_damage * STAB * effective + 2
                        return damage

                    def switch_pokemon(self, index):
                        if index >= 0 and index < len(self.party):
                            self.current_pokemon = index
                            print(f'{self.name} switched to {self.party[index].name}')

                            def take_damage(self, damage):
                                self.hp -= damage
                                if self.hp < 0:
                                    self.hp = 0
                                print(f'{self.name} took {damage} damage and has {self.hp} HP left.')

                                def check_fainted(self):
                                    if self.party[self.current_pokemon].hp <= 0:
                                        print(f'{self.party[self.current_pokemon].name} has fainted!')
                                        self.switch_

                                        class NPCTrainer:
                                            def __init__(self, name, party):
                                                self.name = name
                                                self.party = party
                                                self.current_pokemon = 0

                                            def battle(self, player):
                                                opponent_pokemon = self.party[self.current_pokemon]
                                                player_pokemon = player.party[player.current_pokemon]

                                                # battle logic here

class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type # 'heal' or 'status'
        self.effect = effect # amount of hp restored or status effect applied

    def use(self, target_pokemon):
        if self.item_type == 'heal':
            target_pokemon.hp += self.effect
            print(f'Used {self.name} to restore {self.effect} HP to {target_pokemon.name}.')
        elif self.item_type == 'status':
            target_pokemon.status = self.effect
            print(f'Used {self.name} to apply {self.effect} status effect to {target_pokemon.name}.')

            class Pokedex:
                def __init__(self):
                    self.entries = {}

                def add_entry(self, pokemon):
                    self.entries[pokemon.name] = pokemon

                def show_entry(self, pokemon_name):
                    if pokemon_name in self.entries:
                        pokemon = self.entries[pokemon_name]
                        print(f'Name: {pokemon.name}')
                        print(f'Types: {pokemon.types}')
                        print(f'Base Stats: {pokemon.base_stats}')
                        print(f'Moves: {[move.name for move in pokemon.moves]}')
                    else:
                        print(f'{pokemon_name} not found in Pokedex.')

                        def catch_pokemon(self, pokemon):
                            catch_rate = pokemon.catch_rate
                            ball_type = input("Which ball would you like to use? (Poke/Great/Ultra)")
                            if ball_type == "Poke":
                                ball_rate = 0
