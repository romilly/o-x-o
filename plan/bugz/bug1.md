# Bug saving linked, edited char matrix

```
]link.Create # bugz
Linked: # ←→ /home/romilly/git/active/o-x-o/menace/bugz
     )ed -atest
     ]add atest
Added: #.atest
      ⍝ change some data and save
     )ed -atest 
Link Warning: ⎕SE.Link.Notify: changed /home/romilly/git/active/o-x-o/menace/bu
      gz/atest.apla: invalid name defined by file: /home/romilly/git/active/o-x
      -o/menace/bugz/atest.apla
```

And `atest.apla` contains
```
1 ≡ #.status 2 1 1 2 1 2 1 1 2
2 ≡ #.status 2 1 1 2 1 2 2 0 2
```
