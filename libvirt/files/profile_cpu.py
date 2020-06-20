#!/usr/bin/env python

import re
from collections import defaultdict

numericRegex = r'^[+-]{0,1}((\d*\.)|\d*)\d+$'

def readNextProcessor(file):
	proc = dict()
	while(True):
		line = file.readline().strip()
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
		else:
			break
	return proc

def readCpuInfo():
	with open('/proc/cpuinfo') as f:
		cpuinfo = list()
		while(True):
			proc = readNextProcessor(f)
			if proc:
				cpuinfo.append(proc)
			else:
				break
	return cpuinfo

def getCoreIdDict(cpuinfo):
	ret = defaultdict(list)
	for processor in cpuinfo:
		ret[processor['core id']].append(processor)
	return ret

def getProcIdsByCoreId(core_id, core_id_dict):
	processors = core_id_dict[core_id]
	return [x['processor'] for x in core_id_dict[core_id]]

def go():
	core_id_dict = getCoreIdDict(readCpuInfo())
	core_ids = core_id_dict.keys()
	coreIdToProcIdDict = dict()
	for core_id in core_ids:
		coreIdToProcIdDict[core_id] = getProcIdsByCoreId(core_id, core_id_dict)
	print(coreIdToProcIdDict)

go()
