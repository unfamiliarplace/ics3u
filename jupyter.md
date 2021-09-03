# Jupyter

A [Jupyter Notebook](https://jupyter.org/) is a document that combines formatted text (in the form of [Markdown](https://en.wikipedia.org/wiki/Markdown)) with blocks of code. These can be run independently, though in one session they will share memory between each other.

Prior to using Jupyter Notebooks, I just wrote `.py` scripts on the fly and used comments for my text. While there's a time and place for `.py` files, this proved a very inefficient teaching tool: when all the code lives in one script, you have to comment out blocks you don't want to run, or separate them into many files. Also, plaintext is not a great navigational aid. So students ended up having a very hard time recreating the exercises we did in class, even when I provided my `.py` files.

With Jupyter, I can now have a flow between text and code, text and code, with blocks for students to run and blocks for students to edit and try for themselves. It's really quite lovely, and student feedback has been very positive. It turns out that, just as easily as I can teach through a notebook, a student can take it and read through it and re-run all the code themselves at home, whenever they want. It's very versatile.

## Setting up

I envision two easy ways of getting this to work in a classroom setting.

### Google Colab

This is the form I tend to use, simply because any browser-based platform tends to be highly accessible to students, and they all use the G Suite extensively anyway.

1. Upload all the `.ipynb` files under [materials/notebooks](materials/notebooks) to a Google Drive folder. Set the whole folder to shared or, if you prefer to roll things out at a more controlled pace, share links one by one as you teach them.

2. Exactly once, you — and your students — need to add the Google Colaboratory app to your Drive ecosystem. Open any Drive folder; click `New` → `More` → `Connect other apps` → `Google Colaboratory`. Once this step has been done, all notebooks should open fine in Google Colab.<sup>*</sup>

3. When you begin using a notebook, each student must save a copy to their Drive. This is very important! Google Colab's UI allows them to edit the text and code and run code blocks, but *unless they make a copy, these changes won't save*.

<sub><sup>*</sup> I have sometimes encountered a bug in Drive where notebooks created in the Drive UI are recognized as Google Colab files, but notebooks uploaded to your Drive are not. If this happens, you may have to do `Open with` → `Google Colaboratory` on the uploaded files. They still work fine.</sub>

## IDE

The alternative is to use the notebooks in an IDE setting, such as [VSCode](https://code.visualstudio.com/) with the Python and Jupyter extensions installed. In this case, you can simply distribute the `.ipnyb` files under [materials/notebooks](materials/notebooks) directly to the students. 

This has the disadvantage of needing more setup, but since you are likely asking students to install it anyway, it may be well worth it. Also, execution tends to be faster since it uses your local machine's resources instead of pinging a Google server, and you don't need to worry about ensuring they save a copy in Drive before editing.

It does also make it less convenient for students to share their edited notebooks back with you, considering how much high school students love Google Drive links — but in practice the only one that needs to be shared with you is [My Programming Handbook.ipnyb](materials/notebooks/My%20Programming%20Handbook.ipnyb). The others are not intended to be marked, just done as part of the *action* phase of the lesson.
