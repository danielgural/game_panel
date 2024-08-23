import fiftyone as fo
import fiftyone.operators as foo
import fiftyone.operators.types as types


class DOOM(foo.Panel):
    @property
    def config(self):
        return foo.PanelConfig(
            name="DOOM",
            label="Play Doom!",
            icon="gamepad"
        )

    def on_load(self, ctx):
        pass

    def render(self, ctx):
        panel = types.Object()
        panel.define_property(
            "frame",
            types.String(),
            view=types.HeaderView(
                label="x",
                componentsProps={
                    "label": {
                        "component": "iframe",
                        "src": "https://thedoggybrad.github.io/doom_on_js-dos/",
                        "width":"700px",
                        "height":"700px"
                    }
                },
            ),
        )
        return types.Property(panel, view=types.GridView())
    
def register(p):
    p.register(DOOM)