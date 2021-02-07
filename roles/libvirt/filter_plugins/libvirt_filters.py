#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import functools
import json
import fractions

class FilterModule(object):
    def filters(self):
        return {'cpuset_select': self.cpuset_select_export}

    def cpuset_combinations(self, physical_logical_dict, physical_core_pool, logical_set_size, count):
        selected_logical_pool = set()
        true_cpusets = list()
        for physical_core_id in physical_core_pool:
            logical_cores = physical_logical_dict.get(physical_core_id)
            selected_logical_pool.update(logical_cores)
            true_cpusets.append(set(logical_cores))
        all_cpusets = list()
        for logical_combination in list(combinations(selected_logical_pool, logical_set_size)):
            all_cpusets.append(set(logical_combination))

        # find commonly divisible cpuset size
        true_cpuset_size = len(true_cpusets[0])
        for v in true_cpusets:
            assert len(v) == true_cpuset_size
        common_cpuset_size = fractions.gcd(true_cpuset_size, logical_set_size)

        # determine common cpusets
        if common_cpuset_size == true_cpuset_size:
            common_cpusets = true_cpusets
        else:
            common_cpusets = list()
            for true_cset in true_cpusets:
                true_sorted_cset = sorted(true_cset)
                for i in range(true_cpuset_size):
                    if i % common_cpuset_size == 0:
                        common_cpusets.append(set())
                    common_cpusets[-1].add(true_sorted_cset[i])

        return all_cpusets, common_cpusets

    def find_next_cpuset(self, players, scoreboard, ranked, true_cpusets):
        '''
        players: a list of all remaining combinations of indices, not yet ranked
        scoreboard: dict w/ key=index & value=# of times index is ranked
        ranked: list of all combinations previously selected
        '''
        # find the highest score across all indices that a player is aligned with
        max_score = max(scoreboard.values())
        deficits = {}
        # find the deficit for each index (ie. logical_core_id)
        for k, v in scoreboard.items():
            deficits[k] = max_score - v
        # project the for each player in this round
        projections = defaultdict(int)
        for i in range(len(players)):
            p = players[i]
            # the score is the sum of the deficits for a player's given indices
            for dimension in p:
                projections[i] += deficits[dimension]
        # find out the best score across all players
        max_projection = max([v for k,v in projections.items()])
        # sort players with highest score using comparator
        preferred_cpuset_comparator = lambda x,y: self.compare_cpuset(true_cpusets, x, y)
        top_players = sorted([players[k] for k,v in projections.items() if v == max_projection], key=functools.cmp_to_key(preferred_cpuset_comparator))
        # pick the winner for this round
        winner = top_players[0]
        players.remove(winner)
        ranked.append(winner)
        # update the scoreboard
        for dimension in winner:
            scoreboard[dimension] += 1

    def compare_cpuset_indices(self, set_a, set_b):
        assert len(set_a) == len(set_b)
        list_a = sorted(set_a)
        list_b = sorted(set_b)
        for i in range(len(set_a)):
            if list_a[i] != list_b[i]:
                return -1 if list_a[i] < list_b[i] else 1
        return 0

    def compare_common_cpusets(self, common_cpusets, set_a, set_b):
        if set_a == set_b:
            return 0
        for cset in common_cpusets:
            if cset == set_a:
                return -1
            if cset == set_b:
                return 1
        raise Exception('unhandled1');

    def compare_cpuset(self, common_cpusets, set_a, set_b):
        if (set_a in common_cpusets) != (set_b in common_cpusets):
            if (set_a in common_cpusets):
                return -1
            else:
                return 1
        if (set_a in common_cpusets) and (set_b in common_cpusets):
            return self.compare_common_cpusets(common_cpusets, set_a, set_b)
        return self.compare_cpuset_indices(set_a, set_b)

    def cpuset_select(self, physical_logical_dict, physical_core_pool, logical_set_size, count, common_cpusets_only):
        all_cpusets, common_cpusets = self.cpuset_combinations(physical_logical_dict, physical_core_pool, logical_set_size, count)
        true_cpus = []
        [true_cpus.extend(c) for c in common_cpusets]
        ranked_combos = []
        scoreboard = {core: 0 for core in true_cpus}
        cpusets = common_cpusets if common_cpusets_only else all_cpusets

        while (len(cpusets) > 0):
            self.find_next_cpuset(cpusets, scoreboard, ranked_combos, common_cpusets)

        ranked_pretty = [sorted(list(r)) for r in ranked_combos]
        num_ranked = len(ranked_pretty)
        ranked_limited = list()
        for i in range(count):
            ranked_limited.append(ranked_pretty[i % num_ranked])
        return json.dumps(ranked_limited)

    def cpuset_select_export(self, physical_logical_dict, physical_core_pool, logical_set_size, count, common_cpusets_only=False):
        return self.cpuset_select(physical_logical_dict, physical_core_pool, int(logical_set_size), int(count), common_cpusets_only)


# def go():
#     pld = {0: [0, 4], 1: [1, 5], 2: [2, 6], 3: [3, 7]}
#     cnt = 4
#     pcp = [2, 3]
#     lss = 1
#     only_common_cpusets = False
#
#     fm = FilterModule()
#     out = fm.cpuset_select_export(pld, pcp, lss, cnt, only_common_cpusets)
#     print(str(out))
#
# go()
