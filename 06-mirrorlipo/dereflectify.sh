#!/usr/bin/env bash
# Reflecty:   aciklmnouvwxABCDEHIKMOTUVWXY0138
# Irreflecty: bdefghjpqrstyzFGJLNPQRSZ245679

egrep -v "[bdefghjpqrstyzFGJLNPQRSZ245679]" $1 | egrep "[.]+"
