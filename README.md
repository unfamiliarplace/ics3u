# ICS3U

This is a repo of materials for the programming unit of [Ontario's ICS3U course](http://www.edu.gov.on.ca/eng/curriculum/secondary/computer10to12_2008.pdf#page=41).
I created it based on Daniel Zingaro's [Learn to Code by Solving Problems](https://www.penguinrandomhouse.com/books/670339/learn-to-code-by-solving-problems-by-daniel-zingaro/), for which I also served as technical reviewer. While these materials primarily serve the teacher of ICS3U, the principles of programming taught here through Python are universal. I've released them freely for anyone to benefit from who wants to learn to code.

— Luke Sawczak, 2021-09-03

## Navigating the materials

The starting point is [catalogue.md](catalogue.md), which contains links to all the other components. Those components are:

1. **Jupyter Notebooks** designed for use in Google Colab. These follow the order of the concepts in Dr. Zingaro's book, with slight adjustments to align it with the ICS3U curriculum or adapt to teaching.
<br><br>The notebooks are interactive and contain numerous mini-exercises to scaffold the learning. They can be used for independent asynchronous learning, or can be taught sychronously with live sharing of progress on the exercises. Each notebook is designed to take an average of 2 hours of instructional time (less for the initial notebooks), but they are modular enough to allow pausing and resuming as needed.
<br><br>It is important to note that the exercises in the notebooks are *not* intended to be your primary homework tasks. They typically have a narrowly defined range of solutions, so answers can be shared or easily researched. They are the *action* part of the lesson. For *consolidation*, when I teach from these, I assign custom exercises that are more creative and personalized. Creating a library of such exercises is an item in the [TODO](#todo) section below.
<br><br>There is also an overall "My Programming Handbook". This serves as the students' introduction to the Jupyter technology, and is to be used as a unit-long notebook for students to define terms and provide examples of how to use the concepts, *as they learn them*. I check in with the progress of this notebook multiple times throughout the unit as a way to individually track what students have learned, and make completion of it a significant mark at the end.
<br><br>If you're not familiar with Jupyter or Google Colab, read [jupyter.md](jupyter.md) to get it set up for your class.

2. **Documentation exercises.** These are *minds-on* or *check-in* tasks to review the previous day. Each is a small block of mystery code that the students must analyze and document (this works well in pairs). My solutions are provided, though naturally this type of exercise could admit of multiple names and descriptions.
<br><br>There are currently not very many of these, and while I have numbered them in an order that loosely corresponds to the Jupyter notebooks in terms of the concepts covered, filling out the roster and more tightly coupling them to the notebooks is an item in the [TODO](#todo) section below. Also, note that in the catalogue they are not currently identified by concept.

3. **DMOJ problems.** These are also review / minds-on tasks. They are standard coding problems closely aligned with the concepts and drawn from the curated list in Zingaro's book. One advantage is that they are easy to try independently and get instant automated feedback on; one disadvantage is that they have more narrowly defined solutions and often are Googleable, so I don't recommend them as homework. Note that in my experience, Grade 11 students find these very challenging without guidance.
<br><br>From the complete list in [catalogue.md](catalogue.md), I've bolded a subset. These are the ones I found most useful and doable for the level and time that I was targeting. I've provided a solution for each of these, and in some cases, starter code ("stubs") for problems that are too hard for students to solve in a reasonable time.
<br><br>Students will need to create a DMOJ account to participate. Also, some problems listed may be from [acm.timus.ru](https://acm.timus.ru/) instead and require a separate account, but none of the ones I've used in practice have been from Timus.

4. **Tasks.** These are the creative exercises mentioned above. The library is far from complete at this point and mostly consists of notes one could provide to students in writing to get started.

## ICS4U

There is a folder called [ics4u_supplement](materials/notebooks/ics4u_supplement). The notebooks in here are *not* intended to be a full ICS4U programming or software unit. One semester I had a student whose mastery of ICS3U concepts was so strong that I determined the gap to close to grant an ICS4U credit instead, and these notebooks are the result of that. The student was able to work highly independently to complete these. Hence, I include them here as jumping-off points, rather than a standalone solution.

## TODO

* Create a list of creative homework exercises / mini-projects for consolidation of the concepts. The exercises in the notebooks are too narrowly defined to serve this purpose. Good exercises are designed to allow everyone to solve it in their own way with their own content. There is a small but highly underdeveloped list in the folder at present.
* Make more documentation exercises, preferably at least one per concept/notebook. Identify the existing ones by concept instead of number.
* Find ways to differentiate My Programming Handbook more. Currently, I look for plagiarism only by identifying definitions and examples that are identical between students, but it would be good for it to have more scope for individual creativity in the note-taking.
* The notebooks on files currently rely on downloading some JSON data via [npoint.io](https://www.npoint.io/). This data is personalized to a class I once had, and I update it each time. A better solution would be nice.
* I may at some point integrate the rest of the course into this repo. Currently it only holds the programming unit, but I've also created materials for the computer basics, software development, and topics/careers units, plus miscellaneous projects, all of which is probably useful to other ICS3U teachers too.

## License

This project is licensed under GNU GPL v3.0. The full license is located in [LICENSE](LICENSE) and is summarized below (courtesy of [choosealicense.com](https://choosealicense.com/licenses/gpl-3.0/)).

In short, you may use, modify, and distribute it, as long as you do not obscure the source or change the licence, and understanding that I provide no warranty or liability for its use. 

You may clone and/or branch for your own use as much as you wish, or submit pull requests if you feel an update should be centralized. (I'm excited about this possibility but make no promises of timelines to consider pull requests.)

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

Write to [luke@sawczak.com](luke@sawczak.com).
