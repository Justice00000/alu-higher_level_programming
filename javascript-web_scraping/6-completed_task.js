#!/usr/bin/node
const req = require('request');

function getCompletedTasks (data, userId) {
  let count = 0;
  data
