import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib, Gio
import workbench

demo: Adw.StatusPage = workbench.builder.get_object("GrimoireWindow")
story_details_dialog = workbench.builder.get_object("story_details")
character_dialog = workbench.builder.get_object("character_dialog")
edit_button = workbench.builder.get_object("edit_button")

demo_group = Gio.SimpleActionGroup()
demo.insert_action_group("demo", demo_group)

story_details_action = Gio.SimpleAction(name="story_details")

story_details_action.connect(
    "activate", lambda action, _: story_details_dialog.present(demo)
)

demo_group.add_action(story_details_action)

edit_button.connect("clicked", lambda x: character_dialog.present(demo))


@Gtk.Template.Callback()
def open_character_dialog():
    character_dialog.present(demo)
