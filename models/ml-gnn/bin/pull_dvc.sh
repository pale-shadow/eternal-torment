#!/usr/bin/env bash
#
# SPDX-FileCopyrightText: 2023 DE:AD:10:C5 <franklin@dead10c5.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

DATA_FILES=`gcloud alpha storage ls --recursive gs://backend-datastore/dataset`

for MY_FILE in ${DATA_FILES}
do
  asdf=`echo $MY_FILE | cut -f2 -d'.' `
  if [ $asdf = "dot" ] || [ $asdf = "png" ]; then
    newfile=`echo ${MY_FILE} | cut -f5 -d'/'`
    if [ -f "dataset/${newfile}" ]; then
      echo "Skipping dataset/${newfile} because we found a local copy."
    else
      echo "Getting dataset/${newfile}"
      dvc get-url ${MY_FILE} dataset/${newfile}
    fi
  fi
done

# dvc add dataset/*.dvc
# git add dataset/*.dvc 
