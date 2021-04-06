# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows in current stack pane
    Key([mod], "o", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "i", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "o", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "i", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    #Key([mod], "space", lazy.layout.next(),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "q", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    #Para el rofi
    Key([mod], "u", lazy.spawn("rofi -show run")),
    Key([mod, 'shift'], "u", lazy.spawn("rofi -show")),

    #Para el Ranger
    Key([mod], "f", lazy.spawn(terminal+" -e env EDITOR=nano ranger")),

    #Para el navegador
    Key([mod], "b", lazy.spawn("firefox")),

    # Volumen
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),

    #Para el brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +3%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 3%-")),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in [
    "Web", "Dev", "Term"
]]

keys_group = "123"

for i, group in enumerate(groups):
    actual_key = keys_group[i]
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
layout_theme = {"border_width": 3,
                "margin": 1,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }


layouts = [
    layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Matrix(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(),
]


############################  BAR ##########################

background_color = '#07303e'
etiqueta_uno = '#25d6dc' #Azul
etiqueta_dos = '#e9105f'

widget_defaults = dict(
    font='Ubuntu Bold',
    fontsize=12,
    padding=3,
    background=background_color
)
extension_defaults = widget_defaults.copy()


widget_trian_NR = widget.TextBox(
        text="♦", 
        width=20,
        background=background_color,
        foreground = etiqueta_dos,
        padding = 0,
        fontsize = 40)

widget_trian_RA = widget.TextBox(
        text="♦", 
        width=20,
        background=etiqueta_dos,
        foreground = etiqueta_uno,
        padding = 0,
        fontsize = 40)

widget_trian_AR = widget.TextBox(
        text="♦", 
        width=20,
        background=etiqueta_uno,
        foreground = etiqueta_dos,
        padding = 0,
        fontsize = 40)


widget_pad_R = widget.Sep(
        linewidth = 0,
        padding = 10,
        foreground = '#FFFFFF',
        background = etiqueta_dos
        )

widget_pad_A = widget.Sep(
        linewidth = 0,
        padding = 10,
        foreground = '#FFFFFF',
        background = etiqueta_uno
        )



screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout( 
                    padding = 5),
                widget.GroupBox(
                    margin_y = 3,
                    margin_x = 5,
                    padding_y = 5,
                    padding_x = 3,
                    borderwidth = 3,
                    active = etiqueta_uno,
                    inactive = etiqueta_dos
                ),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget_trian_NR,
                widget_pad_R,
                widget.TextBox("PlugInRichi", 
                    name="propietario",
                    background=etiqueta_dos),
                widget_trian_RA,
                widget_pad_A,
                widget.Clock(
                    background=etiqueta_uno,
                    format='%A %d   ⌚ %I:%M'
                    ),
                widget_trian_AR,
                widget_pad_R,
                widget.Systray(
                    background = etiqueta_dos,
                    padding = 5
                ),
                widget_trian_RA,
                widget.QuickExit(
                    background=etiqueta_uno,
                    font='Ubuntu',
                    fontsize=20,
                    padding = 10,
                    default_text = '  ☢  ',
                    countdown_format = ' {} ⌛'
                ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
