# ML-GNN Collection Module

The ml-gnn collection module is the primary ingestion engine for the
Eternal Torment repository. It automates the extraction of infrastructure
relationship data from Terraform workspaces, converting HCL digraphs into
structured datasets (DOT, PNG, and JSON metadata) for Graph Neural Network
training.

Results are automatically synced to the backend-datastore GCP bucket for centralized processing.

## Setup & Environment\

Docker (Recommended for Isolation)
To build the collection environment as a containerized workload: `docker build -t gnn-collection .`


Example execution

```sh
cd /home/franklin/workspace/lab-home/terraform # to some terraform dir
python3 ${BASE_DIR}/src/collection/collection.py
```

## native environment (BASH)

Standard setup for Debian/OpenBSD environments utilizing the bash shell:

```sh
./bootstrap.sh
./configure
make python
export BASE_DIR=$(pwd)
source ${BASE_DIR}/_build/bin/activate
export PYTHONPATH=${BASE_DIR}
```

## FISH Shell

For interactive sessions using the `fish` shell:

```sh
./bootstrap.sh
./configure
make python
source /home/franklin/workspace/ml-gnn/_build/bin/activate.fish
set --export PYTHONPATH /home/franklin/workspace/ml-gnn
```

## Execution

Once your environment is active, navigate to any directory containing a Terraform plan to begin collection.

```sh
cd /path/to/your/terraform/workspace
python3 ${BASE_DIR}/src/collection/collection.py
```