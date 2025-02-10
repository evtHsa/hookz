#!/usr/bin/python3.5

import os
import subprocess
import sys
import pdb

# DONT USE PRINT UNLESS UNAVOIDABLE

def emit(msg):
    print("## %s: %s" % (sys.argv[0], msg))

def exit(val):
    sys.exit(val)

def argc():
    return len(sys.argv)

def argv(index):
    return sys.argv[index]

def show_args():
    emit("##: hook: %s" % (sys.argv[1:]))

def sha_expr_to_sha(sha_expr): #ex: HEAD~5, HEAD^, <sha_id>^, ...
    result = subprocess.run("git rev-parse  HEAD",
                            shell=True, stdout=subprocess.PIPE)
    return result.stdout.decode("latin-1").strip()
   
def getenv_ifset(vbl_name):
    try:
        val = os.environ[vbl_name]
    except:
        val = None
        
def check_github_comment_preserving_hooks_enabled():
    if getenv_ifset("DISABLE_GITHUB_COMMENT_HOOKS") == 'y':
        emit("DISABLE_GITHUB_COMMENT_HOOKS set github comments not saved")
        return False
    else:
        emit("DISABLE_GITHUB_COMMENT_HOOKS set github comments saved")
        return True
