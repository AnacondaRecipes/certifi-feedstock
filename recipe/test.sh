#!/usr/bin/env bash
# Run the tests for Certifi

set -ex
export PYTHON_MAJOR_VERSION=$(python -c "import sys; print(sys.version[0:3])")

exists() {
	FULL_PATH="${PREFIX}/${1}"
	if [ -f "${FULL_PATH}" ]; then
		echo "Found ${1}"
	else
		echo "Could not find ${FULL_PATH}"
		exit 1
	fi
}

for i in lib/python$PYTHON_MAJOR_VERSION/site-packages/certifi/{cacert.pem,core.py} ; do
	exists $i
done
