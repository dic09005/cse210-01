
"""
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210> git clone https://github.com/dic09005/cse210-01.git                                 Cloning into 'cse210-01'...    
Cloning into 'cse210-01'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210> cd cse210-01
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210\cse210-01> git add README.md
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210\cse210-01> git add demo.py
fatal: pathspec 'demo.py' did not match any files
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210\cse210-01> git add README.md
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210\cse210-01> git add demo.py
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210\cse210-01> git commit -m "first git commit week 02"
[main c3b1310] first git commit week 02
 2 files changed, 2 deletions(-)
 delete mode 100644 README.md
 create mode 100644 demo.py
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210\cse210-01> git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Writing objects: 100% (3/3), 239 bytes | 239.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/dic09005/cse210-01.git
   63ced96..c3b1310  main -> main
PS C:\Users\Robin\Desktop\school2022\Fall 2022\cse210\cse210-01>
"""

# Code to clear screen
import os
os.system('cls' if os.name == 'nt' else 'clear')

