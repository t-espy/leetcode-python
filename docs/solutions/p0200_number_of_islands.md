# Number of Islands

Scan every cell. When a land cell is found, increment the island count and
flood-fill that component by walking 4-neighbors on a stack, writing water
over each visited land cell so it is not counted again. Diagonal neighbors
are ignored, so two lands that only touch at a corner stay two islands.
An empty map or a map of empty rows yields zero.

Time: O(rows * cols) because each cell is entered a constant number of times.
Extra space: O(rows * cols) for the flood stack in a fully land map. The
grid itself is overwritten in place.
