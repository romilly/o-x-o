# Project journal for o-x-o

## Thursday 10 December 2020

I am migrating the old private MENACE notebooks to this public repository and preparing to publish them as a
[jupyter{book}](https://romilly.github.io/o-x-o/an-introduction.html).

## Saturday 12 December 2020

The book is under way - incomplete but readable.

Today I will
1. ~~Tidy up the Appendix and README~~
1. Finish the chapter on canonical board representations.
1. Start the next chapter.

## Thursday 17 December 2020

I've been lax in maintaining the journal, but I have done a lot of work each day.

Today I need to round out, improve and finish Chapter 6.
I think Ch 7 will get us to the point where MENACE can play against a random or human opponent.

The plan is for Ch 8 to cover a version that maintains history across sessions in an APL file,
and Ch 9 to plot performance.

Note for tomorrow: the RI video demo of MENACE is at 37:30 in
https://www.rigb.org/christmas-lectures/watch/2019/secrets-and-lies/how-to-bend-the-rules

## Friday 18 December 2020

I updated the README, and added a link from the introduction to Appendix A.

I'm going to explore my game player in chapter 7, but I won't add it to the book toc yet.

## Saturday 19 December 2020

I can't yet implement the human player in a notebook, as ⍞ is not supported in the dyalog-jupyter kernel.

I have implemented it, in part, in `notebook7a.dws`.

For now, I will concentrate on
1. The random player (a quick win, or more accurately a quick *loss*).
1. The updating menace player.

That would be enough for me to start training a MENACE version.


## Sunday 20 December 2020

I'll do the random player first, just to prove the game_runner design.

Also tweak player to return its type if given an argument of `⍬`.

## Tuesday 22 December 2020

Lots done yesterday, though I was very tired.

`game_runner` now working with a `random_player`,and I have started chapter 8.

I've started a ten-minute guide to RIDE as this will be needed if anyone wants to run a `human_player`.

## Thursday 24 December 2020

Good progress yesterday. Ch 7 now uses Namespaces, as suggested by Morten.

Today I will work on Ch 8, change it to use Namespaces, and actually update the bead counts.

Hopefully I will then see some learning :)

For now, I will
1. plot using LibreOffice, and
1. keep a trained config in a special ws.
   
Later I will plot using SharpPlot and use shared files to keep trained config(s).


## Saturday 26 December 2020

Just discovered ]dinput, ]plot and the ability to define ∇fns in the dyalog notebooks thanks to APL Orchard help.

Yay!


## Sunday 27 December 2020

Got a very helpful reply from RP this morning. Will look at user input in the new year.

Today focus on
1. Appendix B
1. `menace_player`and
1. `]plot`.

## Thursday 31 December 2020

I've done a lot but not been very diligent in keeping the journal up-to-date.

I discovered yesterday that TryAPL now supports notebooks

`https://tryapl.org/?notebook=url_of_next_in_series`

` ?clear=no`


## Monday 04 January 2021

Mega progress.

Today:
1. Finish the restructuring of the material about operators.
1. Get the simple_menace_player working
1. Plot the learning

## Monday 11 January 2021

Back after some work on this, and a lot on a planned blog post and on Hopfield related work.

## Thursday 14 January 2021

The fastest way to get the menace player working will be to use the debugger, so I will ]link and work in that.

Later: Morten has got the latest ]link working for me.

## Friday 15 January 2021

Started by doing ` ]link.Create # apl` in a clear ws, and I have all the code!

## Wednesday 20 January 2021

Back to work after nibbling at this for several days.

Workflow:

1. Load clear ws in OXO RIDE environment
1. ]link
1. Code, adding stuff to link as necessary
1. Use diffs, grep to see what notebooks need changing.

```apl
]LINK.create # apl
config ← good init 20 
config ← menace_player game_runner random_player⊢config
config.menace_moves
```


### Simplification!

Oh my, I just realised that I *don't* need to keep track of who made a bad move. A bad move is a bad move!


## Thursday 21 January 2021

So close to getting the menace player working. All I need to do is
1. Finish the code that decides if the outcome is a loss (for `×`), a draw or a win.
   1. Write a test script
   1. Get the  test working
1. Use that and ⌷-indexing to update the bead counts
1. Plot the results of some games

## Friday 22 January 2021

Some testing works. More to do!

