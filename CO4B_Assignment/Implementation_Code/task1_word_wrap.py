"""
Task 1: Word Wrap as a Document-Layout Engine
Dynamic Programming Solution
Penalty for line with spaces: spaces^3. Last line penalty = 0.
"""
def word_wrap_dp(words, line_width):
    n = len(words)
    lens = [len(w) for w in words]
    
    # lc[i][j]: extra spaces on a line containing words i to j
    # cost[i][j]: penalty
    cost = [[0]*n for _ in range(n)]
    for i in range(n):
        cur_len = -1
        for j in range(i, n):
            cur_len += lens[j] + 1
            spaces = line_width - cur_len
            if spaces < 0:
                cost[i][j] = float('inf')
            elif j == n - 1:
                cost[i][j] = 0 # Final line carries no penalty
            else:
                cost[i][j] = spaces ** 3

    dp = [float('inf')] * (n + 1)
    split = [0] * (n + 1)
    dp[0] = 0

    for j in range(1, n + 1):
        for i in range(1, j + 1):
            if cost[i-1][j-1] != float('inf') and dp[i-1] + cost[i-1][j-1] < dp[j]:
                dp[j] = dp[i-1] + cost[i-1][j-1]
                split[j] = i - 1

    # Reconstruct lines
    lines = []
    curr = n
    while curr > 0:
        prev = split[curr]
        line_words = words[prev:curr]
        used_len = sum(len(w) for w in line_words) + (len(line_words) - 1)
        unused_spaces = line_width - used_len
        line_penalty = 0 if curr == n else unused_spaces ** 3
        lines.append({
            'words': line_words,
            'unused_spaces': unused_spaces,
            'penalty': line_penalty
        })
        curr = prev
    lines.reverse()
    return dp[n], lines

if __name__ == '__main__':
    text = "The quick brown fox jumps over the lazy dog and runs across the wide open green meadow".split()
    widths = [15, 20, 25]
    print(f"Total Words: {len(text)}")
    for w in widths:
        total_pen, lines = word_wrap_dp(text, w)
        print(f"\n--- Word Wrap with Line Width = {w} ---")
        print(f"Minimum Total Penalty: {total_pen}")
        for idx, l in enumerate(lines, 1):
            line_str = " ".join(l['words'])
            print(f"  Line {idx:2d} (len={len(line_str):2d}, unused={l['unused_spaces']:2d}, penalty={l['penalty']:4d}): {line_str}")
