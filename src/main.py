# main.py
#
# Copyright 2019 Avi Wadhwa
# Copyright 2024 Earldridge Jazzed Pineda
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi
gi.require_version('Handy', '1')
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from .window import OrganizerWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='org.librehunt.Organizer',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = OrganizerWindow(application=self)
        win.present()

def main(version):
    app = Application()
    return app.run(sys.argv)
