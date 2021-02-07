#!/usr/bin/env python

import re
from collections import defaultdict


class FilterModule(object):
	def filters(self):
		return {
			'parse' : self.parseCpuInfo,
			'idMap' : self.getIdMap,
			'vcpuMap' : self.getVcpuMap
		}

	def parseCpuInfo(self, proc_cpuinfo):
		numericRegex = r'^[+-]{0,1}((\d*\.)|\d*)\d+$'

		proc = dict()
		cpuinfo = list()
		# cpuinfo.append(proc)
		for line in proc_cpuinfo:
			line = line.strip()
			if line:
				keyval = [x.strip() for x in line.split(':')]
				if not keyval[1]:
					value = None
				elif keyval[1].isdigit():
					value = int(keyval[1])
				elif re.match(numericRegex, keyval[1]):
					value = float(keyval[1])
				elif keyval[1].lower() in ('true', 'yes', 'on'):
					value = True
				elif keyval[1].lower() in ('false', 'no', 'off'):
					value = False
				else:
					value = keyval[1]

				proc[keyval[0]] = value
			elif proc:
				cpuinfo.append(proc)
				proc = dict()
		# remove empty processor
		if proc:
			cpuinfo.append(proc)
		return cpuinfo

	def getCoreIdDict(self, cpuinfo):
		ret = defaultdict(list)
		for processor in cpuinfo:
			ret[processor['core id']].append(processor)
		return ret

	def getProcIdsByCoreId(self, core_id, core_id_dict):
		processors = core_id_dict[core_id]
		return [x['processor'] for x in core_id_dict[core_id]]

	def getIdMap(self, proc_cpuinfo):
		core_id_dict = self.getCoreIdDict(self.parseCpuInfo(proc_cpuinfo))
		core_ids = core_id_dict.keys()
		idmap = dict()
		for core_id in core_ids:
			idmap[core_id] = self.getProcIdsByCoreId(core_id, core_id_dict)
		return idmap

	def getVcpuMap(self, proc_cpuinfo):
		idmap = self.getIdMap(proc_cpuinfo)
		vcpuMap = dict()
		natural_id = 0
		for core_id in sorted(idmap.keys()):
			for vcpu_id in sorted(idmap[core_id]):
				vcpuMap[natural_id] = vcpu_id
				natural_id += 1
		return vcpuMap

import sys
# TODO: remove these
import json
print(json.dumps(FilterModule().getVcpuMap(sys.stdin.readlines())))
