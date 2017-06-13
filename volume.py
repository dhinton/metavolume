import praw
from Tkinter import Toplevel, Label, Entry, Button, Tk
from subprocess import call


class VolumeDialog:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        Label(
            top,
            text="Submit Reddit post id. Volume will be set to ups%100").pack()
        self.e = Entry(top)
        self.e.pack(padx=5)
        b = Button(top, text="Submit", command=self.ok)
        b.pack(pady=5)

    def ok(self):

        post_id = self.e.get()
        r = praw.Reddit('stupid_volume')
        submission = r.submission('%s' % post_id)
        ups = submission.ups % 100
        call(['pulseaudio-ctl', 'set', '%s' % ups])

root = Tk()
root.update()
d = VolumeDialog(root)
root.wait_window(d.top)
