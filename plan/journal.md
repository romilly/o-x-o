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



