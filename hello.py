#!/usr/bin/env python
# coding=utf-8
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'begin call'
		func(*args,**kw)
		print 'end call'
	return wrapper

@log
def now():
	print '2015-04-13'

now()

import functools

def log(arg):
	if callable(arg):
		func = arg
		@functools.wraps(func)
		def wrapper(*args, **kw):
		return wrapper
	else:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
			return wrapper
		return decorator

@log
def f():
	pass

f()

@log('execute')
def f():
	pass

f()



