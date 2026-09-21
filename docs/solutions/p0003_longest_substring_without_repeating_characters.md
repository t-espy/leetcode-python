# Longest Substring Without Repeating Characters

Slide a window `[start, index]` over the string while recording the last
index of each character. When the current character last appeared at or
after `start`, move `start` to one past that earlier occurrence. The window
then holds unique characters, and the answer is the maximum window length.
An empty string keeps length 0; a run of one character keeps length 1.

Time: O(n) for one pass with constant-time map updates.
Extra space: O(min(n, alphabet)) for the last-seen map.
