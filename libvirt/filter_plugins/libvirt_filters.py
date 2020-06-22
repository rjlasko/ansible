#!/usr/bin/env python

from collections import defaultdict
from itertools import combinations
import functools
import json


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
        return all_cpusets, true_cpusets

    def find_next_cpuset(self, players, scoreboard, ranked, true_cpusets):
        '''
        players: a list of all remaining combinations of indices, not yet ranked
        scoreboard: dict w/ key=index & value=# of times index is ranked
        ranked: list of all combinations previously selected
        '''
        max_score = max(scoreboard.values())
        deficits = {}
        for k, v in scoreboard.items():
            deficits[k] = max_score - v
        projections = defaultdict(int)
        for i in range(len(players)):
            p = players[i]
            for dimension in p:
                projections[i] += deficits[dimension]
        max_projection = max([v for k,v in projections.items()])
        preferred_cpuset_comparator = lambda x,y: self.compare_cpuset(true_cpusets, x, y)
        top_players = sorted([players[k] for k,v in projections.items() if v == max_projection], key=functools.cmp_to_key(preferred_cpuset_comparator))
        winner = top_players[0]
        players.remove(winner)
        ranked.append(winner)
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

    def compare_cpuset(self, true_cpusets, set_a, set_b):
        if (set_a in true_cpusets) != (set_b in true_cpusets):
            if (set_a in true_cpusets):
                return -1
            else:
                return 1
        return self.compare_cpuset_indices(set_a, set_b)

    def cpuset_select(self, physical_logical_dict, physical_core_pool, logical_set_size, count, true_cpusets_only):
        all_cpusets, true_cpusets = self.cpuset_combinations(physical_logical_dict, physical_core_pool, logical_set_size, count)
        true_cpus = []
        [true_cpus.extend(c) for c in true_cpusets]
        ranked_combos = []
        scoreboard = {core: 0 for core in true_cpus}
        cpusets = true_cpusets if true_cpusets_only else all_cpusets
        while (len(cpusets) > 0):
            self.find_next_cpuset(cpusets, scoreboard, ranked_combos, true_cpusets)
        ranked_pretty = [sorted(list(r)) for r in ranked_combos]
        num_ranked = len(ranked_pretty)
        ranked_limited = list()
        for i in range(count):
            ranked_limited.append(ranked_pretty[i % num_ranked])
        return json.dumps(ranked_limited)

    def cpuset_select_export(self, physical_logical_dict, physical_core_pool, logical_set_size, count, true_cpusets_only=False):
        return self.cpuset_select(physical_logical_dict, physical_core_pool, int(logical_set_size), int(count), true_cpusets_only)


# def go():
#     pld = {0: [0, 4], 1: [1, 5], 2: [2, 6], 3: [3, 7]}
#     cnt = 4
#     pcp = [2, 3]
#     lss = 2
#     only_true_cpusets = False
#
#     fm = FilterModule()
#     out = fm.cpuset_select_export(pld, pcp, lss, cnt, only_true_cpusets)
#     print(str(out))
#
# go()
