import random
import os
import time
import sys

# ─────────────────────────────────────────────
#  ASCII ART & UI HELPERS
# ─────────────────────────────────────────────

LOGO = r"""
 ██╗   ██╗███╗   ██╗ ██████╗     ███████╗██╗     ██╗██████╗ 
 ██║   ██║████╗  ██║██╔═══██╗    ██╔════╝██║     ██║██╔══██╗
 ██║   ██║██╔██╗ ██║██║   ██║    █████╗  ██║     ██║██████╔╝
 ██║   ██║██║╚██╗██║██║   ██║    ██╔══╝  ██║     ██║██╔═══╝ 
 ╚██████╔╝██║ ╚████║╚██████╔╝    ██║     ███████╗██║██║     
  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚══════╝╚═╝╚═╝     
"""

LIGHT_SIDE_BANNER = """
╔══════════════════════════════════════╗
║       ☀  LIGHT SIDE ACTIVE  ☀       ║
╚══════════════════════════════════════╝"""

DARK_SIDE_BANNER = """
╔══════════════════════════════════════╗
║       🌑  DARK SIDE ACTIVE  🌑      ║
╚══════════════════════════════════════╝"""

COLORS = {
    "Red":    "\033[91m",
    "Green":  "\033[92m",
    "Blue":   "\033[94m",
    "Yellow": "\033[93m",
    "Pink":   "\033[95m",
    "Teal":   "\033[96m",
    "Orange": "\033[33m",
    "Purple": "\033[35m",
    "Wild":   "\033[97m",
    "Reset":  "\033[0m",
    "Bold":   "\033[1m",
    "Black":  "\033[90m",
    "BgRed":  "\033[101m",
    "BgBlue": "\033[104m",
}

def clr(color, text):
    return f"{COLORS.get(color, '')}{text}{COLORS['Reset']}"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(msg="Press Enter to continue..."):
    input(f"\n{clr('Black', msg)}")

def slow_print(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def box(text, width=44, color="Bold"):
    border = "═" * (width - 2)
    print(clr(color, f"╔{border}╗"))
    lines = text.split("\n")
    for line in lines:
        padding = width - 2 - len(line)
        print(clr(color, f"║") + f" {line}" + " " * (padding - 1) + clr(color, "║"))
    print(clr(color, f"╚{border}╝"))

# ─────────────────────────────────────────────
#  CARD DEFINITIONS
# ─────────────────────────────────────────────

LIGHT_COLORS = ["Red", "Green", "Blue", "Yellow"]
DARK_COLORS  = ["Pink", "Teal", "Orange", "Purple"]

LIGHT_NUMBERS = [str(n) for n in range(0, 10)]
DARK_NUMBERS  = [str(n) for n in range(1, 10)]  # No 0 on dark side

LIGHT_ACTIONS = ["Skip", "Reverse", "Draw Two"]
DARK_ACTIONS  = ["Skip Everyone", "Reverse", "Draw Five"]

LIGHT_WILD = ["Wild", "Wild Draw Four"]
DARK_WILD  = ["Wild", "Wild Draw Color"]

CARD_SYMBOLS = {
    "Skip":           "⊘",
    "Skip Everyone":  "⊗",
    "Reverse":        "↺",
    "Draw Two":       "+2",
    "Draw Five":      "+5",
    "Wild":           "★",
    "Wild Draw Four": "★+4",
    "Wild Draw Color":"★+C",
}

class Card:
    def __init__(self, color, value, side="light"):
        self.color = color
        self.value = value
        self.side  = side  # "light" or "dark"

    def is_wild(self):
        return self.color in ("Wild",)

    def display_color(self):
        if self.color == "Wild":
            return "Wild"
        return self.color

    def symbol(self):
        return CARD_SYMBOLS.get(self.value, self.value)

    def colored_str(self):
        sym = self.symbol()
        color_key = self.display_color()
        if color_key == "Wild":
            return clr("Wild", f"[★ {self.value}]")
        return clr(color_key, f"[{color_key[0]} {sym}]")

    def __repr__(self):
        return f"{self.color} {self.value}"

    def matches(self, other, current_color=None):
        """Can this card be played on top of `other`?"""
        top_color = current_color if current_color else other.color
        if self.color == "Wild":
            return True
        if self.color == top_color:
            return True
        if self.value == other.value:
            return True
        return False

# ─────────────────────────────────────────────
#  DECK BUILDER
# ─────────────────────────────────────────────

def build_light_side():
    deck = []
    for color in LIGHT_COLORS:
        for num in LIGHT_NUMBERS:
            deck.append(Card(color, num, "light"))
            if num != "0":
                deck.append(Card(color, num, "light"))
        for action in LIGHT_ACTIONS:
            deck.append(Card(color, action, "light"))
            deck.append(Card(color, action, "light"))
    for wild in LIGHT_WILD:
        for _ in range(4):
            deck.append(Card("Wild", wild, "light"))
    return deck

def build_dark_side():
    deck = []
    for color in DARK_COLORS:
        for num in DARK_NUMBERS:
            deck.append(Card(color, num, "dark"))
            deck.append(Card(color, num, "dark"))
        for action in DARK_ACTIONS:
            deck.append(Card(color, action, "dark"))
            deck.append(Card(color, action, "dark"))
    for wild in DARK_WILD:
        for _ in range(4):
            deck.append(Card("Wild", wild, "dark"))
    return deck

def build_deck():
    light = build_light_side()
    dark  = build_dark_side()
    # Pair them so flipping swaps the whole deck context
    paired = list(zip(light, dark))
    random.shuffle(paired)
    return paired  # list of (light_card, dark_card) tuples

# ─────────────────────────────────────────────
#  GAME STATE
# ─────────────────────────────────────────────

class UnoFlipGame:
    def __init__(self):
        self.side = "light"           # "light" or "dark"
        self.direction = 1            # 1 = normal, -1 = reversed
        self.current_color = None     # after wild is played
        self.deck_pairs = []          # (light, dark) pairs
        self.discard = []             # actual Card objects (current side)
        self.player_hand = []
        self.cpu_hand = []
        self.draw_pile = []           # Card objects (current side)
        self.scores = {"You": 0, "CPU": 0}
        self.round_num = 0

    # ── side helpers ──
    def active_card(self, pair):
        return pair[0] if self.side == "light" else pair[1]

    def flip_side(self):
        self.side = "dark" if self.side == "light" else "light"
        # Rebuild draw pile from remaining pairs, new side
        self.draw_pile = [self.active_card(p) for p in self.deck_pairs]
        random.shuffle(self.draw_pile)
        # Also convert hands  (we store indices; easier to rebuild)
        # Hands are already Card objects — we just tag them as belonging
        # to current side. On flip we swap side attribute.
        for card in self.player_hand + self.cpu_hand:
            card.side = self.side
        # Re-tag discard
        for card in self.discard:
            card.side = self.side

    def get_colors(self):
        return LIGHT_COLORS if self.side == "light" else DARK_COLORS

    # ── deck / deal ──
    def setup_round(self):
        self.round_num += 1
        self.side = "light"
        self.direction = 1
        self.current_color = None
        self.deck_pairs = build_deck()
        self.draw_pile = [self.active_card(p) for p in self.deck_pairs]
        random.shuffle(self.draw_pile)
        self.player_hand = []
        self.cpu_hand = []
        self.discard = []

        # Deal 7 cards each
        for _ in range(7):
            self.player_hand.append(self.draw_pile.pop())
            self.cpu_hand.append(self.draw_pile.pop())

        # Start discard — skip wilds for first card
        starter = self.draw_pile.pop()
        while starter.is_wild():
            self.draw_pile.insert(0, starter)
            starter = self.draw_pile.pop()
        self.discard.append(starter)
        self.current_color = starter.color

    def draw_card(self, hand, count=1):
        drawn = []
        for _ in range(count):
            if not self.draw_pile:
                # Reshuffle discard minus top
                top = self.discard.pop()
                self.draw_pile = self.discard[:]
                random.shuffle(self.draw_pile)
                self.discard = [top]
                if not self.draw_pile:
                    break
            card = self.draw_pile.pop()
            hand.append(card)
            drawn.append(card)
        return drawn

    # ── play logic ──
    def top_card(self):
        return self.discard[-1]

    def can_play(self, card):
        top = self.top_card()
        return card.matches(top, self.current_color)

    def playable_cards(self, hand):
        return [c for c in hand if self.can_play(c)]

    def play_card(self, card, hand, chosen_color=None):
        hand.remove(card)
        self.discard.append(card)
        if card.is_wild():
            self.current_color = chosen_color
        else:
            self.current_color = card.color

    # ── score ──
    def hand_score(self, hand):
        total = 0
        for card in hand:
            if card.value.isdigit():
                total += int(card.value)
            elif card.value in ("Skip", "Reverse", "Draw Two"):
                total += 20
            elif card.value in ("Skip Everyone", "Draw Five"):
                total += 30
            elif card.value in ("Wild",):
                total += 40
            elif card.value in ("Wild Draw Four", "Wild Draw Color"):
                total += 60
        return total

# ─────────────────────────────────────────────
#  DISPLAY
# ─────────────────────────────────────────────

def show_header(game):
    clear()
    print(clr("Bold", LOGO))
    if game.side == "light":
        print(clr("Yellow", LIGHT_SIDE_BANNER))
    else:
        print(clr("Purple", DARK_SIDE_BANNER))
    print()
    dir_sym = "→" if game.direction == 1 else "←"
    print(clr("Black", f"  Round {game.round_num}  |  Direction: {dir_sym}  |  "
              f"Draw pile: {len(game.draw_pile)} cards"))
    print(clr("Black", f"  Score — You: {game.scores['You']}  |  CPU: {game.scores['CPU']}"))
    print()

def show_top_card(game):
    top = game.top_card()
    col = game.current_color
    col_key = col if col else "Wild"
    col_code = COLORS.get(col_key, COLORS["Wild"])
    reset = COLORS["Reset"]
    bold  = COLORS["Bold"]
    sym   = top.symbol()
    print(clr("Bold", "  TOP CARD:"))
    print(f"  {col_code}{bold}┌─────────┐{reset}")
    print(f"  {col_code}{bold}│ {col_key:<7} │{reset}")
    print(f"  {col_code}{bold}│  {sym:^6}  │{reset}")
    print(f"  {col_code}{bold}│         │{reset}")
    print(f"  {col_code}{bold}└─────────┘{reset}")
    if game.current_color and game.current_color != top.color:
        print(clr(col_key, f"  (Color changed to: {game.current_color})"))
    print()

def show_hand(hand, label="YOUR HAND", hide=False):
    print(clr("Bold", f"  {label} ({len(hand)} cards):"))
    if hide:
        print("  " + "  ".join(clr("Black", "[?]") for _ in hand))
    else:
        for i, card in enumerate(hand):
            print(f"  {clr('Bold', str(i+1))}) {card.colored_str()}  {clr('Black', repr(card))}")
    print()

# ─────────────────────────────────────────────
#  CPU AI
# ─────────────────────────────────────────────

def cpu_choose_card(game):
    playable = game.playable_cards(game.cpu_hand)
    if not playable:
        return None, None

    # Priority: action > high-value numbers > others
    def priority(c):
        if "Wild Draw" in c.value:  return 0
        if "Wild" == c.value:       return 1
        if "Draw" in c.value:       return 2
        if "Skip" in c.value:       return 3
        if "Reverse" in c.value:    return 4
        if c.value.isdigit():       return 10 - int(c.value)
        return 5

    playable.sort(key=priority)
    chosen = playable[0]

    # Choose color for wild — pick most frequent color in hand
    chosen_color = None
    if chosen.is_wild():
        colors = game.get_colors()
        color_count = {c: 0 for c in colors}
        for card in game.cpu_hand:
            if card.color in color_count:
                color_count[card.color] += 1
        chosen_color = max(color_count, key=color_count.get)

    return chosen, chosen_color

# ─────────────────────────────────────────────
#  ACTION HANDLERS
# ─────────────────────────────────────────────

def handle_card_effect(game, card, next_player_hand, same_player_hand, game_log):
    """Apply the effect of a played card. Returns True if next player should be skipped."""
    skip_next = False

    if card.value == "Skip":
        game_log.append(clr("Yellow", "  ⊘ Skip! Next player loses their turn."))
        skip_next = True

    elif card.value == "Skip Everyone":
        game_log.append(clr("Pink", "  ⊗ Skip Everyone! Everyone else skips (2-player = 1 skip)."))
        skip_next = True  # In 2-player = skip opponent once

    elif card.value == "Reverse":
        game.direction *= -1
        game_log.append(clr("Teal", "  ↺ Reverse! Direction flipped."))
        # In 2-player reverse = skip
        skip_next = True

    elif card.value == "Draw Two":
        drawn = game.draw_card(next_player_hand, 2)
        game_log.append(clr("Red", f"  +2 Draw Two! Opponent draws 2 cards."))
        skip_next = True

    elif card.value == "Draw Five":
        drawn = game.draw_card(next_player_hand, 5)
        game_log.append(clr("Orange", f"  +5 Draw Five! Opponent draws 5 cards."))
        skip_next = True

    elif card.value == "Wild Draw Four":
        drawn = game.draw_card(next_player_hand, 4)
        game_log.append(clr("Wild", f"  ★+4 Wild Draw Four! Opponent draws 4 cards."))
        skip_next = True

    elif card.value == "Wild Draw Color":
        # Opponent draws until they get a card of declared color
        drawn_count = 0
        colors = game.get_colors()
        while True:
            d = game.draw_card(next_player_hand, 1)
            if not d:
                break
            drawn_count += 1
            if d[0].color == game.current_color:
                break
            if len(game.draw_pile) == 0:
                break
        game_log.append(clr("Purple", f"  ★+C Wild Draw Color! Opponent drew {drawn_count} card(s) until {game.current_color}."))
        skip_next = True

    elif card.value == "Wild":
        game_log.append(clr("Wild", f"  ★ Wild! Color changed to {game.current_color}."))

    # FLIP card
    if card.value in ("Flip",) or "Flip" in card.value:
        game.flip_side()
        game_log.append(clr("Bold", "  🔄 FLIP! The deck has been flipped!"))

    return skip_next

# ─────────────────────────────────────────────
#  PLAYER TURN
# ─────────────────────────────────────────────

def player_turn(game):
    game_log = []
    while True:
        show_header(game)
        show_top_card(game)
        show_hand(game.cpu_hand, "CPU HAND", hide=True)
        show_hand(game.player_hand, "YOUR HAND")

        for entry in game_log[-4:]:
            print(entry)

        playable = game.playable_cards(game.player_hand)
        if not playable:
            print(clr("Red", "  ✗ No playable cards! Drawing from pile..."))
            pause()
            drawn = game.draw_card(game.player_hand, 1)
            if drawn:
                card = drawn[0]
                print(clr("Yellow", f"  Drew: {card.colored_str()}"))
                if game.can_play(card):
                    ans = input(clr("Bold", f"  Play it? (y/n): ")).strip().lower()
                    if ans == "y":
                        color = None
                        if card.is_wild():
                            color = player_choose_color(game)
                        game.play_card(card, game.player_hand, color)
                        game_log.append(f"  You played: {card.colored_str()}")
                        skip = handle_card_effect(game, card, game.cpu_hand, game.player_hand, game_log)
                        return skip, game_log
                pause()
            return False, game_log

        print(clr("Bold", "  Choose a card to play (number), or 0 to draw:"))
        try:
            choice = int(input("  > ").strip())
        except ValueError:
            print(clr("Red", "  Invalid input."))
            pause()
            continue

        if choice == 0:
            drawn = game.draw_card(game.player_hand, 1)
            if drawn:
                print(clr("Yellow", f"  Drew: {drawn[0].colored_str()}"))
            pause()
            return False, game_log

        if choice < 1 or choice > len(game.player_hand):
            print(clr("Red", "  Invalid card number."))
            pause()
            continue

        card = game.player_hand[choice - 1]
        if not game.can_play(card):
            print(clr("Red", f"  Can't play {card.colored_str()} on {game.top_card().colored_str()}"))
            pause()
            continue

        # UNO call
        if len(game.player_hand) == 2:
            ans = input(clr("Yellow", "  🃏 You have 2 cards — say UNO? (y/n): ")).strip().lower()
            if ans != "y":
                print(clr("Red", "  Missed UNO! Draw 2 penalty cards."))
                game.draw_card(game.player_hand, 2)
                pause()

        chosen_color = None
        if card.is_wild():
            chosen_color = player_choose_color(game)

        game.play_card(card, game.player_hand, chosen_color)
        game_log.append(f"  You played: {card.colored_str()}")
        skip = handle_card_effect(game, card, game.cpu_hand, game.player_hand, game_log)
        return skip, game_log

def player_choose_color(game):
    colors = game.get_colors()
    print(clr("Bold", "\n  Choose a color:"))
    for i, c in enumerate(colors, 1):
        print(f"    {i}) {clr(c, c)}")
    while True:
        try:
            ch = int(input("  > ").strip())
            if 1 <= ch <= len(colors):
                return colors[ch - 1]
        except ValueError:
            pass
        print(clr("Red", "  Invalid choice."))

# ─────────────────────────────────────────────
#  CPU TURN
# ─────────────────────────────────────────────

def cpu_turn(game):
    game_log = []
    show_header(game)
    show_top_card(game)
    show_hand(game.cpu_hand, "CPU HAND", hide=True)
    show_hand(game.player_hand, "YOUR HAND")
    print(clr("Black", "  💻 CPU is thinking..."))
    time.sleep(1.2)

    card, chosen_color = cpu_choose_card(game)
    if card is None:
        drawn = game.draw_card(game.cpu_hand, 1)
        game_log.append(clr("Yellow", f"  CPU had no playable cards — drew 1."))
        # Try once more
        if drawn and game.can_play(drawn[0]):
            card = drawn[0]
            if card.is_wild():
                colors = game.get_colors()
                color_count = {c: 0 for c in colors}
                for c in game.cpu_hand:
                    if c.color in color_count:
                        color_count[c.color] += 1
                chosen_color = max(color_count, key=color_count.get)
            game.play_card(card, game.cpu_hand, chosen_color)
            game_log.append(f"  CPU played: {card.colored_str()}")
            skip = handle_card_effect(game, card, game.player_hand, game.cpu_hand, game_log)
            show_header(game)
            show_top_card(game)
            for entry in game_log:
                print(entry)
            pause()
            return skip, game_log
        show_header(game)
        show_top_card(game)
        for entry in game_log:
            print(entry)
        pause()
        return False, game_log

    if len(game.cpu_hand) == 2:
        game_log.append(clr("Yellow", "  💻 CPU says UNO! 🃏"))

    game.play_card(card, game.cpu_hand, chosen_color)
    game_log.append(f"  CPU played: {card.colored_str()}")
    if chosen_color:
        game_log.append(clr(chosen_color, f"  CPU chose color: {chosen_color}"))

    skip = handle_card_effect(game, card, game.player_hand, game.cpu_hand, game_log)

    show_header(game)
    show_top_card(game)
    show_hand(game.cpu_hand, "CPU HAND", hide=True)
    show_hand(game.player_hand, "YOUR HAND")
    for entry in game_log:
        print(entry)
    pause()
    return skip, game_log

# ─────────────────────────────────────────────
#  ROUND LOOP
# ─────────────────────────────────────────────

def play_round(game):
    game.setup_round()
    player_turn_flag = True  # True = player's turn

    while True:
        # Check win
        if not game.player_hand:
            return "player"
        if not game.cpu_hand:
            return "cpu"

        if player_turn_flag:
            skip, log = player_turn(game)
            if not game.player_hand:
                return "player"
            player_turn_flag = not skip  # if skip=True, player goes again (2-player reverse/skip)
            # Wait actually in 2-player: skip means CPU loses their turn = player goes again
            player_turn_flag = False if not skip else True
        else:
            skip, log = cpu_turn(game)
            if not game.cpu_hand:
                return "cpu"
            # skip=True means player loses their turn = cpu goes again
            player_turn_flag = True if not skip else False

# ─────────────────────────────────────────────
#  MAIN MENU & GAME LOOP
# ─────────────────────────────────────────────

def show_rules():
    clear()
    print(clr("Bold", LOGO))
    rules = """
UNO FLIP RULES SUMMARY
══════════════════════

LIGHT SIDE cards:
  Numbers 0-9 (Red, Green, Blue, Yellow)
  Skip        — next player loses a turn
  Reverse     — direction flips (in 2p = skip)
  Draw Two    — next player draws 2 & skips
  Wild        — change active color
  Wild Draw 4 — next draws 4 & skips; you pick color

DARK SIDE cards (harder!):
  Numbers 1-9 (Pink, Teal, Orange, Purple)
  Skip Everyone — all others skip (2p = 1 skip)
  Reverse       — direction flips
  Draw Five     — next player draws 5 & skips
  Wild          — change active color
  Wild Draw Color — next draws until matching color

FLIP card triggers the FLIP:
  All players' hands flip, deck flips!

WINNING A ROUND:
  First to empty hand wins. Loser(s) score
  the point value of remaining cards.
  First to 500 points LOSES!
  (Lowest score at end wins)
"""
    print(clr("Yellow", rules))
    pause()

def show_winner_screen(name):
    clear()
    art = r"""
   _  _  ___  ___   __    __  ___  _  _   _  
  ( \/ )/ __)(   ) (  )  (  )(  _)( \( ) ( ) 
   \  / \__ \ ) (  /__\   )(  ) _)  )  (  \_/ 
   (__) (___/(_) (_)(__) (__)(___) (_)\_) (_) 
"""
    print(clr("Yellow", art))
    slow_print(clr("Bold", f"\n  🏆  {name} wins the round!  🏆\n"), 0.05)
    pause()

def show_game_over(winner):
    clear()
    art = r"""
   ___   _   __  __  ____     _____  _  _  ____  ____ 
  / __) / \ (  \/  )( ___),  (  _  )( \/ )( ___)(  _ \
 ( (_-.(/ _)\)    (  )__)     )(_)(  \  /  )__)  )   /
  \___/(_/ \_)_/\_( (____)   (_____) (__) (____)(_)\_)
"""
    print(clr("Green", art))
    slow_print(clr("Bold", f"\n  🎉  {winner} wins the whole game!  🎉\n"), 0.05)
    pause("Press Enter to return to menu...")

def main():
    game = UnoFlipGame()

    while True:
        clear()
        print(clr("Bold", LOGO))
        print(clr("Yellow", "  ══════════════════════════════════════"))
        print(clr("Bold",   "    Welcome to UNO FLIP — Terminal Edition"))
        print(clr("Yellow", "  ══════════════════════════════════════\n"))
        print(clr("Bold", "  1) New Game"))
        print(clr("Bold", "  2) Rules"))
        print(clr("Bold", "  3) Quit"))
        print()
        choice = input("  > ").strip()

        if choice == "2":
            show_rules()
            continue
        elif choice == "3":
            slow_print(clr("Yellow", "\n  Thanks for playing UNO FLIP! Bye! 🃏\n"))
            sys.exit(0)
        elif choice != "1":
            continue

        game.scores = {"You": 0, "CPU": 0}
        game.round_num = 0
        TARGET = 500

        while True:
            winner = play_round(game)
            if winner == "player":
                show_winner_screen("You")
                pts = game.hand_score(game.cpu_hand)
                game.scores["CPU"] += pts
                slow_print(clr("Yellow", f"  CPU scores {pts} points (their remaining cards)."))
            else:
                show_winner_screen("CPU")
                pts = game.hand_score(game.player_hand)
                game.scores["You"] += pts
                slow_print(clr("Red", f"  You score {pts} points (your remaining cards)."))

            print(clr("Bold", f"\n  Scores — You: {game.scores['You']}  |  CPU: {game.scores['CPU']}"))
            print(clr("Black", f"  (First to {TARGET} points loses!)"))

            loser = None
            if game.scores["You"] >= TARGET:
                loser = "You"
            elif game.scores["CPU"] >= TARGET:
                loser = "CPU"

            if loser:
                final_winner = "CPU" if loser == "You" else "You"
                show_game_over(final_winner)
                break

            pause("Press Enter to play next round...")

if __name__ == "__main__":
    main()