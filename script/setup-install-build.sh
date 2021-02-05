#!/usr/bin/env bash

echo '--- api repo setup'
cd acorn-api
direnv allow
api/script/dev-setup
yarn install
cd ./api
yarn build
yarn migrate up
cd .. && cd ..

echo '--- api referral component setup'
cd acorn-referral-component
direnv allow
script/dev-setup 
yarn install
cd component
yarn create-db
yarn build
cd .. && cd ..

echo '--- api referral view data'
cd acorn-referral-viewdata
direnv allow
script/dev-setup 
yarn install
yarn create-viewdata-db
yarn build
cd ..

echo '--- api referral web client'
cd acorn-web-client
script/dev-setup
yarn install
cd ..

