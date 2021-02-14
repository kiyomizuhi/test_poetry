#!/bin/bash

for d in ./src/*/;
  do
    echo $d

    test_dir="tests/test_${d:6:${#d}}"
    init_py="${test_dir}__init__.py"

    if [ ! -d "$test_dir" ]; then
       mkdir ${test_dir}
       echo $test_dir
    fi

    if [ ! -f "${init_py}" ]; then
       touch ${init_py}
       echo $init_py
    fi

  done
