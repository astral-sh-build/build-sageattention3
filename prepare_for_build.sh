#!/bin/bash
# Script to prepare the build environment for SageAttention3 (Blackwell).
#
# Example usage:
#   ./prepare_for_build.sh v0.1.0

set -euxo pipefail

export ROOT=`pwd`

if [ $# -ne 1 ]; then
    echo "Usage: $0 <sageattention3_version>"
    echo "Example: $0 v0.1.0"
    exit 1
fi

SAGEATTENTION3_VERSION=$1

# Apply patches.
patch_dir="${ROOT}/build_scripts/patches/${SAGEATTENTION3_VERSION}"

if [ ! -d "${patch_dir}" ]; then
    echo "No patches to apply for SageAttention3 version ${SAGEATTENTION3_VERSION}"
else
    for patch in "${patch_dir}"/*.patch; do
        if [ -f "${patch}" ]; then
            patch -p1 -d "${ROOT}" -i "${patch}"
        fi
    done
fi
