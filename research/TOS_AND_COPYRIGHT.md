# Terms of use and copyright (2026-09-21)

This file is the legal fence for the repository. Code, tasks, and ratchetloop
briefs follow it.

## Findings

LeetCode `robots.txt` (fetched 2026-09-21) names these disallowed paths for
`User-agent: *`:

- `/api/`
- `/graphql`
- `/problems/*/submit`
- `/problems/*/interpret_solution`
- `/submissions`
- `/accounts`, `/session`, `/progress`, and several other account surfaces

There is no official public API for bulk problem download or bulk judge
submission. Third-party GraphQL clients exist; they talk to endpoints
robots.txt disallows.

LeetCode problem statements, examples, editorials, and hidden tests are
copyrighted literary works. A public GitHub copy of those texts is a
takedown risk. Short titles, numeric ids, and URL slugs are identifiers.

As of a public count on 2026-08-20, LeetCode listed about 4,029 problems, of
which 781 were premium-gated.

## Rules this repo follows

1. Catalog entries hold identifiers and a link: `id`, `title`, `slug`,
   `difficulty`, `category`, `url`, `paid_only`, `status`, `answer_file`.
   No statement, example list, constraint block, or editorial.
2. Tests and writeups are original. They restate the algorithm in our own
   words and use invented inputs.
3. Premium-gated Blind 75 items are recorded as `skipped_premium` and are
   never fetched, restated from memory of the locked page, or solved here.
4. The tree does not call `leetcode.com` at runtime. No session cookie, no
   GraphQL, no `/api/`, no submit.
5. Local pytest is the merge gate. Passing LeetCode's hidden tests would
   require submit, which this project does not do.

## Sources

- `https://leetcode.com/robots.txt` (2026-09-21)
- Public problem-count article using `leetcode.com/api/problems/all/` on
  2026-08-20 (that URL is disallowed for our crawler; we treat the article
  as a secondary count, not a fetch target)
- Yangshun Tay, Blind 75 / Grind 75 curriculum:
  `https://www.techinterviewhandbook.org/grind75/`
