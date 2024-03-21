#!/bin/bash
# Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me! in the response's body
curl -sX PUT -L -d "user_id=98" --header "origin: You got me!" 0.0.0.0:5000/catch_me
