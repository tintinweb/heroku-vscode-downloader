# VSCode Extension Downloader - Heroku App

A simple PoC for a heroku web-app to download vscode extensions for offline use. → https://vscode-downloader.herokuapp.com/

![screenshot](https://user-images.githubusercontent.com/2865694/64946465-3bf10280-d873-11e9-84e7-9d681c6676f0.png)



## heroku deployment notes

```console
### one time
$ heroku create  # create app
$ heroku ps:scale web=1

### for every modification
$ git push heroku master  # deploy app

### after deployment
$ heroku open  # open heroku webapp
$ heroku logs — tail  # tail remote logs
``` 
