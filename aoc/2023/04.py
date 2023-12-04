from aoc.problem import Problem


class Promblem2023_04(Problem):
    def solve_input(self, text):
        lines = text.splitlines()
        points = 0
        n_won_cards = [1] * len(lines)
        for i, line in enumerate(lines):
            _game, cards = line.split(':')
            winning, numbers = map(lambda x: set(x.strip().split()), cards.split('|'))
            n_matches = len(winning & numbers)
            points += 2 ** (n_matches - 1) if n_matches > 0 else 0
            for j in range(i + 1, i + n_matches + 1):
                n_won_cards[j] += n_won_cards[i]
        self.part1 = points
        self.part2 = sum(n_won_cards)


Promblem2023_04().solve()
