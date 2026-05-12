#!/bin/bash
set -e

AZP_AGENT_NAME=${AZP_AGENT_NAME:-$(hostname)}

./config.sh \
  --unattended \
  --url "$AZP_URL" \
  --auth pat \
  --token "$AZP_TOKEN" \
  --pool "$AZP_POOL" \
  --agent "$AZP_AGENT_NAME" \
  --replace \
  --acceptTeeEula

cleanup() {
  ./config.sh remove --unattended --auth pat --token "$AZP_TOKEN"
}

trap cleanup EXIT

./run.sh
