#!/usr/bin/env python
# coding=utf-8
birth = int(raw_input('birth:'))
if birth < 1990:
	print '90前'
elif birth < 2000:
	print '90后'
else:
	print '00后'
