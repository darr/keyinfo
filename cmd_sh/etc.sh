#!/bin/bash
#####################################
## File name : etc.sh
## Create date : 2018-11-25 15:53
## Modified date : 2019-08-05 15:56
## Author : DARREN
## Describe : not set
## Email : lzygzh@126.com
####################################

realpath=$(readlink -f "$0")
export basedir=$(dirname "$realpath")
export filename=$(basename "$realpath")
export PATH=$PATH:$basedir/dlbase
export PATH=$PATH:$basedir/dlproc
#base sh file
. dlbase.sh
#function sh file

env_path=~/.keyinfo_extract_env
