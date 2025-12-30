#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Ryuta Kawamoto ryu073000@i.softbank.jp
# SPDX-License-Identifier: BSD-3-Clause

ng(){
	echo ${1}行目が違うよ
	res=1
}

res=0
### NORMAL INPUT ###
out=$(echo "林檎 100" | ./mkcon)
[ "${out}" = 100.0 ] || ng "$LINENO"

out=$(echo apple 10000 | ./mkcon)
[ "$?" = 0 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

### ENPTY INPUT ###
out=$(echo | ./mkcon)
[ "$?" = 0 ] || ng "$LINENO"

### STRANGE  INPUT ###
out=$(echo a a 100 | ./mkcon)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(echo a a | ./mkcon)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res


