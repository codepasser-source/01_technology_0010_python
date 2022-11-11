#!/bin/bash
cd ../
rm -rf ./dist/services.tar.gz
tar cvf ./dist/services.tar.gz ./bin ./config ./src ./mapper ./logs
