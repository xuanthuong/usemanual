1. Lấy link của heroku
heroku apps:info -s  | grep web_url | cut -d= -f2
2. Set heroku link
heroku config:set HEROKU_URL=$(heroku apps:info -s  | grep web_url | cut -d= -f2)
3. Issue when deploy Flask
http://p-s.co.nz/wordpress/deploying-simple-flask-app-on-heroku/
4. Chú ý add buildpacks: heroku buildpacks:set heroku/python
5. add file runtime.txt với python version
