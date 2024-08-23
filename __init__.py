import fiftyone as fo
import fiftyone.operators as foo
import fiftyone.operators.types as types

GAMES = [
    "CHESS",
    "DOOM",
    "MINESWEEPER",
    "PAC-MAN",
    "TETRIS",
]

GAMES_URL = [
    "https://js-dos.com/games/chess.exe.html",
    "https://js-dos.com/games/doom.exe.html",
    "https://www.minesweeperforfree.com/",
    "https://js-dos.com/games/pac-man.exe.html",
    "https://js-dos.com/games/tetris.com.html"
]

class Game_Panel(foo.Panel):
    @property
    def config(self):
        return foo.PanelConfig(
            name="Game_Panel",
            label="Play Games!",
            icon="gamepad"
        )

    def on_load(self, ctx):
        pass

    def render(self, ctx):
        panel = types.Object()

        stack = panel.v_stack("my_stack", align_x="center", align_y="center", gap=2)

        stack.md(
            """
            ### Take a Break & Play a Game!

            Choose between Chess, DOOM, Minesweeper, PAC-MAN, or Tertris!
        """,
            name="md1",
        )


        menu = stack.menu("menu", variant="square", width=100, align_x="center", align_y="center")
        actions = menu.btn_group("actions")

        
        actions.enum(
            "game",
            label="Select game:",
            values=GAMES,
            view=types.View(space=3),
            on_change=self.on_change_config,
        )
        if ctx.panel.get_state("my_stack") is not None:
            game = ctx.panel.get_state("my_stack.menu.actions.game")
            game_url = GAMES_URL[GAMES.index(game)]
            
            if game != "MINESWEEPER":
                stack.define_property(
                    "frame",
                    types.String(),
                    view=types.HeaderView(
                        label="x",
                        componentsProps={
                            "headingsContainer": {"overflow": "hidden"},
                            "label": {
                                "component": "iframe",
                                "src": game_url,
                                "width": "700px",
                                "height": "700px",
                                "border": "none",
                                "style": {
                                    "margin-top": "-60px", 
                                    "margin-bottom": "-279px",
                                    "margin-left": "-35px",
                                    "margin-right": "-22px",
                                },
                            },
                        },
                    ),
                )
            elif game == "MINESWEEPER":
                stack.define_property(
                    "frame",
                    types.String(),
                    view=types.HeaderView(
                        label="x",
                        componentsProps={
                            "headingsContainer": {"overflow": "hidden"},
                            "label": {
                                "component": "iframe",
                                "src": game_url,
                                "width": "700px",
                                "height": "700px",
                                "border": "none",
                                "style": {
                                    "margin-top": "-60px", 
                                    "margin-bottom": "-100px",

                                },
                            },
                        },
                    ),
                )
        return types.Property(panel, view=types.GridView())
    
    def on_change_config(self, ctx):
        pass
    
def register(p):
    p.register(Game_Panel)