#!/usr/bin/node
const request = require('request');

// API URL
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// Function to compute the number of completed tasks by user id
function computeCompletedTasksByUserId (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    // Parse the response body
    const todos = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user ID
    const completedTasksByUserId = {};

    // Loop through the todos and count completed tasks for each user ID
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUserId[todo.userId]) {
          completedTasksByUserId[todo.userId]++;
        } else {
          completedTasksByUserId[todo.userId] = 1;
        }
      }
    });

    // Print users with completed tasks
    console.log('Users with completed tasks:');
    for (const userId in completedTasksByUserId) {
      console.log(JSON.stringify(`${userId}:, ${completedTasksByUserId[userId]}`));
    }
  });
}

// Call the function
computeCompletedTasksByUserId(apiUrl);
