#!/bin/bash
# Q1
git branch
# Q2
git log | head -n 1
# Q3
git checkout 4177daab2f54bdb20c71f623296a8bb32616fd12
# Q4
find . -name '*.java' | xargs wc -l | tail -n 1
# Q5
git branch my-local-branch 4177daab2f54bdb20c71f623296a8bb32616fd12
git checkout 2.13.x
git diff ...  # TODO: difference
# Q6
git checkout 2.13.x
# Q7
git log -- src/compiler/scala/tools/nsc/CompilerCommand.scala
# Q8
git diff 205f1c532d0a1b54a2b1874db4c4a553284911b6 src/compiler/scala/tools/nsc/CompilerCommand.scala
# Q9

# Q10

# Q11

# Q12

# Q13

