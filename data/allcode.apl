3*9
3 3⍴'....×....'
⎕io ← 0
3 3⍴'.×○'[0 0 0 0 1 0 0 0 0]
show ← {3 3⍴'.×○'[⍵]}
show 0 0 0 0 1 0 0 0 0
boards ← ⍳19683
boards[0 1 2 3 4 5]
6↑boards
encoded ← (9⍴3)⊤boards
⍴encoded
9 6↑encoded
⍉9 6↑encoded
encode ← {⍉(9⍴3)⊤⍵} ⍝ integer(s) to board vector/matrix
encode ⍳6
decode ← {3⊥⍉⍵}
decode encode ⍳6
show encode ⍳6
show ← {3 3⍴⍤ 1 ⊢'.×○'[⍵]}
show encode ⍳6
⍴show encode ⍳6
⊂⍤2 show encode ⍳6
list ← {⊂⍤2 show ⍵}
list encode ⍳6
⎕io ← 0
⊢ start ← 3 3⍴⍳9
⌽start
show board1 ← 1 1 0 0 2 2 0 1 0
show board1[2 1 0 5 4 3 8 7 6]
,⌽start
m ← {⍵[2 1 0 5 4 3 8 7 6]} ⍝ mirror reflection
r ← {⍵[6 3 0 7 4 1 8 5 2]} ⍝ rotation
show ¨ board1 (m board1) (r board1)
i ← ⍳9
r90 ← r i ⍝ one rotation by 90 degrees
r180 ← r r90 ⍝ two consecutive rotations - 180 degrees
r270 ← r r180 ⍝ three - 270 degrees
mi ← m ⍳9
mr90 ← m r90
mr180 ← m r180
mr270 ← m r270
+symmetries ← ↑ i r90 r180 r270 mi mr90 mr180 mr270
list board1[symmetries]
⎕io ← 0
 ⊢ symmetric ← 3 3⍴'....×....'
see←{{,'.×○'⍳⍵}⍤2⊣⍵}
⊢ sym ← see symmetric
sym[symmetries]
∪sym[symmetries] ⍝ the unique version
⊢ asymmetric ← 3 3⍴'.×.×○×...'
+less ← see asymmetric
less[symmetries]
∪less[symmetries]
⊂⍤2 show ∪less[symmetries]
show board1
⊂⍤2 show ∪board1[symmetries]
canonical ← { ⌊⌿ decode ⍵[symmetries]}
show encode canonical sym
show encode canonical less
show encode canonical board1
all ← canonical encode ⍳3*9
(⊂0 3 2)⌷7 8 9 10 20
ild ← {(⊂⍺) ⌷[¯1+⍴⍴⍵]⍵} ⍝ index last dimension
canonical ← {⌊⌿decode symmetries ild ⍵}
⍴ canonical encode ⍳3*9
⍴ ∪ canonical encode ⍳3*9
⊢ samples ← encode 0 1 9 10 11 18 20 19682
v ← 0 0 0 0 0 0 1 0 2
1 2 ∘.= v
+/1 2 ∘.= v
-/+/1 2 ∘.= v
cd ← {-/+/1 2 ∘.=⍵}
cd 0 0 0 0 0 0 1 0 1
1 2 0 5 1 2 ∊ 0 1
(cd 0 0 0 0 0 0 1 0 1) ∊ 0 1 ⍝ not a possible position
(cd 0 0 0 0 0 0 1 2 1) ∊ 0 1 ⍝ a possible position
0 1 ∊⍨ cd 0 0 0 0 0 0 1 2 1
ok ← {0 1 ∊⍨ cd ⍵}
ok 0 0 0 0 0 0 1 2 1
ok 0 0 0 0 0 0 1 0 1
ok samples
cd ← {-⌿+/1 2 ∘.=⍵}
ok samples
list samples⌿⍨ok samples
⍴uc ← encode ∪ canonical encode ⍳3*9
⍴ucp ← uc⌿⍨ok uc
list 19↑ucp
⍴mn ← +/ucp≠0
mnp ← ⍋mn
↑(list  19↑ucp[mnp;]) (19↑mn[mnp])
⎕io ← 0
3 3⍴⍳9
i ← 3 3⍴⍳9
⊢wpi ← {rows ← ⍵ ⋄ cols ← ⍉⍵ ⋄ diagonals ← 2 3⍴↑(0 0⍉⍵) (0 0⍉⌽⍵) ⋄ ⊃⍪/rows cols diagonals} 3 3⍴⍳9
wf ← {∨⌿∨/^/1 2∘.=wpi ild ⍵} ⍝ is this a win?
wf 1 1 1 0 2 2 0 0 0
wf 2 0 1 2 0 1 2 1 0
wf 1 2 1 0 1 0 2 2 0
+/wf ucp
wp ← {⍵⌿⍨wf ⍵}
list 19↑wp ucp
