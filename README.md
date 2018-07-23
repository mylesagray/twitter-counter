# twitter-counter
Tweet counter based on TwitterAPI in a Docker container

# usage
```
docker run \
-e API_KEY={yourAPIkey} \
-e API_SECRET={yourAPIsecret} \
-e ACCESS_TOKEN={yourAccessToken} \
-e ACCESS_TOKEN_SECRET={yourAccessTokenSecret} \
-p 5000:5000 \
mylesagray/twitter-counter
```

# run app
http://localhost:5000/count/{{queryhere}}