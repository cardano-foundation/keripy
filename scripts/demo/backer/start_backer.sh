#!/bin/bash

CONFIG_DIR=${CONFIG_DIR:-$PWD}
BACKER_CONFIG_FILE=${BACKER_CONFIG_FILE:-$CONFIG_DIR/cf/backer.json}
WITROOT_CONFIG_FILE=${WITROOT_CONFIG_FILE:-$CONFIG_DIR/witroot-config.json}
BACKER_HOST=${BACKER_HOST:-localhost}
BACKER_URL=${BACKER_URL:-http://$BACKER_HOST:5666}

mkdir -p $CONFIG_DIR/cf
cat > $BACKER_CONFIG_FILE <<EOF
{
  "witroot": {
    "dt": "2022-01-20T12:57:59.823350+00:00",
    "curls": ["tcp://${BACKER_HOST}:5665/", "${BACKER_URL}"]
  },
  "dt": "2022-01-20T12:57:59.823350+00:00",
  "iurls": [
  ]
}
EOF

cat > $WITROOT_CONFIG_FILE <<EOF
{
  "transferable": false,
  "wits": [],
  "icount": 1,
  "ncount": 1,
  "isith": "1",
  "nsith": "1"
}
EOF

kli init --name witroot --nopasscode --config-dir ${CONFIG_DIR} --config-file ${BACKER_CONFIG_FILE}

kli incept --name witroot --alias witroot --config ${CONFIG_DIR} --file ${WITROOT_CONFIG_FILE}

kli backer start --name witroot --alias witroot -H 5666 -T 5665 --ledger cardano
