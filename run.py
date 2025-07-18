import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Session1.settings')
django.setup()

from Games.models import GameSession, Word_Chain_player, Word_Chain_words

class CreateGameSession:
    def __init__(self, game_status):
        self.game_status = "waiting"

    def create_game_session(self, game_status, creator_name): 


        self.game_session = GameSession.objects.create(game_status=game_status)
        
        # Set the creator as the first player and mark as creator
        self.creator = Word_Chain_player.objects.create(
            player_name=creator_name,
            player_status='creator',
            game_session_joined=self.game_session,
            player_turn_order=0
        )
        self.game_session.current_player = self.creator
        self.game_session.save()

    def join_game(self, player_name, player_status='waiting', player_turn_order=None):
        if self.game_session.game_status != "waiting":
            raise ValueError("Cannot join a game that is not in waiting status.")
        existing_players = Word_Chain_player.objects.filter(game_session_joined=self.game_session).count()
        if player_turn_order is None:
            player_turn_order = existing_players
        player = Word_Chain_player.objects.create(
            player_name=player_name,
            player_status=player_status,
            game_session_joined=self.game_session,
            player_turn_order=player_turn_order
        )
        return player

    def start_game(self, player):
        # Only the creator can start the game
        if player != self.creator:
            raise ValueError("Only the creator can start the game.")
        if self.game_session.game_status != "waiting":
            raise ValueError("Game has already started or finished.")
        self.game_session.game_status = "playing"
        self.game_session.save()

    def add_word(self, word_provided, player_who_provided, word_used_already):
        if self.game_session.game_status != "playing":
            raise ValueError("Game is not in playing status.")
        if len(word_provided) > 3:
            word_used_already = Word_Chain_words.objects.filter(word_game_session=self.game_session, word_provided=word_provided).exists()
            if word_used_already:
                raise ValueError("This word has already been used in the game.")
            if self.game_session.last_word and word_provided[0].lower() != self.game_session.last_word[-1].lower():
                raise ValueError("The first letter of the provided word does not match the last letter of the last word used in the game.")
            self.wordSession = Word_Chain_words.objects.create(word_provided = word_provided,player_who_provided = player_who_provided, word_used_already=word_used_already, word_game_session=self.game_session)
            # self.word_provided = input("Enter the word you want to provide: ")
            # word = Word_Chain_words.objects.create(
            #     word_provided=self.word_provided,
            #     player_who_provided=player_who_provided,
            #     word_used_already=word_used_already,
            #     word_game_session=self.game_session
            # )
            # self.game_session.last_word = word.word_provided
            # self.game_session.save()
            # return word

    def next_turn(self):
        players = Word_Chain_player.objects.filter(game_session_joined=self.game_session).order_by('player_turn_order')
        if players.count() == 1:
            self.game_session.winner = players.first()
            self.game_session.game_status = 'finished'
            self.game_session.save()
            return
        if not self.game_session.current_player:
            self.game_session.current_player = players[0]
            self.game_session.save()
            return
        current_player = self.game_session.current_player
        players_list = list(players)
        try:
            current_index = players_list.index(current_player)
        except ValueError:
            self.game_session.current_player = players[0]
            self.game_session.save()
            return
        next_index = (current_index + 1) % players.count()
        self.game_session.current_player = players_list[next_index]
        self.game_session.save()

    def main(self):
        print("Welcome to Word Chain!")
        decision = input("Create Game or Join Game? (C/J): ").strip().lower()
        if decision == "c":
            creator_name = input("Enter your name (creator): ")
            game_status = "waiting"
            self.create_game_session(game_status, creator_name)
            print(f"Game session created by {creator_name}. Session code: {self.game_session.id}")
            print("Share this code with friends so they can join.")
            input("Press Enter when all players have joined and you want to start the game...")
            self.start_game(self.creator)
            print("Game started!")
            print("\nLet the game begin! Players take turns to add words.")
            
            while self.game_session.game_status == "playing":
                current_player = self.game_session.current_player
                
                print(f"\nIt's {current_player.player_name}'s turn.")
                word = input(f"{current_player.player_name}, enter your word: ").strip()
                try:
                    self.add_word(word, current_player, False)
                    self.game_session.last_word = word
                    self.wordSession.word_provided = word
                    self.game_session.save()
                    
                except Exception as e:
                    print(f"Error: {e}")
                    continue
                self.next_turn()
            print("Game over!")
        elif decision == "j":
            join_existing_game()
        else:
            print("Invalid option. Exiting.")

def join_existing_game():
    session_code = input("Enter the game session code: ")
    print(session_code)
    player_name = input("Enter your name: ")
    try:
        session = GameSession.objects.get(id=session_code, game_status='waiting')
    except GameSession.DoesNotExist:
        print("No active game session found with that code.")
        return
    existing_players = Word_Chain_player.objects.filter(game_session_joined=session).count()
    player = Word_Chain_player.objects.create(
        player_name=player_name,
        player_status='waiting',
        game_session_joined=session,
        player_turn_order=existing_players
    )
    print(f"Player '{player.player_name}' joined the game. Waiting for the creator to start the game...")

p = CreateGameSession(game_status="waiting")
if __name__ == "__main__":
    p.main()












