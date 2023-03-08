tvShows = {
    "theXFiles": {
        "season1": {
            "episodes": ["scaryMonster","scaryAlien"],
            "genre": "scienceFiction",
            "year":1993
        },
        "season2":{
            "episode2":["scaryConspiracy"],
            "genre":"horror",
            "year":1994
        }   
    },
    "lost" : {
        "season1" : {
            "episodes" : ["what the the heck is happening on this island?"],
            "genre"  : "scienceFiction",
            "year" : 2004
        }
    }
}


#print(tvShows)

#accessing nested elements
print(tvShows["theXFiles"]["season1"]["episodes"][1]) #op: scaryAlien
