#!/bin/bash
# Q1
git branch

# Q2
git log -n 1 --format=%H

# Q3
git checkout 4177daab2f54bdb20c71f623296a8bb32616fd12

# Q4
find . -name '*.java' | xargs wc -l | tail -n 1

# Q5
git branch my-local-branch 4177daab2f54bdb20c71f623296a8bb32616fd12
git checkout my-local-branch
ls
git log

# Q6
git checkout 2.13.x

# Q7
git log -- src/compiler/scala/tools/nsc/CompilerCommand.scala

# Q8
git diff 205f1c532d0a1b54a2b1874db4c4a553284911b6 src/compiler/scala/tools/nsc/CompilerCommand.scala

# Q9
git diff ac849228490d5a0e2d3f048d649297d5c59b6ade 2.13.x src/compiler/scala/tools/nsc/CompilerCommand.scala

# Q10
git diff HEAD HEAD~1

# Q11
git log --oneline src/ | wc -l

# Q12
git log v2.10.0 -n 1 --format=%H

# Q13
git log 'v2.13.2'...'v2.13.1' --oneline | wc -l
