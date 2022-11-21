 uvicorn.run("exam:app", port=443, host='0.0.0.0', reload = True, reload_dirs = ["html_files"], ssl_keyfile="/etc/letsencrypt/live/tlg.gramm.ml/privkey.pem", ssl_certfile="/etc/letsencrypt/live/tlg.gramm.ml/fullchain.pem")
 uvicorn.run("exam:app", host="0.0.0.0",  port=443, log_level="debug", reload = True,  ssl_keyfile="/etc/letsencrypt/live/tlg.gramm.ml/privkey.pem", ssl_certfile="/etc/letsencrypt/live/tlg.gramm.ml/fullchain.pem")

 uvicorn exam:app --host "0.0.0.0"  --port 1443 --log_level "debug" --reload True --reload_dirs ["/var/www/uvic"]  --ssl-keyfile "/etc/letsencrypt/live/tlg.gramm.ml/privkey.pem" --ssl-certfile "/etc/letsencrypt/live/tlg.gramm.ml/fullchain.pem"

uvicorn /var/www/uvic/exam:app --host "0.0.0.0"  --port 1443 --log-level "debug"  --reload-dir "/var/www/uvic"  --ssl-keyfile ./privkey.pem --ssl-certfile ./fullchain.pem
