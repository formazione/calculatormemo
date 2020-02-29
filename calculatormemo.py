import tkinter as tk
import os
from datetime import datetime
import argparse, sys, markdown


TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="referrer" content="no-referrer" />
    <meta name="referrer" content="unsafe-url" />
    <meta name="referrer" content="origin" />
    <meta name="referrer" content="no-referrer-when-downgrade" />
    <meta name="referrer" content="origin-when-cross-origin" />

    <title>Page Title</title>

    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            font-family: Helvetica,Arial,sans-serif;
        }
        code, pre {
            font-family: monospace;
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""


def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    md = args.mdfile.read()
    extensions = ['extra', 'smarty']
    html = markdown.markdown(md, extensions=extensions, output_format='html5')
    doc = TEMPLATE.replace('{{content}}', html);
    args.out.write(doc)
    with open("file.html", "w") as file:
        file.write(doc)
    os.startfile("file.html")
# This class inherit from Frame
class App(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.option_add("*Font", "arial 20 bold")
        self.pack(expand=tk.YES, fill=tk.BOTH)
        self.master.title("Calculator ctrl+s=save txt ctrl+b=save md")
        self.master.tk.call('wm', 'iconphoto', self.master._w, tk.PhotoImage(file='calculator.png'))
        # the widgets: display, clear button...
        self._display()
        self.list_of_ops()

    def _display(self):
        display = tk.StringVar()
        entry = tk.Entry(
            self,
            relief=tk.FLAT,
            textvariable=display,
            justify='right',
            bd=15,
            bg='orange')
        entry.pack(side=tk.TOP)
        entry.focus()
        entry.bind("<Return>", lambda x: self.calc(display))
        entry.bind("<Escape>", lambda x: display.set(""))
        self.master.bind("<Control-s>", self.save)
        self.master.bind("<Control-b>", self.start)

    def getname(self):
        d = datetime.today()
        d = str(d).split(":")
        d = "".join(d)
        d = d.replace("-","_")
        d = d.replace(" ","_")
        d = d.replace(".","_")
        name = "memo" + d + ".txt"
        return name

    def save(self, event):
        "Save the memo about the operations"
        name = self.getname()
        with open(name, "w", encoding="utf-8") as file:
            file.write(self.text.get("0.0", tk.END))
        os.startfile(name)

    def start(self, event):
        name = self.getname()
        testo = self.text.get("0.0", tk.END)
        with open("file_1.md", "w") as file:
            file.write(testo)
        sys.exit(main(["file_1.md"]))

    def list_of_ops(self):
        self.text = tk.Text(self, height=10, width=30)
        self.text.pack(fill="both", expand=1)


    def calc(self, display):
        try:
            ris = eval(display.get())
            if str(display.get()) == str(ris):
                display.set("")
            else:
                self.text.insert(tk.END, display.get() + "=" + str(ris) + "\n")
                display.set(ris)
        except NameError as e:
            display.set("ERR: press ESC")


if __name__ == '__main__':
    a = App()
    a.mainloop()
