#!/bin/bash
cd ../
rm -rf ./logs/*
rm -rf ./dist/services.tar.gz
tar cvf ./dist/services.tar.gz ./config ./src ./mapper ./logs
