"""
(This reasoning applies only when ymax < ymin < 0.)

The key observation for this problem can be seen in an example:

  target area: x=20..30, y=-4..-2
  (call these values xmin, xmax, ymin, ymax)

  S..............................
  ...............................
  ....................TTTTTTTTTTT
  ....................TTTTTTTTTTT
  ....................TTTTTTTTTTT

Let's pick an arbitrary initial velocity that lands in the target area.

  initial velocity (xvel,yvel) = 6,2:

  ...........#...#...............
  ......#...........#............
  ...............................
  S...................#..........
  ...............................
  ....................TTTTTTTTTTT
  ....................T*TTTTTTTTT
  ....................TTTTTTTTTTT

Observe the point (x',y'), which is the first moment the probe's elevation
dips below zero. It is marked * in the diagram. Here, y' = -3. More generally,
for any yvel > 0, y' = -yvel - 1.

This leads to the KEY OBSERVATION: In order to maximize apex elevation, we
need to maximize yvel without y' moving past ymin. This maximum is reached at:

  yvel = -ymin - 1

In this example, yvel = 3 (with xvel and target area unchanged) is the desired
maximum (left diagram) -- increasing it any further e.g. to yvel = 4 would
cause * to land outside the target area (right diagram).

  ...............................    ..................#.#..........
  ...............................    ...............#.....#.........
  ...............................    ...............................
  ...............................    ...........#.........#.........
  ...............#..#............    ...............................
  ...........#........#..........    ...............................
  ...............................    ......#..............#.........
  ......#..............#.........    ...............................
  ...............................    ...............................
  ...............................    ...............................
  S....................#.........    S....................#.........
  ...............................    ...............................
  ....................TTTTTTTTTTT    ....................TTTTTTTTTTT
  ....................TTTTTTTTTTT    ....................TTTTTTTTTTT
  ....................T*TTTTTTTTT    ....................TTTTTTTTTTT
  ...............................    .....................*.........
"""

import sys
from util import findints


def main():
    # Parse. We don't actually need anything other than ymin.
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    xmin, xmax, ymin, ymax = findints(f.read())

    assert ymax < 0

    # Find yvel (as described above).
    yvel = -ymin - 1

    # Find apex elevation. Actually, this is the yvel'th triangular number :)
    y = 0
    while yvel:
        y += yvel
        yvel -= 1
    print(y)


if __name__ == '__main__':
    main()
