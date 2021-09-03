# ICS3U

This is a repo of free programming materials for Ontario's ICS3U course.
It was created by Luke Sawczak based on Daniel Zingaro's Learn to Code by Solving Problems, for which Luke also served as technical reviewer.

The starting point is `catalogue.md`, which contains links to all the other components. Those components are:

1. **Jupyter Notebooks** designed for use in Google Colab. These follow the order of the concepts in Dr. Zingaro's book, with slight adjustments to align it with the ICS3U curriculum or adapt to teaching.
<br><br>The notebooks are interactive and contain numerous mini-exercises to scaffold the learning. They can be used for independent asynchronous learning, or can be taught sychronously with live sharing of progress on the exercises. Each notebook is designed to take an average of 2 hours of instructional time (less for the initial notebooks), but they are modular enough to allow pausing and resuming as needed.
<br><br>It is important to note that the exercises in the notebooks are *not* intended to be your primary homework tasks. They typically have a narrowly defined range of solutions, so answers can be shared or easily researched. They are the *action* part of the lesson. For *consolidation*, when I teach from these, I assign custom exercises that are more creative and personalized. Creating a library of such exercises is an item in the *TODO* section below.
<br><br>There is also an overall "Programming Notebook". This serves as the students' introduction to the technology, and serves as a unit-long notebook for students to define terms and provide examples of how to use the concepts. I check in with the progress of this notebook multiple times throughout the unit as a way to individually track what students have learned, and make completion of it a significant mark at the end.
<br><br>If you're not familiar with Jupyter or Google Colab, read `jupyter.md` to get it set up for your class.

2. **Documentation exercises.** These are *minds-on* or *check-in* tasks to review the previous day. Each is a small block of mystery code that the students must analyze and document (this works well in pairs). My solutions are provided, though naturally this type of exercise could admit of multiple names and descriptions.
<br><br>There are currently not very many of these, and while I have numbered them in an order that loosely corresponds to the Jupyter notebooks in terms of the concepts covered, filling out the roster and more tightly coupling them to the notebooks is an item in the *TODO* section below.

3. **DMOJ problems.** These are also review / minds-on tasks. They are standard coding problems closely aligned with the concepts and drawn from the curated list in Zingaro's book. One advantage is that they are easy to try independently and get instant automated feedback on; one disadvantage is that they have more narrowly defined solutions and often are Googleable, so I don't recommend them as homework. Note that in my experience, Grade 11 students find these very challenging without guidance.
<br><br>From the list in `catalogue.md`, I've bolded a few. These are the ones I found most useful and doable in class time. I've provided a solution for each of these, and in some cases, starter code ("stubs") for problems that are too hard for students to solve in a reasonable time.

4. **Tasks.** These are the creative exercises mentioned above. The library is far from complete at this point and mostly consists of notes one could provide to students in writing to get started.

## ICS4U

There is a folder called `ics4u_supplement`. The notebooks in here are *not* intended to be a full ICS4U programming or software unit. One year I had a student whose mastery of ICS3U concepts was so strong that I determined the gap to close to grant an ICS4U credit instead, and these notebooks are the result of that. The student was able to work highly independently to complete these. Hence, I include them as jumping-off points, rather than a standalone solution.

## TODO

* Create a list of creative homework exercises / mini-projects for consolidation of the concepts. The exercises in the notebooks are too narrowly defined to serve this purpose. Good exercises are designed to allow everyone to solve it in their own way with their own content. Some of the ones I've done in the past are below:
  * Death Clock: take input from the user and output their life expectancy.
  * Death Clock Plus: add conditional questions to the Death Clock, e.g. ask about pregnancy depending on response to gender.
  * Covid Simulator Plus: based on starter code running on viral  spread throughout a population over a given number of days, add a new feature of your choosing (a list of suggestions is provided).
  * Sentence Randomizer: Create lists of words or short phrases. Based on variables from the environment or user input, output a "mad libs" style sentence.
  * Text Analysis: Given textual user input, calculate and output various statistics of your choosing (a list of suggestions is provided).
  * Wage Calculator: Create a program that takes various inputs from the user and outputs their expected wages for a week. Invent a job so as to have unique tasks done that factor into the user's wages.
  * Menu of Programs: Create various subprograms. Present the user with a menu of the ones they would like to run, with an inner input to be sent (as an argument to the subprogram function).
  * Class List: Create a dictionary of classmates' names to attributes. Manipulate/invert/output personality data ... [Not very good; actual programming operation is too narrowly defined.]
* Make more documentation exercises, preferably at least one per concept/notebook.
* Create ways to differentiate the course-long Programming Notebook a little more. Currently, I look for plagiarism only by identifying duplicate wording or examples between students, but it would be nice for it to have more scope for individual creativity in the note-taking.

## License

This project is licensed under GNU GPL v3.0. The full license is located in `LICENSE` and is summarized below (courtesy of [choosealicense.com](https://choosealicense.com/licenses/gpl-3.0/)).

In short, you may use, modify, and distribute it, as long as you do not obscure the source or change the licence, and understanding that there is no warranty or liability provided for its use. You may branch for your own use or submit pull requests (though I make no promises of timelines to consider these!).

* Permissions
  * Commercial use
  * Distribution
  * Modification
  * Patent use
  * Private use
* Conditions
  * Disclose source
  * License and copyright notice
  * Same license
  * State changes
* Limitations
  * Liability
  * Warranty

## Feedback & Questions

Write to [luke.sawczak@mail.utoronto.ca](mailto:luke.sawczak@mail.utoronto.ca).
