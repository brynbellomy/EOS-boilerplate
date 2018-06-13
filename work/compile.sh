#!/bin/sh
eosiocpp -o ./contracts/test/test.wast ./contracts/test/test.cpp
eosiocpp -g ./contracts/test/test.abi ./contracts/test/test.cpp
cleos set contract test.code ./contracts/test ./contracts/test/test.wast ./contracts/test/test.abi -p test.code@active




