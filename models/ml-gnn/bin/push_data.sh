#!/usr/bin/env bash
#
# SPDX-FileCopyrightText: 2023 DE:AD:10:C5 <franklin@dead10c5.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

#DATA_FILES=`gcloud alpha storage ls --recursive gs://backend-datastore/dataset`

DATA_FILES=`ls dataset/`

for MY_FILE in ${DATA_FILES}
do
  gcloud alpha storage cp --recursive dataset/${MY_FILE} gs://backend-datastore/dataset
done

# dvc add dataset/*.dvc
# git add dataset/*.dvc 